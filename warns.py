import discord
from discord.ext import commands

warnings = {}

def setup(bot):
    @bot.command()
    async def warn(ctx, user: discord.User, *, reason: str):
        
        user_id = user.id

        if user_id in warnings:
            warnings[user_id] += 1
        else:
            warnings[user_id] = 1

        await ctx.send(f'{user.mention} received a warning. Reason: {reason}. Warning count: {warnings[user_id]}.')
        
        if warnings[user_id] == 3:
            await ctx.send(f'This is your third warning. Next time, you will get sanctionned.')

        #if warnings[user_id] > 3:
            #await ctx.send