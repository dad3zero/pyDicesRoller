import diceroller.conf

import logging
from argparse import ArgumentParser

from dotenv import load_dotenv

load_dotenv()

from diceroller.cli import interaction_loop

def launch_bot():
    import diceroller.bots.discord

def launch_app():
    import diceroller.ui.tkapp

logging.info("App started")
logging.info(f"Using root path: {diceroller.conf.ROOT_DIR}")

parser = ArgumentParser("python -m diceroller", description="A cool dice rolling app")

actions = {"cli":interaction_loop,
           "app":launch_app,
           "bot":launch_bot,
           }

parser.add_argument("command", choices=list(actions),
                    help="Launches as an app (tkinter) or command line interface")

args = parser.parse_args()

if actions[args.command]:
    actions[args.command]()
else:
    print("Sorry, this action have not been implemented yet.")
