import uvloop
import asyncio
from pyrogram import Client, filters
from decouple import config
print("Starting...")
# Install uvloop for faster event loops
uvloop.install()

# Read configurations from environment variables
SESSION = config("SESSION")  # Session string
api_id = config("APP_ID", cast=int)  # API ID
api_hash = config("API_HASH")  # API Hash
source_channel = config("SOURCE_CHANNEL")  # Source channel username or ID
TO_BOT_USERNAME = config("TO_BOT_USERNAME")  # Destination bot username

# Create Pyrogram Client using StringSession
app = Client(name=SESSION, session_string=SESSION, api_id=api_id, api_hash=api_hash)
async def start_bot():
    await app.start()
    user = await app.get_me()
    print(f"Logged in as : {user.first_name}")

    await asyncio.Event().wait()

# Function to forward messages from the source channel to the bot
@app.on_message(filters.chat(source_channel))
async def forward_messages(client, message):
    try:
        # Forward the message to the bot
        await message.forward(TO_BOT_USERNAME)
        print(f"Message forwarded: {message.message_id}")
    except Exception as e:
        print(f"Failed to forward message {message.message_id}: {e}")

# Run the client
app.run(start_bot())
