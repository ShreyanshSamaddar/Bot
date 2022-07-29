import discord
import asyncio
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title="**Wrong Command Triggered**",
                              description='''Type .help to get more info about Blekan Bot''', colour=0xe74c3c)
        mymessage = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await mymessage.delete()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        if amount <= 0:
            embed = discord.Embed(title="**Command triggered Insufficient/Wrong Data**", description='''Please specify the number of messages to be purged
    **Example**: .purge 10''', colour=0x3498db)
            mymessage = await ctx.send(embed=embed)
            await asyncio.sleep(4)
            await mymessage.delete()
        elif amount > 0:
            await ctx.channel.purge(limit=amount+1)
            await asyncio.sleep(0.2)
            temp = str(amount)
            temp2 = 'Purged '+temp+' Messages'
            embed = discord.Embed(title=temp2, colour=0xe74c3c)
            mymessage = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await mymessage.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=''):
        if member == None or member == ctx.author:
            await ctx.send('Mention a user')
        else:
            message = discord.Embed(
                description=f"You have been banned from {ctx.guild.name} \nReason: {reason}")
            await member.send(embed=message)
            await ctx.guild.ban(member, reason=reason)
            embed = discord.Embed(
                description=f"{member.mention} has been banned! \nReason: {reason}")
            await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason='Not Specified'):
        if member == None or member == ctx.author:
            await ctx.send('Mention a user')
        else:
            message = discord.Embed(
                description=f"You have been kicked from {ctx.guild.name} \nReason: {reason}")
            await member.send(embed=message)
            await ctx.guild.kick(member, reason=reason)
            embed = discord.Embed(
                description=f"{member.mention} has been kicked! \nReason: {reason}")
            await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason='Not Specified'):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(
            title="Muted", description=f"{member.mention} was muted ")
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        message = discord.Embed(
            description=f"You have been muted in {ctx.guild.name} \nReason: {reason}")
        await member.send(embed=message)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId: discord.User):
        await ctx.guild.unban(userId)
        await ctx.send(f"{userId.mention} have been unbanned sucessfully")


"""    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        if amount <= 0:
            embed = discord.Embed(title="**Command triggered Insufficient/Wrong Data**", description='''Please specify the number of messages to be purged
    **Example**: .purge 10''', colour=0x3498db)
            mymessage = await ctx.send(embed=embed)
            await asyncio.sleep(4)
            await mymessage.delete()
        elif amount > 0:
            await ctx.channel.purge(limit=amount+1)
            await asyncio.sleep(0.2)
            temp = str(amount)
            temp2 = 'Purged '+temp+' Messages'
            embed = discord.Embed(title=temp2, colour=0xe74c3c)
            mymessage = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await mymessage.delete()"""


def setup(bot):
    bot.add_cog(Moderation(bot))
