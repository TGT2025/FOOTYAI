"""
Form Analyzer Agent

Analyzes team form, momentum, and recent performance trends to predict match outcomes.
"""

from typing import Dict, Any, List
from datetime import datetime, timedelta

class FormAnalyzerAgent:
    """
    Analyzes team form and momentum to predict match outcomes.
    
    Key Metrics:
    - Recent match results (W/D/L)
    - Goals scored/conceded trends
    - Home/away performance splits
    - Winning/losing streaks
    - Points per game trends
    """
    
    def __init__(self):
        self.name = "FormAnalyzerAgent"
        self.lookback_matches = 5
        self.home_weight = 1.3  # Home advantage factor
        
    def analyze(self, fixture_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze team form for the given fixture
        
        Args:
            fixture_data: Dictionary with fixture information including:
                - home_team: str
                - away_team: str
                - home_team_id: int
                - away_team_id: int
                
        Returns:
            Dictionary with prediction and confidence
        """
        try:
            # Extract team information
            home_team = fixture_data.get('home_team', 'Unknown')
            away_team = fixture_data.get('away_team', 'Unknown')
            
            # Calculate form scores (simplified - would use real data in production)
            home_form_score = self._calculate_form_score(home_team, is_home=True)
            away_form_score = self._calculate_form_score(away_team, is_home=False)
            
            # Apply home advantage
            adjusted_home_score = home_form_score * self.home_weight
            
            # Determine prediction
            if adjusted_home_score > away_form_score * 1.2:
                prediction = "home_win"
                confidence = min(0.85, (adjusted_home_score / away_form_score) * 0.6)
            elif away_form_score > adjusted_home_score * 1.2:
                prediction = "away_win"
                confidence = min(0.85, (away_form_score / adjusted_home_score) * 0.6)
            else:
                prediction = "draw_or_close"
                confidence = 0.55
            
            return {
                'prediction': prediction,
                'confidence': confidence,
                'form_analysis': {
                    'home_form_score': home_form_score,
                    'away_form_score': away_form_score,
                    'home_advantage_applied': True
                }
            }
            
        except Exception as e:
            # Return default prediction on error
            return {
                'prediction': 'unknown',
                'confidence': 0.5,
                'error': str(e)
            }
    
    def _calculate_form_score(self, team: str, is_home: bool) -> float:
        """
        Calculate form score for a team (0-10 scale)
        
        In production, this would:
        - Query recent match results
        - Calculate win/draw/loss ratios
        - Analyze goals scored/conceded
        - Consider home/away splits
        
        For now, returns a simulated score based on team name hash
        """
        # Simulate form score (replace with real data in production)
        import hashlib
        team_hash = int(hashlib.md5(team.encode()).hexdigest(), 16)
        base_score = (team_hash % 60) / 10 + 3  # Range: 3-9
        
        # Adjust for home/away
        if is_home:
            base_score += 0.5
        
        return min(10.0, base_score)
    
    def _analyze_recent_matches(self, team_id: int, recent_matches: List[Dict]) -> Dict:
        """
        Analyze recent match performance
        
        Args:
            team_id: Team identifier
            recent_matches: List of recent match data
            
        Returns:
            Dictionary with form metrics
        """
        if not recent_matches:
            return {
                'wins': 0,
                'draws': 0,
                'losses': 0,
                'goals_scored': 0,
                'goals_conceded': 0,
                'form_trend': 'unknown'
            }
        
        wins = draws = losses = 0
        goals_scored = goals_conceded = 0
        
        for match in recent_matches[-self.lookback_matches:]:
            # Determine if team was home or away
            is_home = match.get('home_team_id') == team_id
            
            home_goals = match.get('home_goals', 0)
            away_goals = match.get('away_goals', 0)
            
            if is_home:
                team_goals = home_goals
                opponent_goals = away_goals
            else:
                team_goals = away_goals
                opponent_goals = home_goals
            
            goals_scored += team_goals
            goals_conceded += opponent_goals
            
            # Determine result
            if team_goals > opponent_goals:
                wins += 1
            elif team_goals == opponent_goals:
                draws += 1
            else:
                losses += 1
        
        # Calculate form trend
        points = wins * 3 + draws
        max_points = len(recent_matches[-self.lookback_matches:]) * 3
        form_percentage = points / max_points if max_points > 0 else 0
        
        if form_percentage >= 0.7:
            form_trend = 'excellent'
        elif form_percentage >= 0.5:
            form_trend = 'good'
        elif form_percentage >= 0.3:
            form_trend = 'average'
        else:
            form_trend = 'poor'
        
        return {
            'wins': wins,
            'draws': draws,
            'losses': losses,
            'goals_scored': goals_scored,
            'goals_conceded': goals_conceded,
            'form_percentage': form_percentage,
            'form_trend': form_trend
        }
    
    def get_insights(self, fixture_data: Dict[str, Any]) -> List[str]:
        """
        Generate human-readable insights about team form
        
        Returns:
            List of insight strings
        """
        analysis = self.analyze(fixture_data)
        insights = []
        
        prediction = analysis.get('prediction', 'unknown')
        confidence = analysis.get('confidence', 0.5)
        
        insights.append(f"Form prediction: {prediction} (confidence: {confidence:.2%})")
        
        form_details = analysis.get('form_analysis', {})
        if form_details:
            home_score = form_details.get('home_form_score', 0)
            away_score = form_details.get('away_form_score', 0)
            insights.append(f"Home form: {home_score:.1f}/10, Away form: {away_score:.1f}/10")
        
        return insights
