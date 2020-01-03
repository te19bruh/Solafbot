import discord, random, string
from time import sleep
import botlib.info as info

botid = info.getBotId()
botid = botid[1]

firstname   = info.setUser("firstname")
lastname    = info.setUser("lastname")
discordTag  = info.setUser("discord")

def id_generator(size=11, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class MyClient(discord.Client):
    
    with open("penislength", "a") as init:
        pass
    with open("penislength", "r") as init:
        penis = init.read()
        if penis == "":
            penis = "="
    
    easteregg=2
    
    async def on_ready(self):
        print(f"\nLogged on as {self.user}\n")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        async def sendMessage(messagelist, istyping=True):
            print(f"{message.author}:\t{message.content}")
            for messages in messagelist:
                if istyping == True:
                    async with message.channel.typing():
                        sleep(random.randint(1,5))
                await message.channel.send(messages)
                print(f"{self.user}:\t{messages}")

        if message.content == ('Solaf, hjälp!'):
            messagelist = [
                    "Trim!",
                    "Solad, vad kollar du på?",
                    "Solaf, har du sett klistermärkerna?",
                    f"{self.easteregg} easteregg ;)"
                    ]
            await sendMessage(messagelist, istyping=False)

        if message.content == ('Solaf, har du sett klistermärkerna?'):    
                async with message.channel.typing():
                    sleep(9)
                await message.channel.send('Ja.')

        if message.content == ('Solaf, vad kollar du på?'):
            messagelist = [f"https://youtube.com/watch?v={id_generator()}"]
            await sendMessage(messagelist)

        if str(message.author) != discordTag[1] and message.content == "Solaf, Samuel skickade mig.":
            messagelist = [f"https://youtube.com/{random.randint(1,1000)}", "Berätta inte till Greta :|"]
            await sendMessage(messagelist)
        
        if message.content == ('Solaf, tar det vanliga.') and str(message.author) == discordTag[1]:
            messagelist = [f"https://youtube.com/{random.randint(1,1000)}", "Berätta inte till Greta :|"]
            await sendMessage(messagelist)

        if str(message.author) != discordTag[4] and message.content == "Trim!":
            messagelist = ["Halal. :thumbsup:"]
            await sendMessage(messagelist)

        if message.content == ('+penis'):
            messagelist = [f"8{self.penis}3"]
            await sendMessage(messagelist)
            self.penis+='='
            with open("penislength", "w") as penislength:
                penislength.write(f"{str(self.penis)}")
                
client = MyClient()
client.run(botid)
