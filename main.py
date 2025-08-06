import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os

# ---------------------------
# CONFIGURATION
# ---------------------------
BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = int(os.environ['CHANNEL_ID'])  # stored as string, convert to int
MESSAGE_DAY = 27  # e.g., 27th of every month
MESSAGE_HOUR = 19  # 7 PM UTC
MESSAGE_MINUTE = 0
MESSAGE_TEXT = "Hey! the lords demandeth from us once more. (friendly rent reminder) Stay weird. 🔮"
# ---------------------------

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
scheduler = AsyncIOScheduler()

# Define the scheduled task
async def send_monthly_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(MESSAGE_TEXT)
    else:
        print("⚠️ Could not find channel.")

# Schedule the task BEFORE the bot starts
scheduler.add_job(send_monthly_message, 'cron',
                  day=MESSAGE_DAY, hour=MESSAGE_HOUR, minute=MESSAGE_MINUTE)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("👋 Bot is now online and ready!")
    scheduler.start()

# Run the bot
bot.run(BOT_TOKEN)
