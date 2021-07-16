from discord.ext.commands import Cog, command, has_permissions, bot_has_permissions
from typing import Optional
from time import time

class Commands(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="ping")
  async def ping(self, ctx):
    start = time()
    message = await ctx.send(f"Pong :ping_pong:! **{self.bot.latency*100:,.0f} ms**")
    end = time()

    await message.edit(content=f"Pong :ping_pong:! **Latency: {self.bot.latency*100:,.0f} ms** | **Response Time {(end-start)*1000:,.0f} ms**")

  @command(aliases=["massclear", "clear"])
  @bot_has_permissions(manage_messages=True)
  @has_permissions(manage_messages=True)
  async def purge(self, ctx, limit: Optional[int] = 10):
    def _check(message):
      if message.pinned:
        return False

      return True

    with ctx.channel.typing():
      await ctx.message.delete()
      deleted = await ctx.channel.purge(limit=limit, check=_check)

      await ctx.send(f"Deleted {len(deleted):,} messages.", delete_after=5)

  @Cog.listener()
  async def on_ready(self):
    print(f"Commands cog ready")

def setup(bot):
  bot.add_cog(Commands(bot))