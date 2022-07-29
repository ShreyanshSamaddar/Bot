import discord
import random
import asyncio
from discord.ext import commands


class Extra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title='**Invite Link**', colour=0x3498db)
        embed.add_field(name='If you wish to add me in your server:',
                        value='[Click here to add](https://discord.com/api/oauth2/authorize?client_id=1002535280336703559&permissions=8&scope=bot)', inline=False)
        embed.add_field(name='Support Server for Blekan :',
                        value='[Discord Server](https://discord.gg/jTYE3E7a)', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def random8balltest(self, ctx):
        responses = ['Heads', 'Tails']
        col = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f,
               0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a, 0x7289da, 0x99aab5]
        embed = discord.Embed(
            description=f'Tossing a coin \n Result: {random.choice(responses)}',
            color=random.choice(col))
        mym = await ctx.send(embed=embed)
        await asyncio.sleep(100)
        await mym.delete()


def setup(bot):
    bot.add_cog(Extra(bot))
