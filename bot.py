#!/usr/bin/env python3.6

import discord
import asyncio
import requests
import json
from discord.ext import commands

startup_extensions = [
"cogs.events",
"cogs.no_erp",
"cogs.clever",
"cogs.reddit",
"cogs.BTC",
"cogs.husbando",
"cogs.update",
"cogs.userinfo",
"cogs.block_tenor",
"cogs.magic8ball"
]

client = discord.Client()

with open('token.json') as startup_data_file:
    startup_data = json.load(startup_data_file)
    startup_data_file.close()
    token = startup_data['tokens']['discord']['discord_token']
    prefix = startup_data['bot_settings']['prefix']

client = commands.Bot(command_prefix=(prefix),
                      pm_help=True,
                      case_insensitive=True,
                      owner_id=115895386606010376)


client.remove_command('help')
client.load_extension("jishaku")

async def background_loop():
    while True:
        await client.wait_until_ready()
        online = []
        x = client.get_all_members()
        for member in x:
            if member.status == discord.Status.online:
                online.append(member)
            elif member.status == discord.Status.idle:
                online.append(member)
            elif member.status == discord.Status.dnd:
                online.append(member)
        onlinemaid = "{0} maids!".format(str(len(set(online)) -1))

        await client.change_presence(activity=discord.Activity(name=onlinemaid, type=3))
        print("updated maid count, now " + str(len(set(online)) -1))
        await asyncio.sleep(600)

async def twitchlive():
    while True:
        await client.wait_until_ready()

        with open('twitch.json') as talk1:
            data1 = json.load(talk1)
            talk1.close()

        twitch_client_id = data1['token']['Twitch_Client-ID']
        streamers = data1['streamers']
        livemessage = None

        for streamer in streamers:

            if streamer == data1['streamers'][0]:
                live_notification = data1['discord']['live_notification']['streamer1']
                returndata_sendmsg = 'streamer1'
                returndata_msgid = 'disc_msg_id_str1'
            elif streamer == data1['streamers'][1]:
                live_notification = data1['discord']['live_notification']['streamer2']
                returndata_sendmsg = 'streamer2'
                returndata_msgid = 'disc_msg_id_str2'

            stream = requests.get("https://api.twitch.tv/helix/streams?user_id={0}".format(streamer), headers=twitch_client_id, timeout=None).json()

            if len(stream['data']) > 0:
                if live_notification == "notsendyet":
                    user = requests.get("https://api.twitch.tv/helix/users?id={0}".format(streamer),
                                        headers=twitch_client_id).json()
                    game = requests.get("https://api.twitch.tv/helix/games?id={0}".format(stream['data'][0]['game_id']),
                                        headers=twitch_client_id).json()

                    embed = discord.Embed(title=stream['data'][0]['title'], colour=discord.Colour(0x4b387a),
                                          url="https://twitch.tv/{}".format(stream['data'][0]['user_name']))
                    embed.set_image(url=stream['data'][0]['thumbnail_url'].format(width='1920', height='1080'))
                    embed.set_thumbnail(url=game['data'][0]['box_art_url'].format(width='272', height='380'))
                    embed.set_author(name=stream['data'][0]['user_name'],
                                     icon_url=user['data'][0]['profile_image_url'])
                    embed.set_footer(text="Twitch Livestream",
                                     icon_url="https://pngimg.com/uploads/twitch/twitch_PNG22.png")

                    embed.add_field(name="Game:", value=game['data'][0]['name'], inline=True)
                    embed.add_field(name="Viewers", value=stream['data'][0]['viewer_count'], inline=True)

                    channel = client.get_channel(int(data1['discord']['discord_channel']))
                    livemessage = await channel.send(embed=embed)

                    with open('twitch.json', 'w') as returndata:
                        data1['discord']['live_notification']["{}".format(returndata_sendmsg)] = "alreadysend"
                        data1['discord']['live_notification']["{}".format(returndata_msgid)] = "{0}".format(livemessage.id)
                        json.dump(data1, returndata)
                        talk1.close()

            else:
                with open('twitch.json', 'w') as returndata:
                    data1['discord']['live_notification']["{}".format(returndata_sendmsg)] = "notsendyet"
                    json.dump(data1, returndata)
                    talk1.close()

                if livemessage is not None:
                    await livemessage.delete()

        await asyncio.sleep(900)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.loop.create_task(background_loop())
client.loop.create_task(twitchlive())
client.run(token, bot=True, reconnect=True)
