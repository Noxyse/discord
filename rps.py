import random
from discord.ext import commands

def setup(bot):
    @bot.command()
    async def rps(ctx, guess: str):
        # Normalize the user input to lowercase
        guess = guess.lower()

        # Mapping of abbreviations to full words
        abbreviations = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        options = ['rock', 'paper', 'scissors']

        # Convert abbreviations to full words
        if guess in abbreviations:
            guess = abbreviations[guess]
        elif guess not in options:
            await ctx.send('Invalid input. Please choose "Rock", "Paper", "Scissors" or "r", "p", "s".')
            return
        
        # Choose a random option from the list
        random_guess = random.choice(options)

        # Determine the outcome of the game
        if guess == random_guess:
            await ctx.send(f'Hmpf. I hate draws. We both chose {random_guess.capitalize()}.')
        elif (guess == 'rock' and random_guess == 'scissors') or \
             (guess == 'paper' and random_guess == 'rock') or \
             (guess == 'scissors' and random_guess == 'paper'):
            await ctx.send(f'Whatever. You win. You chose {guess.capitalize()} and I chose {random_guess.capitalize()}. I want a rematch!')
        else:
            await ctx.send(f'Ha. Loser. My awesome {random_guess.capitalize()} beat the crap out of your {guess.capitalize()}!')