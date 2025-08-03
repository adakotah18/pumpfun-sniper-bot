from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read DRY_RUN mode
DRY_RUN = os.getenv("DRY_RUN", "True").lower() == "true"

if DRY_RUN:
    print("DRY_RUN MODE ENABLED — safe test mode")
else:
    print("LIVE MODE ENABLED — real trades will execute")

# TODO: Add trading logic (Ichimoku, scaling, Telegram alerts, kill switch)

