from dotenv import load_dotenv
import os
import time
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables
load_dotenv()

# Config
DRY_RUN = os.getenv("DRY_RUN", "False").lower() == "true"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SOL_PRIVATE_KEY = os.getenv("SOL_PRIVATE_KEY")
SOL_BALANCE = float(os.getenv("SOL_BALANCE", "0"))

# Basic Bot Status
status_msg = "LIVE MODE ENABLED — real trades will execute" if not DRY_RUN else "DRY RUN MODE ENABLED — safe mode"

print(status_msg)
print("Bot is now listening for commands via Telegram...")

# Telegram Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sniper bot active. Use /buy, /sell, /status, /rotate, /kill, /resume.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Bot Status: {status_msg}\nBalance: {SOL_BALANCE} SOL")

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    amount = context.args[0] if context.args else "0.1"
    await update.message.reply_text(f"[BUY] Executing trade for {amount} SOL (pump.fun)...")
    # Placeholder: call pump.fun API here

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    amount = context.args[0] if context.args else "ALL"
    await update.message.reply_text(f"[SELL] Executing sell for {amount} SOL...")
    # Placeholder: call pump.fun API here

# Initialize Telegram bot
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("sell", sell))

# Run the bot
if __name__ == "__main__":
    app.run_polling()
