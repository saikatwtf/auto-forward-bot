import uvloop
from pyrogram import Client, filters
from decouple import config

print("Starting...")

# Install uvloop for faster event loops
uvloop.install()

# Read configurations from environment variables
session_string = config("SESSION")  # Session string
api_id = config("APP_ID", cast=int)  # API ID
api_hash = config("API_HASH")  # API Hash
source_channel = config("SOURCE_CHANNEL")  # Source channel username or ID
destination_bot_username = config("TO_BOT_USERNAME")  # Destination bot username

# Create Pyrogram Client using session string
app = Client(session_string, api_id=api_id, api_hash=api_hash)

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
