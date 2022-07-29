import discord
from discord.ext import commands


class Helping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
# Events
#  @commands.Cog.listener()


# Commands


    @commands.command()
    # help
    async def help(self, ctx, argument='', member: discord.Member = None):
        member = ctx.author
        if argument.lower() == 'utility':
            embed = discord.Embed(title="Utility Commands", description='''`-changeprefix [new prefix]`
Changes the prefix of Blekan for the server

`-whois [member mention/id]`
Gives information about the user

`-avatar (optional:Member)`
Get the avatar of yourself or another user.

`-serverinfo`
Gives information about the guild
''', color=0x109319)
            await ctx.send(embed=embed)
        elif argument.lower() == 'moderator':
            embed = discord.Embed(title="Moderator Commands", description='''`-ban [member] (optional:reason)`
Bans a member from the server.

`-kick [member] (optional reason)`
Kicks a member from the server.

`-mute [member] (optional:reason)`
Temporarily mutes a member in the server.

`-purge [amount]`
Deletes the amount of messages in the channel.
''', color=0x109319)
            await ctx.send(embed=embed)
        elif argument.lower() == 'music':
            # `join`, `play`, `pause`, `resume`, `repeat`, `download`, `queue`, `reset`,
            # `skip`, `song-info`, `volume`, `stop`, `leave`
            embed = discord.Embed(title="Music Commands(Delayed Music)", description='''`-join`
Joins the voice channel.

`-play [title/youtube url or playlist]`
Plays the song.

`-pause`
Pause the current song

`-resume`
Resumes the current song.

`-repeat`
Loops the current song.

`-download [title/youtube url or playlist]`
Downloads the song in mp3 format and sends in it discord.

`-queue`
Shows up the current queue.

`-reset`
Starts the song from beginning.

`-skip`
Skips the current song playing and plays the next soong in the queue if any.

`-song-info`
Gives info of the current song playing.

`-volume [integer]`
Adjust volume of Blekan. [Default=50]

`-stop`
Stops the current song playing.

`-leave`
Leaves the voice channel.''', color=0x109319)
            await ctx.send(embed=embed)
        elif argument.lower() == 'about':
            embed = discord.Embed(title="About Commands", description='''`-ping`
Tells you the current latency of Hormoni bot.

`-invite`
Gives a invite link for Blekan Bot.
''', color=0x109319)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Blekan Bot", description='''**All Blekan Commands Categories:**
You could type `-help <category>` for more info.''', color=0x109319)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/1002535280336703559/2216c80f56ce697cfa69d92729584cb5.webp?size=128")
            embed.add_field(name="1. :gear:Utility:",
                            value='''`whois`, `avatar`, `serverinfo`,`changeprefix`''', inline=True)

            embed.add_field(name="2. :tools:Moderator:",
                            value='''`ban`, `kick`, `mute`, `purge`''', inline=True)

            embed.add_field(name="3. :musical_note:Music(Delayed):",
                            value='''`join`, `play`, `pause`, `resume`, `repeat`, `download`, `queue`, `reset`, `skip`, `song-info`, `volume`, `stop`, `leave`''', inline=False)

            embed.add_field(name="4. :robot:About Bot",
                            value='''`ping`, `invite`''', inline=True)

            embed.add_field(
                name='**Extra Links**', value=' • [**Invite Link**](https://discord.com/api/oauth2/authorize?client_id=1002535280336703559&permissions=8&scope=bot)  •   [**Support Server**](https://discord.gg/jTYE3E7a)  ', inline=True)

            embed.set_footer(text=f'''Blekan Bot version-Beta 1.5. More features will be added in the upcoming version.
Requested by:{member}''', icon_url=member.avatar_url)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Helping(bot))
