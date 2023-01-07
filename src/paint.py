from discord.ext.commands import Context, command
from discord.ext import commands

canvas = []
with open('canvas', 'r') as f:
    for line in f:
        canvas.append(int(line.strip()))


@command()
@commands.cooldown(1.0, 30.0, commands.BucketType.guild)
async def paint(context: Context, height: int, width: int, color: str):
    global canvas
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "white", "black"]
    if color not in colors:
         text = "that's not a color silly"
         await context.send(text)
    else:
         discordcolors = [":red_square:", ":orange_square:", ":yellow_square:", ":green_square:", ":blue_square:", ":purple_square:", ":brown_square:", ":large_white_square:", ":large_black_square:", ]
         colorind = colors.index(color) 
         choice = discordcolors[colorind]
         canvaschoice = height * 5 + width - 1
         if canvaschoice >= 14:
             text = "that's not a valid pixel silly"
             await context.send(text)
         else:
             canvas[canvaschoice] = colorind
             with open('canvas', 'w') as f:
                for value in canvas:
                    f.write(str(value) + '\n')
             text = "result:\n"
             newlinevalue = [4, 9,]
             for pxl in canvas:
                 if pxl in newlinevalue:
                     text += discordcolors[pxl]
                     text += "\n"
                 else:
                     text += discordcolors[pxl]
                 await context.send(text)
                 
                
