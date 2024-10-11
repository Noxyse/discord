def setup(bot):
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        if message.content.startswith(('www.twitch.tv', 'https://www.twitch.tv')):
            await message.delete()

        await bot.process_commands(message)