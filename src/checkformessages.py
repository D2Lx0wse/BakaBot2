import datetime
import pathlib
import time
import re

from discord import Message

timer_file = pathlib.Path('timer')


async def checkformessages(message: Message):
    currenttime = int(time.time())
    aaa = timer_file.read_text()
    pasttime = currenttime - int(float(aaa))
    print(pasttime)
    if pasttime < 300:
        return

    shitposts = message.content.lower().split(" ")
    if "touhou" in shitposts:
        await message.reply("https://cdn.discordapp.com/attachments/918571405212270652/1056934396852191343/to_ho.mp4")
        timer_file.write_text(str(currenttime))
    elif "rent" in shitposts:
        await message.reply("https://media.discordapp.net/stickers/1009434642123870298.png")
        timer_file.write_text(str(currenttime))
    elif "cyberpunk" in shitposts:
        await message.reply("https://cdn.discordapp.com/attachments/1050415207849136148/1050427339537920070/bocchi_but_now_with_kid_named_cyberpunk.png")
        timer_file.write_text(str(currenttime))
    elif "makima" in shitposts:
        await message.reply(
            "https://tenor.com/view/makima-bean-beans-chainsaw-man-gif-25992235")
    elif "Banned" in shitposts:
        await message.reply(
            "https://tenor.com/view/ban-banned-sakura-anime-spray-gif-22585378")
        timer_file.write_text(str(currenttime))
    elif "turkey" in shitposts:
        await message.reply(
            "https://tenor.com/view/astolfo-turkey-turkish-rider-of-black-akif-gif-26672595")
        timer_file.write_text(str(currenttime))


