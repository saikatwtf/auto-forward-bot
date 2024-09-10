import uvloop
import asyncio
from pyrogram import Client, filters
from decouple import config

print("Starting...")

# Install uvloop for faster event loops
uvloop.install()

# Replace with your session string, API ID, and API Hash
session_string = config("SESSION")
api_id = config("APP_ID", cast=int)
api_hash = config("API_HASH")

# Replace with your source channel username or ID
source_channel = config("SOURCE_CHANNEL")

# Replace with your bot's username (the bot must be added to your chat list)
destination_bot_username = config("TO_BOT_USERNAME")

# Create Pyrogram Client using session string
app = Client(session_name=session_string, api_id=api_id, api_hash=api_hash)

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
if __name__ == "__main__":
    app.run()
