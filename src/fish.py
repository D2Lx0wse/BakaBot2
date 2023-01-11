from discord.ext.commands import Context, command
from discord.ext import commands
import time

with open('fishtime', 'r') as timesave:
    aaa = timesave.read()
with open('fishhealth', 'r') as healthsave:
    health = float(healthsave.read())


def hunger():
    currenttime = int(time.time())
    global health
    pasttime = currenttime - int(float(aaa))
    print(pasttime)
    healthloss = pasttime / 864
    health -= healthloss
    if health <= 0:
        fishdead = 1
    if health >= 200:
        fishdead = 1
    else:
        fishdead = 0
    with open('fishtime', 'w') as timesave:
        timesave.write(str(currenttime))
    with open('fishhealth', 'w') as healthsave:
        healthsave.write(str(health))

    
@command()
@commands.cooldown(1.0, 30.0, commands.BucketType.guild)
async def fish(context: Context,):
    global health
    hunger()
    if health <= 0:
        await context.send("uh oh fishy ded of hunger :skull:")
    elif health >= 200: 
        await context.send("uh oh fishy too fat it ded :skull:")
    else:
        if health >= 150:
            await context.send("fishy fat but ok")
        elif health <= 50:
            await context.send("fishy thin but ok")
        else:
            await context.send("fishy good :fish:")
            
@command()
@commands.cooldown(1.0, 30.0, commands.BucketType.guild)
async def feedfish(context: Context,):
    global health
    hunger()
    if fishdead == 1:
        await context.send("fishy dead")
    else:
        health += 20
        with open('fishhealth', 'w') as healthsave:
            healthsave.write(health)
        await context.send("fishy fed")
