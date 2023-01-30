from argparse import ArgumentParser

from .cli import interaction_loop

parser = ArgumentParser("python -m diceroller", description="A cool dice rolling app")

actions = {"cli":interaction_loop,
           "app":None}

parser.add_argument("command", choices=list(actions),
                    help="Launches as an app (tkinter) or command line interface")

args = parser.parse_args()

actions[args.command]()
