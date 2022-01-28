import discord

bot = discord.Bot()

#write code here
@bot.slash_command(guild_ids=[...])
async def ping(ctx):
    await ctx.respond('pong')

bot.run('OTMyNDM3MjE1NTQ2NjA1NTk5.YeS91A.DxG_doFZkL9IxKKmCtacFjhOMig')