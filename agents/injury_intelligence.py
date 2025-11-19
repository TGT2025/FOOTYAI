"""
Injury Intelligence Agent

Tracks player injuries, lineup changes, and their impact on team performance.
"""

from typing import Dict, Any, List
import random

class InjuryIntelligenceAgent:
    """
    Analyzes player availability and injury impacts on team strength.
    
    Key Metrics:
    - Key player availability
    - Injury severity and duration
    - Squad depth analysis
    - Lineup strength comparison
    - Formation stability
    """
    
    def __init__(self):
        self.name = "InjuryIntelligenceAgent"
        self.key_position_weights = {
            'goalkeeper': 0.15,
            'defender': 0.25,
            'midfielder': 0.30,
            'forward': 0.30
        }
    
    def analyze(self, fixture_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze injury situation for the given fixture
        
        Args:
            fixture_data: Dictionary with fixture information
            
        Returns:
            Dictionary with prediction and confidence
        """
        try:
            home_team = fixture_data.get('home_team', 'Unknown')
            away_team = fixture_data.get('away_team', 'Unknown')
            
            # Calculate lineup strength (would use real injury data in production)
            home_lineup_strength = self._calculate_lineup_strength(home_team)
            away_lineup_strength = self._calculate_lineup_strength(away_team)
            
            # Determine impact
            strength_diff = abs(home_lineup_strength - away_lineup_strength)
            
            if strength_diff < 0.1:
                prediction = "equal_strength"
                confidence = 0.6
            elif home_lineup_strength > away_lineup_strength:
                prediction = "home_advantage"
                confidence = min(0.9, 0.6 + strength_diff * 2)
            else:
                prediction = "away_advantage"
                confidence = min(0.9, 0.6 + strength_diff * 2)
            
            return {
                'prediction': prediction,
                'confidence': confidence,
                'injury_analysis': {
                    'home_lineup_strength': home_lineup_strength,
                    'away_lineup_strength': away_lineup_strength,
                    'strength_difference': strength_diff
                }
            }
            
        except Exception as e:
            return {
                'prediction': 'unknown',
                'confidence': 0.5,
                'error': str(e)
            }
    
    def _calculate_lineup_strength(self, team: str) -> float:
        """
        Calculate lineup strength considering injuries (0-1 scale)
        
        In production, this would:
        - Query current injury list
        - Assess player importance
        - Evaluate squad depth
        - Consider formation changes
        
        Returns simulated strength score
        """
        import hashlib
        team_hash = int(hashlib.md5(team.encode()).hexdigest(), 16)
        
        # Base strength (70-95%)
        base_strength = 0.7 + (team_hash % 25) / 100
        
        # Simulate injury impact (-0 to -0.2)
        injury_impact = -(team_hash % 20) / 100
        
        final_strength = max(0.5, base_strength + injury_impact)
        return final_strength
    
    def _assess_injury_impact(self, injuries: List[Dict], team_data: Dict) -> Dict:
        """
        Assess the impact of current injuries
        
        Args:
            injuries: List of injured players
            team_data: Team information and squad depth
            
        Returns:
            Dictionary with impact metrics
        """
        total_impact = 0.0
        critical_absences = []
        
        for injury in injuries:
            player_name = injury.get('player_name', 'Unknown')
            position = injury.get('position', 'unknown')
            importance = injury.get('importance', 5)  # 1-10 scale
            
            # Calculate position-specific impact
            position_weight = self.key_position_weights.get(position, 0.2)
            player_impact = (importance / 10) * position_weight
            
            total_impact += player_impact
            
            # Track critical absences
            if importance >= 8:
                critical_absences.append({
                    'player': player_name,
                    'position': position,
                    'impact': player_impact
                })
        
        # Normalize total impact to 0-1 scale
        normalized_impact = min(1.0, total_impact)
        
        # Determine severity
        if normalized_impact >= 0.3:
            severity = 'severe'
        elif normalized_impact >= 0.15:
            severity = 'moderate'
        elif normalized_impact > 0:
            severity = 'minor'
        else:
            severity = 'none'
        
        return {
            'total_impact': normalized_impact,
            'severity': severity,
            'critical_absences': critical_absences,
            'affected_positions': list(set(i.get('position') for i in injuries))
        }
    
    def get_insights(self, fixture_data: Dict[str, Any]) -> List[str]:
        """Generate human-readable injury insights"""
        analysis = self.analyze(fixture_data)
        insights = []
        
        prediction = analysis.get('prediction', 'unknown')
        confidence = analysis.get('confidence', 0.5)
        
        insights.append(f"Injury impact: {prediction} (confidence: {confidence:.2%})")
        
        injury_details = analysis.get('injury_analysis', {})
        if injury_details:
            home_strength = injury_details.get('home_lineup_strength', 0)
            away_strength = injury_details.get('away_lineup_strength', 0)
            insights.append(f"Lineup strength - Home: {home_strength:.1%}, Away: {away_strength:.1%}")
        
        return insights
