# PumpFun Sniper Bot — Phase 8

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Set up `.env` file (already pre‑configured for $117 SOL + Telegram)
3. Run bot: `python main.py`
4. Open dashboard: `python -m http.server 3000` inside `dashboard` folder

## Features (Phase 8)
- Live trading (Ichimoku strategy)
- Dynamic scaling with balance
- Telegram alerts + commands (`/status`, `/kill`, `/resume`)
- Kill switch + safety triggers
- Conservative default mode (aggressive toggle in dashboard)

## Next Phase
Phase 9 will add PnL graph + milestone tracker to the dashboard.
