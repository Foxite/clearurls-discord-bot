import os
import re
import discord
from discord import Intents
from dotenv import load_dotenv
from unalix import clear_url

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == client.user:
            permissions = message.channel.guild.me.permissions_in(message.channel)
            # Suppress embeds for bot messages to avoid visual clutter
            if permissions.manage_messages:
                await message.edit(suppress=True)
                # Add :wastebasket: emoji for easy deletion if necessary
                if permissions.add_reactions and permissions.read_message_history:
                    await message.add_reaction('🗑')

        # Extract links and clean
        urls = re.findall('(?P<url>https?://[^\s]+)', message.content)
        cleaned = []
        for url in urls:
            if clear_url(url) != url:
                cleaned.append(clear_url(url))

        # Send message and add reactions
        if cleaned:
            #text = 'It appears that you have sent one or more links with tracking parameters. Below are the same links with those fields removed:\n' + '\n'.join(cleaned)
            await message.reply(cleaned, mention_author=False)
            await message.delete()

load_dotenv()
intents = Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.environ['TOKEN'])
