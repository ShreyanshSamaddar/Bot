import discord
from datetime import datetime
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *,  member: discord.Member = None):
        if member == None:
            member = ctx.author
        userAvatarUrl = member.avatar_url
        embed = discord.Embed(title=f"{member.name}'s Avatar")
        embed.set_image(url=userAvatarUrl)
        await ctx.send(embed=embed)

    @commands.command()
    async def whois(self, ctx, target: discord.Member = None):
        if target == None:
            target = ctx.author
        if target.bot == True:
            temp = 'Bot'
        else:
            temp = 'Human'
        embed = discord.Embed(title='User Information',
                              colour=target.colour, timestamp=datetime.utcnow())
        embed.set_thumbnail(url=target.avatar_url)
        role_names = [role.name for role in target.roles]
        role_names.remove('@everyone')
        if len(role_names) == 0:
            temp2 = None
        else:
            temp2 = role_names
        fields = [("Name", str(target), True),
                  ("ID", target.id, True),
                  ("Human/Bot?", temp, True),
                  (f"Roles[{len(role_names)}]", temp2, False),
                  ("Created at", target.created_at.strftime(
                      "%d/%m/%Y %H:%M:%S"), True),
                  ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True)]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        embed = discord.Embed(title="Server information",
                              colour=0x3498db,
                              timestamp=datetime.utcnow())

        embed.set_thumbnail(url=ctx.guild.icon_url)

        fields = [("ID", ctx.guild.id, True),
                  ("Owner", ctx.guild.owner, True),
                  ("Created at", ctx.guild.created_at.strftime(
                      "%d/%m/%Y %H:%M:%S"), True),
                  ("Members", len(ctx.guild.members), True),
                  ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                  ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                  ("Banned members", len(await ctx.guild.bans()), True),
                  ("Text channels", len(ctx.guild.text_channels), True),
                  ("Voice channels", len(ctx.guild.voice_channels), True),
                  ("Categories", len(ctx.guild.categories), True),
                  ("Roles", len(ctx.guild.roles), True),
                  ("Invites", len(await ctx.guild.invites()), True), ]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
