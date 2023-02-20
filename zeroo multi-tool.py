import time
from os import system, name
import sys
import os
sys.tracebacklimit = 0
import subprocess
try:
    import discord
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
import discord
from discord.ext import commands
import json
try:
    import colorama
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
from colorama import Fore, init, Style
from datetime import datetime
import asyncio
import time
init()
#this is required for some windows users
# enabling member intents:
intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)

# disclaimer:
print(f'''Must have enabled all bot intents and use a bot token or else it won't work, same as Mass Ban and Mass Nickname.
Must use a human account and human token to use or else it won't work.
''')
time.sleep(0.8)

# poor booting animation:
print(f"Starting mass-dm tool")
time.sleep(0.3)
print(f"15/100")
time.sleep(0.5)
print(f"25/100")
time.sleep(0.5)
print(f"35/100")
time.sleep(0.5)
print(f"45/100")
time.sleep(0.5)
print(f"55/100")
time.sleep(0.5)
print(f"65/100")
time.sleep(0.6)
print(f"75/100")
time.sleep(0.6)
print(f"85/100")
time.sleep(0.7)
print(f"95/100")
time.sleep(1)
print(f"failed to start")
time.sleep(0.7)
print(f"get trolled lol")
time.sleep(1)
print(f"mass-dm tool has started")
time.sleep(1)

# setting bot to true or false:
chupapi = input(f'Is this a bot?(y or n) = ')
if chupapi == "y":
    munanyo = "bot"
elif chupapi == "n":
    munanyo = "human"
while chupapi !="n" and chupapi != "y":
    print(f'Stupid dumbfuck\ny is yes\nn is no\nNow enter y or n')
    chupapi = input('Is this a bot?(y or n) = ')
if chupapi == "y":
    munanyo = "bot"
elif chupapi == "n":
    munanyo = "human"

# getting the token:
token = input(f"Enter token = ")


