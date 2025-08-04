# Pumpfun Sniper Bot (v8.9-stable)

## Quick Start

### 1. Clone or Download
If using Git:
cd C:\Users\bidne\Downloads
git clone https://github.com/adakotah18/pumpfun-sniper-bot.git
cd pumpfun-sniper-bot

Or manually upload files into this repo.

---

### 2. Configure .env
- Open `.env` and paste your **Phantom private key**
- Ensure `DRY_RUN=False` for live trades

---

### 3. Install Dependencies
pip install -r requirements.txt

---

### 4. Run Bot
python main.py

Bot will respond:
LIVE MODE ENABLED — real trades will execute
Bot is now listening for commands via Telegram...

---

### 5. Test Telegram Commands
Use:
/status
/buy 0.1
/sell 0.1

---

## Folder Structure

pumpfun-sniper-bot/
│── main.py
│── .env
│── requirements.txt
│── trades.log
│── README.md
│── dashboard/
    │── package.json
    │── pages/
    │   └── index.js

---

## Dashboard (PnL Graph + Wallet Rotation)

### Install and Run Dashboard
cd dashboard
npm install
npm run dev

Open browser at:  
http://localhost:3000

---

## Next Steps
- Phase 9 → Real-time PnL Graph + Telegram Alerts
- Phase 10 → Whale Tracking + Influencer Scoring
