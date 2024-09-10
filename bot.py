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
destination_bot_username = config("TO_BOT_USERNAME")  # Destination bot username

# Create Pyrogram Client using StringSession
app = Client(name=SESSION, api_id=APP_ID, api_hash=API_HASH, session_string=SESSION)
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

async def start_bot():
    await app.start()
    user = await app.get_me()
    print(f"Logged in as : {user.first_name}")

    await asyncio.Event().wait()
# Function to forward messages from the source channel to the bot
@app.on_message(filters.chat(source_channel))
async def forward_messages(client: Client, message: Message):
    try:
        # Forward the message to the bot
        await message.forward(destination_bot_username)
        print(f"Message forwarded: {message.message_id}")
    except Exception as e:
        print(f"Failed to forward message {message.message_id}: {e}")

# Run the client
app.run(start_bot())
