from slackbot.bot import Bot

from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


@listen_to('which one should i pick?', re.IGNORECASE)
def which_one(message):
    message.send('Why not both!?')

@listen_to('which one?', re.IGNORECASE)
def which_one_short(message):
    message.send('Why not both!?')

@listen_to('when should i do this?', re.IGNORECASE)
def when(message):
    message.send('Why not now!?')

@listen_to('how do you suggest i proceed?', re.IGNORECASE)
def how(message):
    message.send('¯\_(ツ)_/¯')

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
