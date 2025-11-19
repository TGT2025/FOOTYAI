#!/usr/bin/env python3
"""
Demo script for the Autonomous Football Betting System

This script demonstrates the core capabilities without requiring API keys
or running the full autonomous operation.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.form_analyzer import FormAnalyzerAgent
from agents.injury_intelligence import InjuryIntelligenceAgent
from agents.h2h_specialist import H2HSpecialistAgent
from agents.odds_value_hunter import OddsValueHunterAgent

def print_section(title: str):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)

def demo_agent_predictions():
    """Demonstrate individual agent predictions"""
    print_section("AGENT PREDICTIONS DEMO")
    
    # Sample fixture data
    fixture = {
        'fixture_id': 'demo_001',
        'home_team': 'Manchester United',
        'away_team': 'Liverpool',
        'home_team_id': 33,
        'away_team_id': 40,
        'league_id': 39,  # Premier League
        'timestamp': '2024-11-16T15:00:00Z'
    }
    
    print(f"\n📊 Fixture: {fixture['home_team']} vs {fixture['away_team']}")
    print(f"   League ID: {fixture['league_id']} | Match ID: {fixture['fixture_id']}\n")
    
    # Initialize agents
    agents = {
        'Form Analyzer': FormAnalyzerAgent(),
        'Injury Intelligence': InjuryIntelligenceAgent(),
        'H2H Specialist': H2HSpecialistAgent(),
        'Odds Value Hunter': OddsValueHunterAgent()
    }
    
    # Get predictions from each agent
    predictions = {}
    for agent_name, agent in agents.items():
        print(f"\n🤖 {agent_name}:")
        analysis = agent.analyze(fixture)
        predictions[agent_name] = analysis
        
        prediction = analysis.get('prediction', 'unknown')
        confidence = analysis.get('confidence', 0)
        
        print(f"   Prediction: {prediction}")
        print(f"   Confidence: {confidence:.1%}")
        
        # Show detailed analysis if available
        if agent_name == 'Form Analyzer' and 'form_analysis' in analysis:
            details = analysis['form_analysis']
            print(f"   Home Form: {details.get('home_form_score', 0):.1f}/10")
            print(f"   Away Form: {details.get('away_form_score', 0):.1f}/10")
            
        elif agent_name == 'Injury Intelligence' and 'injury_analysis' in analysis:
            details = analysis['injury_analysis']
            print(f"   Home Lineup: {details.get('home_lineup_strength', 0):.1%}")
            print(f"   Away Lineup: {details.get('away_lineup_strength', 0):.1%}")
            
        elif agent_name == 'H2H Specialist' and 'h2h_analysis' in analysis:
            details = analysis['h2h_analysis']
            print(f"   Historical Edge: {details.get('historical_edge', 'unknown')}")
            
        elif agent_name == 'Odds Value Hunter' and 'odds_analysis' in analysis:
            details = analysis['odds_analysis']
            value_edge = details.get('value_edge', 0)
            best_odds = details.get('best_odds', 0)
            print(f"   Value Edge: {value_edge:.1%}")
            print(f"   Best Odds: {best_odds:.2f}")
    
    return predictions

def demo_agent_fusion(predictions):
    """Demonstrate weighted agent fusion"""
    print_section("AGENT FUSION DEMO")
    
    print("\n🎯 Fusing agent predictions using weighted consensus...\n")
    
    # Agent weights (from AGENTSADD)
    agent_weights = {
        'Form Analyzer': 0.7,
        'Injury Intelligence': 0.8,
        'H2H Specialist': 0.6,
        'Odds Value Hunter': 0.9
    }
    
    print("Agent Weights:")
    for agent, weight in agent_weights.items():
        print(f"   {agent}: {weight:.1f}")
    
    # Calculate weighted average confidence
    total_weighted_confidence = 0
    total_weight = 0
    
    print("\nWeighted Contributions:")
    for agent_name, prediction_data in predictions.items():
        weight = agent_weights.get(agent_name, 0.5)
        confidence = prediction_data.get('confidence', 0.5)
        weighted_confidence = confidence * weight
        
        total_weighted_confidence += weighted_confidence
        total_weight += weight
        
        print(f"   {agent_name}: {confidence:.1%} × {weight:.1f} = {weighted_confidence:.2f}")
    
    # Calculate consensus
    fusion_threshold = 0.65
    consensus_confidence = total_weighted_confidence / total_weight if total_weight > 0 else 0
    consensus = consensus_confidence > fusion_threshold
    
    print(f"\n📊 Fusion Results:")
    print(f"   Consensus Confidence: {consensus_confidence:.1%}")
    print(f"   Fusion Threshold: {fusion_threshold:.1%}")
    print(f"   Recommendation: {'✅ BET' if consensus else '❌ NO BET'}")
    
    if consensus:
        # Determine bet type based on strongest signal
        bet_recommendation = "Value bet based on multi-agent consensus"
        print(f"   Bet Type: {bet_recommendation}")
        print(f"   Suggested Stake: {min(0.1, consensus_confidence * 0.15):.2%} of bankroll")

def demo_system_config():
    """Show system configuration"""
    print_section("SYSTEM CONFIGURATION")
    
    print("\n⚙️ Elite Performance Targets:")
    targets = {
        "Min Win Rate": "71%",
        "Min Profit Margin": "26%",
        "Max Stake per Bet": "10%",
        "Daily Bet Target": "17",
        "Multi-League Coverage": "8+",
        "Bet Type Diversity": "6 types"
    }
    
    for key, value in targets.items():
        print(f"   {key}: {value}")
    
    print("\n🏆 Elite Leagues Covered:")
    leagues = [
        "Premier League", "La Liga", "Serie A", "Bundesliga",
        "Ligue 1", "Eredivisie", "Primeira Liga", "Super Lig",
        "Champions League", "FA Cup", "World Cup Qualifiers"
    ]
    
    for i, league in enumerate(leagues, 1):
        print(f"   {i:2d}. {league}")
    
    print("\n🤖 Agent Synergy Settings:")
    print(f"   Agent Synergy: ENABLED")
    print(f"   Min Accuracy Threshold: 60%")
    print(f"   Fusion Threshold: 65%")
    print(f"   Performance Lookback: 30 days")

def demo_autonomous_workflow():
    """Demonstrate the autonomous workflow"""
    print_section("AUTONOMOUS WORKFLOW")
    
    print("\n🔄 Continuous Alpha Hunting Loop:\n")
    
    phases = [
        ("🧠 Reasoner Phase", "Build execution plan using LLM reasoning"),
        ("🛠️ Coder Phase", "Generate Python strategy implementation"),
        ("🤖 Agent Validation", "Test and improve individual agents"),
        ("🎯 Strategy Enforcement", "Validate bet generation targets"),
        ("📊 Performance Testing", "Run paper trading simulations"),
        ("🔄 Agent Learning", "Update weights based on accuracy"),
        ("🏆 Champion Promotion", "Identify top-performing strategies")
    ]
    
    for i, (phase, description) in enumerate(phases, 1):
        print(f"   {i}. {phase}")
        print(f"      {description}")
        print()

def main():
    """Run the demo"""
    print("\n" + "=" * 80)
    print("  🏈 AUTONOMOUS FOOTBALL BETTING SYSTEM - DEMO")
    print("=" * 80)
    print("\n  This demo showcases the merged capabilities from MAIN and AGENTSADD")
    print("  without requiring API keys or running the full autonomous system.\n")
    
    # Demo 1: System configuration
    demo_system_config()
    
    # Demo 2: Agent predictions
    predictions = demo_agent_predictions()
    
    # Demo 3: Agent fusion
    demo_agent_fusion(predictions)
    
    # Demo 4: Autonomous workflow
    demo_autonomous_workflow()
    
    print("\n" + "=" * 80)
    print("  ✅ DEMO COMPLETE")
    print("=" * 80)
    print("\n  To run the full system with real API integration:")
    print("     1. Set environment variables: FOOTBALL_API_KEY, DEEPSEEK_API_KEY")
    print("     2. Install dependencies: pip install -r requirements.txt")
    print("     3. Run: python football_betting_system.py")
    print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    main()
