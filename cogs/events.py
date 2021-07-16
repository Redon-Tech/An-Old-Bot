from discord.ext.commands import Cog, command
from discord import Embed, Colour
from time import time

class Events(Cog):
  def __init__(self, bot):
    self.bot = bot

  @Cog.listener()
  async def on_member_join(self, member):
    embed = Embed(
      title = "New Member",
      description = f"{member.mention} | {member.name}#{member.discriminator}\nHas joined the server please give them there roles",
      colour = Colour.green()
    )
    await self.bot.get_channel(852268960975945778).send("<@&852260161534820423>", embed=embed)

    await member.add_roles(*(member.guild.get_role(id_) for id_ in (852274222297382952,)))

  @Cog.listener()
  async def on_ready(self):
    print(f"Events cog ready")

def setup(bot):
  bot.add_cog(Events(bot))