import discord, random, string
from asyncio import sleep
from discord.ext import commands
import botlib.info as info
from discord import Game
from discord.utils import get
from colorama import init, Fore, Back, Style

init(autoreset=True)

client = discord.Client()

botToken = info.getBotId()
botToken = botToken[1]

firstname   = info.setUser("firstname")
lastname    = info.setUser("lastname")
fullname    = info.setUser("fullname")
discordTag  = info.setUser("discord")
easteregg   = 2

with open("penissize", "a"):
    pass
with open("penissize", "r") as init:
    global penisSize
    penisSize = init.read()
    if penisSize == "":
        penisSize = "1"
with open("penissize", "w") as init:
    init.write(penisSize)

async def id_generator(size=11, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

async def getUserFName(userId):
    pos = discordTag.index(str(userId))
    return firstname[pos]

async def getTag(fname):
    pos = fullname.index(str(fname))
    return discordTag[pos]
    
async def find_channel(guild):
    for c in guild.text_channels:
        if not c.permissions_for(guild.me).send_messages:
            continue
        return c
     
async def getPenis(save=True):
    with open("penissize", "r") as f:
        penisSize = f.read()
    penisLength = ""
    for length in range(int(penisSize)+1):
        penisLength+="="
    
    if save is True:
        penisSize = int(penisSize)
        penisSize+=1
        with open("penissize", "w") as save:
            save.write(str(penisSize))
    return penisLength
    
@client.event
async def on_ready():
    print(f"Logged in as:\t{Fore.MAGENTA}{Style.BRIGHT}{client.user}{Fore.RESET}.")
    await client.change_presence(activity=discord.Activity(name=f"you.", type=2))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    async def sendMessage(messagelist, istyping=True, channel=message.channel):
        print(f"{Style.BRIGHT}{Fore.GREEN}{message.author}{Style.RESET_ALL}:\t{message.content}")
        for messages in messagelist:
            if istyping == True:
                async with message.channel.typing():
                    await sleep(random.randint(2,5))
            await channel.send(messages)
            print(f"{Fore.MAGENTA}{Style.BRIGHT}{client.user}{Style.RESET_ALL}:\t{messages}")   


    if message.content == ('Solaf, hjälp!'):
        messagelist = [
                "Trim!",
                "Solaf, vad kollar du på?",
                "Solaf, har du sett klistermärkerna?",
                f"{easteregg} easteregg ;)"]
        await sendMessage(messagelist, istyping=False)

    if message.content == ('Solaf, har du sett klistermärkerna?'):    
        async with message.channel.typing():
            await sleep(9)
        await message.channel.send('Ja.')
        
    if message.content == ("+penis"):
        penis = await getPenis()
        messagelist = [f"8{(penis)}3"]
        await sendMessage(messagelist)
    
    if message.content == ('Solaf, vad kollar du på?'):
        id = await id_generator()
        messagelist = [f"https://youtube.com/watch?v={id}"]
        await sendMessage(messagelist)
    
    if str(message.author) != str(await getTag("Samuel Broman")) and message.content == "Solaf, Samuel skickade mig.":
        messagelist = [f"https://youtube.com/{random.randint(1,1000)}", "Berätta inte till Greta :|"]
        await sendMessage(messagelist)      

    if message.content == ('Solaf, tar det vanliga.') and str(message.author) == str(await getTag("Samuel Broman")):
        messagelist = [f"https://youtube.com/{random.randint(1,1000)}", "Berätta inte till Greta :|"]
        await sendMessage(messagelist)
        
    if str(message.author) != str(await getTag("Calle Engman")) and message.content == "Trim!":
        messagelist = ["Halal. :thumbsup:"]
        await sendMessage(messagelist)


@client.event
async def on_member_join(member):
    channel = await find_channel(member.guild)
    await channel.send(f"@everyone Welcom da cannibal: **{member}**.")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{member}{Style.RESET_ALL}\t{Fore.GREEN}joined{Style.RESET_ALL} the guild.")
    
@client.event
async def on_member_remove(member):
    channel = await find_channel(member.guild)
    await channel.send(f"@everyone Goodbye to the cannibal: **{member}**.")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{member}{Style.RESET_ALL}\t{Fore.RED}left{Style.RESET_ALL} the guild.")


client.run(botToken)
