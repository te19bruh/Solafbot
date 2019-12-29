import discord
import random
import string
from time import sleep

botid = ''

junior = 'Salanty#4884'
samuel = 'sampaixd#8896'
adams = 'Ugn Värmsson#7650'
adamw = 'Eyy B0ss#9506'
calle = 'Calle#4643'
solaf = 'Solaf#7852'

def id_generator(size=11, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class MyClient(discord.Client):

    penis='='
    easteregg=2
    
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
		# don't respond to ourselves
        if message.author == self.user:
            return
		
        if message.author == (self.user):
            return


        if message.content == ('Solaf, hjälp!'):
            await message.channel.send('Trim!')
            await message.channel.send('Solaf, vad kollar du på?')
            await message.channel.send('Solaf, har du sett klistermärkerna?')
            await message.channel.send(f'+{self.easteregg} easteregg ;)')			

        if message.content == ('Solaf, har du sett klistermärkerna?'):
            for i in range(10):	
                async with message.channel.typing():
                    sleep(9)
            await message.channel.send('Ja.')

        if message.content == ('Solaf, vad kollar du på?'):
            mymessage = "https://youtube.com/watch?v="+str(id_generator())
            async with message.channel.typing():
                sleep(random.randint(1,2))
            await message.channel.send(mymessage)

        if str(message.author) != samuel:
            if message.content == ('Solaf, Samuel skickade mig.'):
                for i in range(3):
                    if i==1:
                        videonumber = random.randint(1,1000)
                        mymessage = "https://youtube.com/"+str(videonumber)
                        async with message.channel.typing():
                            sleep(random.randint(1,2))
                        await message.channel.send(mymessage)
                    if i==2:
                        sleep(5)
                        mymessage = "Berätta inte till Greta :|"
                        async with message.channel.typing():
                            sleep(random.randint(1,2))
                        await message.channel.send(mymessage)
        if message.content == ('Solaf, tar det vanliga.'):
            if str(message.author) == samuel:
                for i in range(3):
                    if i==1:
                        videonumber = random.randint(1,1000)
                        mymessage = "https://youtube.com/"+str(videonumber)
                        async with message.channel.typing():
                            sleep(random.randint(1,2))
                        await message.channel.send(mymessage)
                    if i==2:
                        sleep(5)
                        mymessage = "Berätta inte till Greta :|"
                        async with message.channel.typing():
                            sleep(random.randint(1,2))
                        await message.channel.send(mymessage)
        if str(message.author) != calle:
            if message.content == ('Trim!'):
                async with message.channel.typing():
                    sleep(random.randint(1,2))
                await message.channel.send('Halal. :thumbsup: ')
                
        if message.content == ('+penis'):
            async with message.channel.typing():
                sleep(random.randint(1,2))
            await message.channel.send(f'8{self.penis}3')
            self.penis+='='
				
client = MyClient()
client.run(botid)
