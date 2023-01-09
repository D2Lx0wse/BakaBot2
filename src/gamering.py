import random
from discord.ext import commands
from discord.ext.commands import Context, command
from random import randint

with open("coin", "r") as coinsave:
    coinS = coinsave.read()
coin = float(coinS)

with open("pochicoin", "r") as pochicoinsave:
    pochicoinS = pochicoinsave.read()
pochicoin = int(pochicoinS)

with open("chain", "r") as chainsave:
    chainS = chainsave.read()
chain = int(chainS)


@command()
@commands.cooldown(1.0, 30.0, commands.BucketType.guild)
async def pochibalancebalance(context: Context,):
    if str(context.channel) !="bot-channel":
        return
    else:
        global pochicoin
        pochicoint = str(pochicoin)
        text = pochicoint
        text +=" pochicoin"
        await context.send(text) 
        
@command()
@commands.cooldown(1.0, 30.0, commands.BucketType.guild)
async def pochiguess(context: Context, guess: int):
    global pochicoin
    bread = randint(1,16)
    guessstr = str(guess)
    if guess == bread :
          chain += 1
          prize = bread * chain
          text = "You guessed right. You won"
          text += str(prize)
          pochicoin += prize
          with open("pochicoin", "w") as pochicoinsave:
              pochicoinsave.write(str(pochicoin))
          text += " pochicoin and you streak is"
          text += str(chain)
          with open("chain", "w") as chainsave:
              chainsave.write(str(chain))
    else :
          chain = 0
          with open("chain", "w") as chainsave:
              chainsave.write(str(chain))
          text = "You guessed wrong. You lost"
          text += guessstr
          text += " pochicoin and your strike is reset"
          pochicoin -= guess
          with open("pochicoin", "w") as pochicoinsave:
              pochicoinsave.write(str(pochicoin))
    await(context.send.text) #maybe

@command()
@commands.cooldown(1.0, 2.0, commands.BucketType.guild)
async def mine(context: Context,):
    if str(context.channel) !="bot-channel":
        return
    else:
        global coin
        coin +=1
        coint =str(coin)
        text ="You bakas have "
        text +=coint
        text +=" bakacoin."
        with open("coin", "w") as coinsave:
            coinsave.write(coint)
        await context.send(text) 

@command()
@commands.cooldown(1.0, 30.0, commands.BucketType.guild)
async def balance(context: Context,):
    if str(context.channel) !="bot-channel":
        return
    else:
        global coin
        if coin == 1000:
            text ="everythingonarm they did it !!!!!! look!!!!"
        elif coin <= 1000:
            coint =str(coin)
            text = coint
            text +=" bakacoin"
        else:
            text ="everythingonarm they did it !!!!!! look!!!!"
        await context.send(text) 
    
@command()
@commands.cooldown(1.0, 120.0, commands.BucketType.guild)
async def invest(context: Context,):
    if str(context.channel) !="bot-channel":
        return
    else:
        global coin
        winchance = randint(1, 5)
        win = 3
        if winchance >= win:
            coin = coin * 2
        else:
            coin = coin / 2
        coint =str(coin)
        text ="You bakas have "
        text +=coint
        text +=" bakacoin."
        with open("coin", "w") as coinsave:
            coinsave.write(coint)
        await context.send(text) 
    
@command()
@commands.cooldown(1.0, 30.0, commands.BucketType.guild)
async def rps(context: Context, *, player_choice: str):
    player_choice = player_choice.replace("https://", "").replace("http://", "").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    text = f"you chose {player_choice}, i chose {computer_choice}. "

    if player_choice == computer_choice:
        text += "its a tie lmao"
    elif player_choice == "rock" and computer_choice == "scissors":
        text += "you win"
    elif player_choice == "paper" and computer_choice == "rock":
        text += "you win"
    elif player_choice == "scissors" and computer_choice == "paper":
        text += "you win"
    elif player_choice in options:
        text += "i win"
    else:
        text += random.choice(["i win", "you win"])

    await context.send(text)
