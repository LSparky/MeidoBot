import discord
from discord.ext import commands
import random

class magic8ball:
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx, *args):
        question = ("{} " * len(args)).format(*args)

        answers = random.randint(1, 20)

        if question == "":
            await ctx.send("Please enter a question");
            return

        elif answers == 1:
            embedtext = "It is certain"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 2:
            embedtext = "It is decidedly so"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 3:
            embedtext = "Without a doubt"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 4:
            embedtext = "Yes - definitely"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 5:
            embedtext = "You may rely on it"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 6:
            embedtext = "As I see it, yes"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 7:
            embedtext = "Most likely"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 8:
            embedtext = "Outlook good"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 9:
            embedtext = "Yes"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 10:
            embedtext = "Signs point to yes"
            embedlink = "https://i.imgur.com/hEOQ5JY.png"

        elif answers == 11:
            embedtext = "Reply hazy, try again"
            embedlink = "https://i.imgur.com/VtFhNuf.png"

        elif answers == 12:
            embedtext = "Ask again later"
            embedlink = "https://i.imgur.com/VtFhNuf.png"

        elif answers == 13:
            embedtext = "Better not tell you now"
            embedlink = "https://i.imgur.com/VtFhNuf.png"

        elif answers == 14:
            embedtext = "Cannot predict now"
            embedlink = "https://i.imgur.com/VtFhNuf.png"

        elif answers == 15:
            embedtext = "Concentrate and ask again"
            embedlink = "https://i.imgur.com/VtFhNuf.png"

        elif answers == 16:
            embedtext = "Don't count on it"
            embedlink = "https://i.imgur.com/LpHdcpM.png"

        elif answers == 17:
            embedtext = "My reply is no"
            embedlink = "https://i.imgur.com/LpHdcpM.png"

        elif answers == 18:
            embedtext = "My sources say no"
            embedlink = "https://i.imgur.com/LpHdcpM.png"

        elif answers == 19:
            embedtext = "Outlook not so good"
            embedlink = "https://i.imgur.com/LpHdcpM.png"

        elif answers == 20:
            embedtext = "Very doubtful"
            embedlink = "https://i.imgur.com/LpHdcpM.png"

        embed = discord.Embed(colour=discord.Colour(0xff0000))

        embed.set_thumbnail(url=embedlink)
        embed.set_author(name="8Ball", icon_url="https://i.imgur.com/0vLmxUP.png")
        embed.set_footer(text="Requested by: {0}".format(ctx.message.author),
                         icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="```Answer:```", value="```{0}```".format(embedtext))

        await ctx.send(embed=embed)




def setup(client):
	client.add_cog(magic8ball(client))
