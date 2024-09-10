import uvloop
import asyncio
from pyrogram import Client, filters
from decouple import config

print("Starting...")

uvloop.install()

# Replace with your session string, API ID, and API Hash
session_string = config("SESSION")
api_id = config("APP_ID", default=None, cast=int)
api_hash = config("API_HASH", default=None)
# Replace with your source channel username or ID
source_channel = config("SOURCE_CHANNEL")

# Replace with your bot's username (the bot must be added to your chat list)
destination_bot_username = config("TO_BOT_USERNAME")

# Create Pyrogram Client using session string
app = Client(api_id=APP_ID, api_hash=API_HASH, session_string=SESSION)

# Function to forward messages from the source channel to the bot
@app.on_message(filters.chat(source_channel))
async def forward_messages(client, message):
    try:
        # Forward the message to the bot
        await message.forward(destination_bot_username)
        print(f"Message forwarded: {message.message_id}")
    except Exception as e:
        print(f"Failed to forward message {message.message_id}: {e}")

# Run the client
app.run()
