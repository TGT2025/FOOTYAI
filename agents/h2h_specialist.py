"""
Head-to-Head Specialist Agent

Analyzes historical matchup patterns and style compatibility between teams.
"""

from typing import Dict, Any, List
from datetime import datetime

class H2HSpecialistAgent:
    """
    Analyzes head-to-head historical data and matchup patterns.
    
    Key Metrics:
    - Historical results between teams
    - Venue-specific performance
    - Recent h2h trends
    - Style matchup compatibility
    - Psychological factors
    """
    
    def __init__(self):
        self.name = "H2HSpecialistAgent"
        self.h2h_lookback_matches = 10
        self.recent_weight = 1.5  # Weight recent matches higher
    
    def analyze(self, fixture_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze head-to-head history for the given fixture
        
        Args:
            fixture_data: Dictionary with fixture information
            
        Returns:
            Dictionary with prediction and confidence
        """
        try:
            home_team = fixture_data.get('home_team', 'Unknown')
            away_team = fixture_data.get('away_team', 'Unknown')
            
            # Calculate h2h dominance score
            h2h_score = self._calculate_h2h_score(home_team, away_team)
            
            # Determine prediction based on h2h history
            if h2h_score > 0.6:
                prediction = "home_historical_advantage"
                confidence = min(0.85, 0.5 + h2h_score * 0.4)
            elif h2h_score < 0.4:
                prediction = "away_historical_advantage"
                confidence = min(0.85, 0.5 + (1 - h2h_score) * 0.4)
            else:
                prediction = "balanced_h2h"
                confidence = 0.55
            
            return {
                'prediction': prediction,
                'confidence': confidence,
                'h2h_analysis': {
                    'h2h_score': h2h_score,
                    'historical_edge': 'home' if h2h_score > 0.55 else 'away' if h2h_score < 0.45 else 'balanced'
                }
            }
            
        except Exception as e:
            return {
                'prediction': 'unknown',
                'confidence': 0.5,
                'error': str(e)
            }
    
    def _calculate_h2h_score(self, home_team: str, away_team: str) -> float:
        """
        Calculate h2h dominance score (0-1, where 1 = complete home dominance)
        
        In production, this would:
        - Query historical h2h matches
        - Weight recent results higher
        - Consider venue-specific results
        - Analyze goal differences
        
        Returns simulated h2h score
        """
        import hashlib
        
        # Create deterministic but varied score based on team matchup
        combined = f"{home_team}_{away_team}"
        matchup_hash = int(hashlib.md5(combined.encode()).hexdigest(), 16)
        
        # Generate score in range 0.2-0.8 to avoid extreme predictions
        base_score = 0.2 + (matchup_hash % 60) / 100
        
        return base_score
    
    def _analyze_h2h_history(self, home_team_id: int, away_team_id: int, 
                            h2h_matches: List[Dict]) -> Dict:
        """
        Analyze head-to-head match history
        
        Args:
            home_team_id: Home team identifier
            away_team_id: Away team identifier
            h2h_matches: List of historical h2h matches
            
        Returns:
            Dictionary with h2h metrics
        """
        if not h2h_matches:
            return {
                'total_matches': 0,
                'home_wins': 0,
                'away_wins': 0,
                'draws': 0,
                'dominance': 'no_data'
            }
        
        recent_matches = h2h_matches[-self.h2h_lookback_matches:]
        
        home_wins = away_wins = draws = 0
        total_home_goals = total_away_goals = 0
        
        for i, match in enumerate(recent_matches):
            # Weight recent matches higher
            match_weight = 1.0 + (i / len(recent_matches)) * (self.recent_weight - 1)
            
            # Determine which team was home in this match
            match_home_id = match.get('home_team_id')
            home_goals = match.get('home_goals', 0)
            away_goals = match.get('away_goals', 0)
            
            # Determine result from perspective of current home team
            if match_home_id == home_team_id:
                team_goals = home_goals
                opponent_goals = away_goals
            else:
                team_goals = away_goals
                opponent_goals = home_goals
            
            total_home_goals += team_goals * match_weight
            total_away_goals += opponent_goals * match_weight
            
            # Count results with weighting
            if team_goals > opponent_goals:
                home_wins += match_weight
            elif team_goals < opponent_goals:
                away_wins += match_weight
            else:
                draws += match_weight
        
        # Calculate dominance
        total_weighted_matches = home_wins + away_wins + draws
        home_dominance = home_wins / total_weighted_matches if total_weighted_matches > 0 else 0
        
        if home_dominance >= 0.6:
            dominance = 'home_dominant'
        elif home_dominance <= 0.3:
            dominance = 'away_dominant'
        else:
            dominance = 'balanced'
        
        return {
            'total_matches': len(recent_matches),
            'home_wins': home_wins,
            'away_wins': away_wins,
            'draws': draws,
            'home_dominance_pct': home_dominance,
            'dominance': dominance,
            'avg_home_goals': total_home_goals / len(recent_matches) if recent_matches else 0,
            'avg_away_goals': total_away_goals / len(recent_matches) if recent_matches else 0
        }
    
    def get_insights(self, fixture_data: Dict[str, Any]) -> List[str]:
        """Generate human-readable h2h insights"""
        analysis = self.analyze(fixture_data)
        insights = []
        
        prediction = analysis.get('prediction', 'unknown')
        confidence = analysis.get('confidence', 0.5)
        
        insights.append(f"H2H prediction: {prediction} (confidence: {confidence:.2%})")
        
        h2h_details = analysis.get('h2h_analysis', {})
        if h2h_details:
            edge = h2h_details.get('historical_edge', 'unknown')
            insights.append(f"Historical edge: {edge}")
        
        return insights
