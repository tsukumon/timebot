import discord

bot = discord.Bot()

#write code here
@bot.slash_command(guild_ids=[...])
async def ping(ctx):
    await ctx.respond('pong')

bot.run('#')
