def setup(bot):
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        if message.content.startswith(('hello ', 'hi')):
            await message.channel.send('Hello there!')

#auto-deletion of words
        if 'fuck' in message.content.lower():
            await message.delete()

            warn_command = bot.get_command('warn')
            if warn_command:
                reason = 'Usage of banned word'

                ctx = await bot.get_context(message)

                await warn_command(ctx, user=message.author, reason=reason)

        await bot.process_commands(message)