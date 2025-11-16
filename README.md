# 🏈 Autonomous Football Betting System

An advanced autonomous football betting system that combines LLM-powered strategy generation with multi-agent intelligence for optimal betting decisions.

## 🌟 Features

### Core Capabilities (from MAIN)
- **DeepSeek LLM Integration**: Autonomous code generation and strategy development
- **Football Data Engine**: Real-time data from Football-API
- **Continuous Alpha Hunting**: 24/7 autonomous operation finding profitable betting strategies
- **Strategy Validation**: Automated testing and enforcement of performance targets
- **Champion Tracking**: Promotes and monitors top-performing strategies

### Agent Synergy System (from AGENTSADD)
- **Multi-Agent Intelligence**: Specialized agents for different analysis aspects
  - Form Analyzer: Team performance trends
  - Injury Intelligence: Player availability impact
  - H2H Specialist: Historical matchup analysis
  - Odds Value Hunter: Bookmaker discrepancy detection
- **Performance Tracking**: Continuous monitoring of agent accuracy
- **Weighted Fusion**: Intelligent combination of agent predictions
- **Adaptive Learning**: Automatic weight adjustment based on performance

## 🎯 Performance Targets

- **Win Rate**: 71%
- **ROI**: 26%
- **Daily Bets**: 17+
- **League Coverage**: 8+ top leagues
- **Bet Types**: Singles, accumulators, BTTS, over/under, double chance, value bets

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
```

### Installation
```bash
# Clone the repository
git clone https://github.com/TGT2025/FOOTYAI.git
cd FOOTYAI

# Install dependencies
pip install -r requirements.txt
```

### Configuration
Set environment variables for API keys:
```bash
export FOOTBALL_API_KEY="your_football_api_key"
export DEEPSEEK_API_KEY="your_deepseek_api_key"
```

Or create a `.env` file:
```
FOOTBALL_API_KEY=your_football_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
```

### Running the System
```bash
python football_betting_system.py
```

## 📊 System Architecture

```
Autonomous Football Betting System
│
├── LLM Client (DeepSeek)
│   ├── Strategy Generation
│   ├── Code Synthesis
│   └── Plan Reasoning
│
├── Football Data Engine
│   ├── Live Fixtures
│   ├── Historical Matches
│   ├── Team Statistics
│   └── Odds Data
│
├── Agent Synergy System
│   ├── Form Analyzer
│   ├── Injury Intelligence
│   ├── H2H Specialist
│   └── Odds Value Hunter
│
├── Performance Tracking
│   ├── Agent Accuracy
│   ├── Weight Updates
│   └── Fusion Engine
│
└── Alpha Hunting Loop
    ├── Reasoner Phase
    ├── Coder Phase
    ├── Validation Phase
    ├── Testing Phase
    └── Champion Promotion
```

## 🔄 Continuous Operation Flow

1. **Reasoner Phase**: LLM generates execution plan with strategy requirements
2. **Coder Phase**: Synthesizes Python code for betting strategies
3. **Agent Validation**: Tests and improves individual agents
4. **Strategy Enforcement**: Validates bet generation and performance targets
5. **Performance Testing**: Runs simulations and paper trading
6. **Agent Learning**: Updates weights based on prediction accuracy
7. **Champion Promotion**: Identifies and promotes top strategies

## 🤖 Agent System

The system uses specialized agents that work together through weighted fusion:

- **Form Analyzer** (weight: 0.7): Analyzes recent team performance, momentum, scoring patterns
- **Injury Intelligence** (weight: 0.8): Tracks player availability and lineup strength
- **H2H Specialist** (weight: 0.6): Studies historical head-to-head matchups
- **Odds Value Hunter** (weight: 0.9): Identifies value in bookmaker odds

Agents are continuously evaluated and their weights adjusted based on prediction accuracy.

## 📁 Project Structure

```
FOOTYAI/
├── football_betting_system.py  # Main unified system
├── MAIN                         # Original monolith (4000+ lines)
├── AGENTSADD                    # Agent synergy enhancements
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── logs/                        # System logs
└── iterations/                  # Generated strategy iterations
```

## 🔧 Configuration

Edit the `Config` class in `football_betting_system.py`:

```python
class Config:
    # Elite performance targets
    ELITE_TARGETS = {
        "min_win_rate": 0.71,
        "min_profit_margin": 0.26,
        "max_stake_per_bet": 0.1,
        "daily_bet_target": 17,
        "multi_league_coverage": 8,
    }
    
    # Agent settings
    AGENT_SYNERGY_ENABLED = True
    FUSION_THRESHOLD = 0.65
```

## 📝 Logging

Logs are automatically created in the `logs/` directory with detailed information about:
- System initialization
- Iteration progress
- Agent performance
- Strategy generation
- Error tracking

## ⚠️ Disclaimer

This system is for educational and research purposes only. Always bet responsibly and within your means. Past performance does not guarantee future results.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - See LICENSE file for details

## 🔗 API Sources

- Football Data: [API-Football](https://www.api-football.com/)
- LLM: [DeepSeek](https://www.deepseek.com/)

## 🎓 Key Learnings Merged

### From MAIN:
- Robust LLM integration with retry logic
- Comprehensive logging infrastructure
- Continuous alpha hunting architecture
- Strategy validation and enforcement
- Champion tracking system

### From AGENTSADD:
- Multi-agent performance tracking
- Weighted fusion algorithm
- Adaptive learning mechanisms
- Agent validation and improvement
- Enhanced orchestration strategies

## 🚀 Future Enhancements

- [ ] Real-time betting execution
- [ ] Advanced bankroll management
- [ ] Multi-model LLM ensemble
- [ ] Enhanced agent specialization
- [ ] Live data streaming
- [ ] Web dashboard interface
- [ ] Backtesting framework
- [ ] Risk management tools
