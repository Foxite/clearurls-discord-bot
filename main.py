import os
import re
import discord
from discord import Intents
from dotenv import load_dotenv
from unalix import clear_url

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == client.user:
            return

        # Extract links and clean
        cleaned = ""
        any_cleaned = False
        last_match = None
        for match in re.finditer('(?P<url>https?://[^\s]+)', message.content):
            if last_match is None:
                cleaned += message.content[0:match.start()]
            else:
                cleaned += message.content[last_match.end():match.start()]

            last_match = match

            url = message.content[match.start():match.end()]
            cleaned_url = clear_url(url)
            if cleaned_url != url:
                cleaned += cleaned_url
                any_cleaned = True
            else:
                cleaned += url

        if last_match is not None:
            cleaned += message.content[last_match.end():]

        # Send message and add reactions
        if any_cleaned:
            #text = 'It appears that you have sent one or more links with tracking parameters. Below are the same links with those fields removed:\n' + '\n'.join(cleaned)
            await message.reply(cleaned, mention_author=False)
            await message.delete()

load_dotenv()
intents = Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.environ['TOKEN'])
