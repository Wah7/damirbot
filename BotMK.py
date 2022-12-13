import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
import random
from random import randint

client = commands.Bot(command_prefix="mk") 
token = ("token_here")
invite = ("invite_here")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="(mkhelp) DamieMK is a god"))
    print ("Bot is ready")

client.remove_command("help")

#HELP COMMANDS

@client.command()
async def help(ctx):
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name="Command List")
        embed.add_field(name="`mknuke`", value="- does a totally real nuke on the server")
        embed.add_field(name="`mkamogus`", value="- sussy baka")
        embed.add_field(name="`mkserverinfo`", value="- shows server stats")
        embed.add_field(name="`mkmembercount`", value="- tells you how many members this discord has")
        embed.add_field(name="`mkfreeadmin`", value="- gives you admin")
        embed.add_field(name="`mkinvite`", value="- gives invite link if you want to invite this bot to your own server")
        embed.add_field(name="`mkhelpadmin`", value="- shows admin commands")
        embed.add_field(name="`mkhelpantishit`", value="- shows commands for preventing nukes, raids, and spam")
        embed.add_field(name="`mkeightball`", value="- tells ur fortune or somethijng idk")
        embed.add_field(name="`mkinfo`", value="- shows info about this bot")
        embed.set_image(url="")
        await ctx.send(embed=embed)


@client.command()
async def helpadmin(ctx):
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name="Admin Commands")
        embed.add_field(name="`mkban`", value="- bans a member for you")
        embed.add_field(name="`mkunbanban`", value="- unbans a member for you")
        embed.add_field(name="`mkkick`", value="- kicks a member for you")
        embed.add_field(name="`mkrenameall`", value="- renames everyone in the server to whatever you choose")
        embed.set_image(url="")
        await ctx.send(embed=embed)

@client.command()
async def helpantishit(ctx):
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name="Anti-Shit is currently disabled/is a work in progress")
        await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  memberCount = str(ctx.guild.member_count)
  role_count = len(ctx.guild.roles)
   
  embed = discord.Embed(
      title=name + " Server Info",
      timestamp=ctx.message.created_at,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=ctx.guild.icon_url)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)
  embed.add_field(name='Number of roles', value=str(role_count), inline=True)

  await ctx.send(embed=embed)

@client.command()
async def membercount(ctx):
  memberCount = str(ctx.guild.member_count)
  embed = discord.Embed(
      title="Member Count",
      description=memberCount+" Members",
      timestamp=ctx.message.created_at,
      color=discord.Color.red()
  )
  await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
  embed = discord.Embed(
      title="Bot Invite Link",
      description=invite,
      timestamp=ctx.message.created_at,
      color=discord.Color.red()
  )
  await ctx.send(embed=embed)

@client.command()
async def freeadmin(ctx):
    await ctx.send("https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif")

@client.command()
async def eightball(ctx, question):
  answer = randint(1, 20)
  if answer == 1:
    await ctx.send("It is certain")
  if answer == 2:
    await ctx.send("Without a doubt")
  if answer == 3:
    await ctx.send("You may rely on it")
  if answer == 4:
    await ctx.send("Yes definitely")
  if answer == 5:
    await ctx.send("It is decidedly so")
  if answer == 6:
    await ctx.send("As I see it, yes")
  if answer == 7:
    await ctx.send("Most likely")
  if answer == 8:
    await ctx.send("Yes")
  if answer == 9:
    await ctx.send("Outlook good")
  if answer == 10:
    await ctx.send("Signs point to yes")
  if answer == 11:
    await ctx.send("Reply hazy try again")
  if answer == 12:
    await ctx.send("Better not tell you now")
  if answer == 13:
    await ctx.send("Ask again later")
  if answer == 14:
    await ctx.send("Cannot predict now")
  if answer == 15:
    await ctx.send("Concentrate and ask again")
  if answer == 16:
    await ctx.send("Dont count on it")
  if answer == 17:
    await ctx.send("Outlook not so good")
  if answer == 18:
    await ctx.send("My sources say no")
  if answer == 19:
    await ctx.send("Very doubtful")
  if answer == 20:
    await ctx.send("My reply is no")

@client.command()
async def nuke(ctx):
    await ctx.send("`Preparing the nuke...`")
    await ctx.send("`Deleting all emojis...`")
    await ctx.send("`Removing all roles...`")
    await ctx.send("`Deleting channels...`")
    await ctx.send("`Giving everyone role admin perms...`")
    await ctx.send("`Deleting the server...`")
    await ctx.send("_The totally real and powerful nuke has been completed_")

@client.command()
async def amogus(ctx):
    await ctx.send("_A M O G U S_ \nhttps://cdn.discordapp.com/attachments/804437210299760682/817524893351411743/video0.mp4")
    
@client.command()
async def info(ctx):
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name="BOT INFO")
        embed.add_field(value="CREATED BY DamieMK#6767")
        await ctx.send(embed=embed)
        
# ADMIN COMMANDS    
    
@client.command()
@commands.has_permissions(administrator=True)
async def renameall(ctx, *, nick):
    for member in ctx.guild.members:
            
        try:
            await member.edit(nick=nick)
        except discord.Forbidden:
            print(f"{member.name} has NOT been renamed to {nick} in {ctx.guild.name}")
        else:
            print(f"{member.name} has been renamed to {nick} in {ctx.guild.name}")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{discord.member} Has been banned for {reason}")

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{member_name} has been unbanned")
            return

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{discord.Member} has been kicked for {reason}")

@client.event
async def on_command_error(ctx, error):
    print(f"{ctx.guild.name}:  {error}")
    if isinstance(error, commands.CommandError):
        await ctx.send(f">>> **you did the command wrong dumbass** \n{error}")
        
    
client.run(token)