# main part of the code:
async def main():
    # mass dm part of the code:
    async def massdm():
        print(f'loading...')
        if chupapi == "n":
            input(
                f"Stupid monkey mass-dm doesn't work if human tokens\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
        else:
            pass
        print(f'mass-dm is ready to rape everyone')
        while True:
            try:
                guild_id = int(input('Server ID = '))
                break
            except ValueError:
                print(f'Enter a valid Server ID')
                continue
        print(f'Loading...')
        for guild in client.guilds:
            if guild.id == guild_id:
                print('Server that is getting raped "{}", smoke that pack on these bozos'.format(guild.name))
                ahegao = input(f"Enter text = ")
                membercount = len(guild.members)
                index = 0
                for member in guild.members:
                    index += 1
                    try:
                        await member.send(ahegao)
                        print(
                            f"[+] {index}/{membercount} Sent {ahegao} to {member}")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"[-] {index}/{membercount} failed to send {ahegao} to {member} - {e}")
        print(f'Finished raping dms')
        input(f"\nNow go rape your self or press Enter to return to the main menu")
        await main()
    # embed mass dm friends part of the code:
    async def embedmassdmfriends():
        print(f'loading...')
        if chupapi == "y":
            input(
                f"Stupid monkey mass-dm friends doesn't work if bot tokens\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
        else:
            pass
        print(f'Embed-Mass Dm friends was selected')
        print(f'Loading...')
        print(f'leave blank = none')
        title = input(f"Title = ")
        desc = input(f"Description = ")
        thumb = input(f"Thumbnail(url) = ")
        img = input(f"Image(url) = ")
        footer = input(f"Footer = ")
        footer_icon = input(
            f"Footer Icon(url) = ")
        author = input(f"Author = ")
        icn = input(
            f"Author Icon(url) = ")
        if title and desc and thumb and img and footer and footer_icon and author and icn is None:
            input(f"You can't put none every where stupid mf\nPress Enter to return to the main menu")
            await main()
        else:
            pass
        karma = discord.Embed(
            title=f"{title}",
            description=f'{desc}',
            color=discord.Colour.default())
        karma.set_thumbnail(url=f'{thumb}'),
        karma.set_image(url=f"{img}")
        karma.set_footer(text=f"{footer}", icon_url=f"{footer_icon}")
        karma.set_author(name=f"{author}", icon_url=f"{icn}")
        friendcounter = len(client.user.friends)
        index = 0
        for user in client.user.friends:
            index += 1
            try:
                await user.send(embed=karma)
                print(f"[+] {index}/{friendcounter} Sent the embed to {user}")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(
                    f"[-] {index}/{friendcounter} Failed to send the embed to {user} - {e}")
        print(f'Finished raping friends dms')
        input(f"\nNow go rape your self or press Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        await main()
    # embed mass dm part of the code:
    async def embedmassdm():
        print(f'Loading...')
        if chupapi == "n":
            input(
                f"Stupid monkey mass-dm doesn't work if human tokens\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
        else:
            pass
        print(f'Embed-Mass Dm was selected')
        while True:
            try:
                guild_id = int(input('Server ID = '))
                break
            except ValueError:
                print(f'Enter a valid Server ID')
                continue
        print(f'Embed-Mass Dm was selected')
        print(f'Loading...')
        print(f'leave blank = none')
        for guild in client.guilds:
            if guild.id == guild_id:
                hanime_tv = input(f"Title = ")
                hentai = input(f"Description = ")
                seggs = input(
                    f"Thumbnail(url) = ")
                incest = input(
                    f"Image(url) = ")
                knockknockknock = input(f"Footer = ")
                fbi = input(
                    f"Footer Icon(url) = ")
                opn = input(f"Author =")
                up = input(
                    f"Author Icon(url) = ")
                if hanime_tv and hentai and seggs and incest and knockknockknock and fbi and opn and up is None:
                    input(
                        f"You can't put none every where stupid mf\nPress Enter to return to the main menu")
                    await main()
                else:
                    pass
                kamehameha = discord.Embed(
                    title=f"{hanime_tv}",
                    description=f'{hentai}',
                    color=discord.Colour.purple())
                kamehameha.set_thumbnail(url=f'{seggs}'),
                kamehameha.set_image(url=f"{incest}")
                kamehameha.set_footer(text=f"{knockknockknock}", icon_url=f"{fbi}")
                kamehameha.set_author(name=f"{opn}", icon_url=f"{up}")
                membercount = len(guild.members)
                index = 0
                for member in guild.members:
                    index += 1
                    try:
                        await member.send(embed=kamehameha)
                        print(
                            f"[+] {index}/{membercount} Sent the embed to {member}")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"[-] {index}/{membercount} Failed to send the embed to {member} - {e}")
        print(f'Finished raping dms')
        input(f"\nNow go rape your self or press Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        await main()
    # nuke part of the code:
    async def Nuke():
        print(f'Loading...')
        print('Nuke was selected')
        if chupapi == "n":
            print(f"Mass Ban won't work with a Human tokan")
        else:
            pass
        while True:
            try:
                server_id = int(input(f'Server ID = '))
                break
            except ValueError:
                print(f'Enter a valid Server ID')
                continue
        print(f'Loading...')
        for guild in client.guilds:
            if guild.id == server_id:
                print('Server that is getting raped "{}", smoke that pack on these bozos'.format(guild.name))
                print(f"Leave blank = none")
                ban_reason = input('Enter ban reason: ')
                index = 0
                guildinvites = len(await guild.invites())
                for invite in await guild.invites():
                    index += 1
                    try:
                        await invite.delete()
                        print(
                            f"[+] {index}/{guildinvites} Deleted invite [{invite}] in '{guild.name}'")
                    except Exception as e:
                        print(
                            f"[-]  {index}/{guildinvites} Failed to delete [{invite}] in '{guild.name}' - {e}")
                index = 0
                guildchannels = len(guild.channels)
                for channel in guild.channels:
                    index += 1
                    try:
                        await channel.delete()
                        print(
                            f"[+] {index}/{guildchannels} Deleted channel [{channel.name}] in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"[-] {index}/{guildchannels} Failed to delete channel [{channel.name}] in '{guild.name}' - {e}")
                index = 0
                guildroles = len(guild.roles)
                for role in guild.roles:
                    index += 1
                    try:
                        await role.delete()
                        print(
                            f"[+] {index}/{guildroles} Delted role [{role.name}] in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"[-] {index}/{guildroles} Failed to delete role [{role.name}] in '{guild.name}' - {e}")
                index = 0
                guildmembers = len(guild.members)
                for member in guild.members:
                    index += 1
                    try:
                        await guild.ban(member, reason=ban_reason, delete_message_days=7)
                        print(
                            f"[+] {index}/{guildmembers} Successfully banned [{member}] [ID: {member.id}] in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"[-] {index}/{guildmembers} Failed to ban [{member}] [ID: {member.id}] in '{guild.name}'- {e}")
                index = 0
                guildemojis = len(guild.emojis)
                for emoji in guild.emojis:
                    index += 1
                    print(emoji)
                    try:
                        await emoji.delete()
                        print(
                            f"[+] {index}/{guildemojis} Deleted emoji [{emoji.name}] in '{guild.name}'")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"[-] {index}/{guildemojis} Failed to delete emoji [{emoji.name}] in '{guild.name}' - {e}")
        print(f'Finished raping the server')
        input(f"\nNow go rape your self or press Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        await main()
    # server id displayer:
    async def server_id_displayer():
        index = 0
        for guild in client.guilds:
            if munanyo == "bot":
                try:
                    senpai = 0
                    if len(await guild.invites()) != 0:
                        for invite in await guild.invites():
                            while senpai < 1:
                                INVITE = f" | Server invite = {invite}"
                                senpai += 1
                    else:
                        for channel in guild.channels:
                            if channel.position == 1:
                                try:
                                    INVITE = f" | Server invite = {await channel.create_invite()}"
                                except:
                                    INVITE = f" | Server invite = Failed to fetch the invite link"
                except:
                    INVITE = f" | Server invite = Failed to fetch the invite link"
            else:
                INVITE = ""
            index += 1
            print(
                f"Server info = [{index}/{len(client.guilds)}] [{guild.name}] [{guild.id}] | Total members = [{len(guild.members)}] | Server invite = {INVITE}")
        print(f'Finished raping server info')
        input(f"\nNow go rape your self or press Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        await main()
    # embed mass dm all client users:
    async def embed_dm_all_client_users():
        users = len(client.users)
        index = 0
        print(f'Loading...')
        if chupapi == "n":
            input(
                f"Stupid monkey mass-dm doesn't work if human tokens\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
        else:
            pass
        print(f'Embed-Mass Dm Client Users was selected')
        print(f"Leave blank = none")
        for user in client.users:
            hanime_tv = input(f"Title = ")
            hentai = input(f"Description = ")
            seggs = input(
                f"Thumbnail(url) = ")
            incest = input(
                f"Image(url) = ")
            knockknockknock = input(f"Footer = ")
            fbi = input(
                f"Footer icon(url) = ")
            opn = input(f"Author = ")
            up = input(
                f"Author icon(url) = ")
            if hanime_tv and hentai and seggs and incest and knockknockknock and fbi and opn and up is None:
                input(
                    f"You can't put none every where stupid mf\nPress Enter to return to the main menu")
                await main()
            else:
                pass
            kamehameha = discord.Embed(
                title=f"{hanime_tv}",
                description=f'{hentai}',
                color=discord.Colour.default())
            kamehameha.set_thumbnail(url=f'{seggs}'),
            kamehameha.set_image(url=f"{incest}")
            kamehameha.set_footer(text=f"{knockknockknock}", icon_url=f"{fbi}")
            kamehameha.set_author(name=f"{opn}", icon_url=f"{up}")
            usercount = len(client.users)
            index = 0
            for user in client.users:
                index += 1
                try:
                    await user.send(embed=kamehameha)
                    print(
                        f"[+] {index}/{usercount} Sent the embed to {user}")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(
                        f"[-] {index}/{usercount} Failed to the embed to {user} - {e}")
        print(f'Finished raping dms')
        input(f"\nNow go rape your self or press Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
    #mass dm client users:
    async def dm_all_client_users():
        users = len(client.users)
        index = 0
        print(f'Loading...')
        if chupapi == "n":
            input(
                f"Stupid monkey mass-dm doesn't work if human tokens\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
        else:
            pass
        print(f'Mass-Dm Client Users was selected')
        for user in client.users:
            yamete_kudasai = input(f"Text = ")
            usercount = len(client.users)
            index = 0
            for user in client.users:
                index += 1
                try:
                    await user.send(yamete_kudasai)
                    print(
                        f"[+] {index}/{usercount} Sent {yamete_kudasai} to {user}")
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(
                        f"[-] {index}/{usercount} Failed to send the text to {user} - {e}")
        print(f'Finished raping dms')
        input(f"\nNow go rape your self or press Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
    # guild leaver:
    async def guild_leaver():
        last_question = input(f"Leave all servers(y or n) = ")
        if last_question == "y":
            guild_counter = len(client.guilds)
            index = 0
            for guild in client.guilds:
                index +=1
                try:
                    await guild.leave()
                    print(f"[+] {index}/{guild_counter} Left from {guild.name}")
                except Exception as e:
                    print(f"[-] {index}/{guild_counter} Failed to leave from {guild.name} - {e}")
        elif last_question == "n":
            input("Phew...\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
        while last_question != "n" and chupapi != "y":
            print(f'Stupid dumbfuck\ny is yes\nn is no\nNow enter y or n')
            last_question = input(f"Are you sure you wanna leave all server? ")
        if last_question == "y":
            guild_counter = len(client.guilds)
            index = 0
            for guild in client.guilds:
                index +=1
                try:
                    await guild.leave()
                    print(f"[+] {index}/{guild_counter} Left from {guild.name}")
                except Exception as e:
                    print(f"[-] {index}/{guild_counter} Failed to leave from {guild.name} - {e}")
        elif last_question == "n":
            input("Phew...\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
    async def exit():
        await client.close()
        input(f"\nNow go rape your self or press Enter 3 times to close the program")
        [input(i) for i in range(2, 0, -1)]
        raise SystemExit
    # raid part of the code:
    async def raid():
        print(f'Loading...')
        print('Raid was selected')
        if chupapi == "n":
            print(f"Mass Nickname only works with a Bot token")
        else:
            pass
        while True:
            try:
                server_id = int(input(f'Server ID = '))
                break
            except ValueError:
                print(f'Enter a valid Server ID')
                continue
        print('Loading...')
        for guild in client.guilds:
            if guild.id == server_id:
                print('Server that is getting raped "{}", smoke that pack on these bozos'.format(guild.name))
                servername = input(f"Server name = ")
                role = input(f"Role = ")
                role_ammount = int(input(f"Roles amount = "))
                text_channel = input(f"Channels name = ")
                channel_ammount = int(input(f"Channels amount = "))
                newnick = input(f"Nickname = ")
                if servername == "":
                    servername = guild.name
                await guild.edit(name=servername)
                print(f"[+] Renamed the server to = {servername}")
                index = 0
                while index < channel_ammount:
                   await guild.create_text_channel(text_channel)
                   index += 1
                   print(f"[+] {index}/{channel_ammount} Created a text channel = {text_channel} in {guild.name}")
                   await asyncio.sleep(0.1)
                index_roles = 0
                while index_roles < role_ammount:
                    index_roles += 1
                    await guild.create_role(name=role)
                    print(f"[+] {index_roles}/{role_ammount} Created a role = {role} in {guild.name}")
                    await asyncio.sleep(0.1)
                index = 0
                usercount = len(guild.members)
                for user in guild.members:
                    index += 1
                    try:
                        await user.edit(nick=newnick)
                        print(
                            f"[+] {index}/{usercount} Changed {user} name in {guild.name} to {newnick}")
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(
                            f"[-] {index}/{usercount} Failed to change {user} name in {guild.name} to {newnick} - {e}")
        print(f'Finished raping the server')
        input(f"\nNow go rape your self or press Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        await main()
    if munanyo == "human":
        Connected = f"Server count = [{len(client.guilds)}] | Friend count = [{len(client.user.friends)}]"
    else:
        Connected = f"Server count = [{len(client.guilds)}] | User count = [{len(client.users)}]"
    print('''

                           ▒███████▒▓█████  ██▀███   ▒█████   ▒█████  
                           ▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒
                           ░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒
                            ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░▒██   ██░
                           ▒███████▒░▒████▒░██▓ ▒██▒░ ████▓▒░░ ████▓▒░
                             ▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░ 
                             ░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░ 
                             ░ ░ ░ ░ ░   ░     ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒  
                              ░ ░       ░  ░   ░         ░ ░      ░ ░  
                                ░   
''')
    print(f'''
                            Made by zeroo[https://github.com/zeroo-0]          
                        Logged in as [{client.user}] (ID: {client.user.id})
                               {Connected}

 ╔═════╩═════════════════════════════╦════════════════════════════╦══════════════════╩═══════════════╗
 ║ (0) < Nuke                        ║ (4) < Leave all Servers    ║ (8)  < Mass Dm friends           ║
 ║ (1) < Raid                        ║ (5) < Mass Dm              ║ (9)  < Mass Embed Dm friends     ║
 ║ (2) < Mass Dm Client Users        ║ (6) < Mass Embed Dm        ║ (10) < Exit                      ║  
 ║ (3) < Mass Embed Dm Client Users  ║ (7) < Display all Servers  ║                                  ║
 ╚═════╦═════════════════════════════╩════════════════════════════╩══════════════════╦═══════════════╝
         
''')
    select = input(f"Select: ")
    if select == '8': # mass dm friends part of the code:
        print(f'{Fore.LIGHTYELLOW_EX}------')
        if chupapi == "y":
            input("Stupid monkey mass-dm doesn't work if bot tokens\nPress Enter to return to the main menu")
            os.system('cls' if os.name == 'nt' else 'clear')
            await main()
        else:
            pass
        overflow = input(f"Mass Dm friends was selected\nText = ")
        friendcounter = len(client.user.friends)
        index = 0
        for user in client.user.friends:
            index += 1
            try:
                await user.send(f"{overflow}")
                print(f"[+] {index}/{friendcounter} Sent {overflow} to {user}")
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"[-] {index}/{friendcounter} Failed to send {overflow} to {user} - {e}")
        print(f'Finished raping your friends')
        input(f"\nNow go rape your self or press Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        await main()
    elif select == '0':
        await Nuke() # runs the nuke part of the code
    elif select == '10':
        await exit() # runs the exit part of the code
    elif select == '1':
        await raid() # runs the raid part of the code
    elif select == '5':
        await massdm() # runs the mass dm part of the code
    elif select == '6':
        await embedmassdm() # runs the embed mass dm part of the code
    elif select == '9':
        await embedmassdmfriends() # runs the embed mass dm friends part of the code
    elif select == '7':
        await server_id_displayer() # runs the embed mass dm part of the code
    elif select == '4':
        await guild_leaver() # runs the guild-leaver part of the code
    elif select == '3':
        await embed_dm_all_client_users() # runs the embed mass dm client users part of the code
    elif select == '2':
        await dm_all_client_users() # runs the mass dm client users part of the code
    else:
        input(f"Invalid option(1-10)\nPress Enter to return to the main menu")
        os.system('cls' if os.name == 'nt' else 'clear')
        await main()

# on ready event:
def start():
    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/zeroo-0"))
        await client.change_presence(status=discord.Status.dnd)
        os.system('cls' if os.name == 'nt' else 'clear')
        await main()

start()

if munanyo == "human":
    client.run(token) # runs the human token if human token was selected
elif munanyo == "bot":
    client.run(token) # runs the bot token if bot token was selected

#end
