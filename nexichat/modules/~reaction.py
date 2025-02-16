from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

EMOJIS = ["🥰", "❤️", "😁", "💋", "😱", "🤣", "😘", "❤️‍🔥", "👌", "🫡", "😍"]

@nexichat.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        react = random.choice(EMOJIS)
        await message.react(react)
    except Exception as e:
        print(f"Failed to react to message: {e}")
