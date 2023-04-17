import os
import logging
import discord
import re

from diceroller import roller

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(guild.name)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello {message.author}!')

    elif dice_roll := re.search("!([0-9]+)D([0-9]+)", message.content):
        await message.channel.send(f'Oh, you want to play a game ?')
        number_of_dices = int(dice_roll.group(1))
        dice_faces = int(dice_roll.group(2))

        if number_of_dices > 20:
            await message.channel.send(f"Nope… I will not throw more than 20 dices!")
            number_of_dices = 20

        if dice_faces > 100:
            await message.channel.send(f"Why do you need more than 100 sided dices ?\nNope, I'll not throw those!")
            return

        results = roller.roll_dice(number_of_dices, dice_faces)

        await message.channel.send(f'Ok, rolling {number_of_dices} dices… Got {results} for a total of {sum(results)}')


client.run(TOKEN)