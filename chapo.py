import discord
import random

def setup(bot):
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        if '^^' in message.content.lower():
            with open('responses.txt', 'r', encoding='utf-8') as file:
                responses = file.readlines()

            response = random.choice(responses).strip()

            await message.channel.send(response)