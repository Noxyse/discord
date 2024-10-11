import random
from discord.ext import commands

def setup(bot):
    bot.games = {}  # Initialize the games dictionary

    @bot.command()
    async def startgame(ctx):
        """Start a new guessing game."""
        bot.games[ctx.channel.id] = random.randint(1, 100)
        await ctx.send('The guessing game is starting! Guess the number between 1 and 100!')

    @bot.event
    async def on_message(message):
        """Handle messages for the guessing game."""
        # Prevent the bot from responding to its own messages
        if message.author == bot.user:
            return

        # Debugging print statements
        print(f"Received message: {message.content} in channel: {message.channel.id}")

        # Check if there is an active game in the channel
        if message.channel.id in bot.games:
            try:
                number = int(message.content)  # Try to convert the message content to an integer
                random_number = bot.games[message.channel.id]

                # Debugging print statements
                print(f"Guess received: {number}, Random number: {random_number}")

                if number > random_number:
                    await message.channel.send('Too big!')
                elif number < random_number:
                    await message.channel.send('Too small!')
                else:
                    await message.channel.send(f'Ding ding ding! You found the correct number: {random_number}!')
                    del bot.games[message.channel.id]  # End the game
            except ValueError:
                # If the message is not a number, notify the user
                await message.channel.send('Enter a valid positive number.')

        # Process commands after handling messages
        await bot.process_commands(message)
