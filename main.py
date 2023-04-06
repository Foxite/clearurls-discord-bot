import os
import re
import discord
from discord import Intents
from dotenv import load_dotenv
from unalix import clear_url

delete_emoji = os.environ['DELETE_EMOJI']

def clean_message(content):
    # Extract links and clean
    cleaned = ""
    any_cleaned = False
    last_match = None
    for match in re.finditer('(?P<url>https?://[^\s]+)', content):
        if last_match is None:
            cleaned += content[0:match.start()]
        else:
            cleaned += content[last_match.end():match.start()]

        last_match = match

        url = content[match.start():match.end()]
        cleaned_url = clear_url(url)
        if cleaned_url != url:
            cleaned += cleaned_url
            any_cleaned = True
        else:
            cleaned += url

    if last_match is not None:
        cleaned += content[last_match.end():]

    return any_cleaned, cleaned


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == client.user:
            return

        any_cleaned, cleaned = clean_message(message.content)

        # Send message and add reactions
        if any_cleaned:
            #text = 'It appears that you have sent one or more links with tracking parameters. Below are the same links with those fields removed:\n' + '\n'.join(cleaned)
            message_files = []
            for att in message.attachments:
                message_files.append(await att.to_file())

            await message.channel.send("Cleaned message by " + message.author.mention + ":\n" + cleaned, mention_author=False, files=message_files, reference=message.reference)
            await message.delete()

    async def on_reaction_add(self, reaction, user):
        if reaction.message.author == client.user and len(reaction.message.mentions) > 0 and reaction.message.mentions[0] == user and str(reaction.emoji) == delete_emoji:
            await reaction.message.delete()

if __name__ == "__main__":
    load_dotenv()
    intents = Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(os.environ['TOKEN'])
