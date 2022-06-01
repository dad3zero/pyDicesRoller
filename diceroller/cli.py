from diceroller import roller
from diceroller import parser


def interaction_loop():
    """
    Interaction CLI loop. Call this function to use the application with the
    CLI.
    """
    while True:
        answer = input("Lancer un dé ? (q pour quitter) : ")
        if answer in "qQ":
            break

        try:
            dices_number, dices_face = parser.parse_dice_request(answer)
            dices_values = roller.roll_dice(dices_number, dices_face)
            print(f"Valeurs : {dices_values}")
            print(f"Total : {sum(dices_values)}")
        except ValueError:
            print("Description non reconnue")
