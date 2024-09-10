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
app = Client(name=SESSION, session_string=SESSION, api_id=api_id, api_hash=api_hash)

# Function to forward messages from the source channel to the bot
@app.on_message(filters.chat(source_channel))
async def forward_messages(client, message):
    for i in destination_bot_username:
        try:
            await client.copy_message(
                chat_id=i,
                from_chat_id=message.chat.id,
                message_id=message.id,
                caption=message.caption,
                caption_entities=message.caption_entities,
                reply_markup=message.reply_markup
            )
        except Exception as e:
            print(e)

BotzHubUser.run(start_bot())
