import random as rd
import re

rd.seed()

dice_pattern = r"(\d+)[dD](\d+)"


def roll_dice(how_many:int = 1, sides:int = 6) -> tuple[int, ...]:
    """
    Roll a number of dices.

    :param how_many: number of dices to roll, optional, default is 1.
    :param sides: number of sides per dice, optional, default is 6. Expected values are 4, 6, 8, 10, 12, 20 and 100.
    :raises ValueError: raised if the number of dices is negative or null or if the number of sides is not as expected.
    :return: a tuple of dices results
    :
    """
    if sides not in [4, 6, 8, 10, 12, 20, 100]:
        raise ValueError(f'Non valide number of dice sides, got {sides}')

    if how_many < 1:
        raise ValueError(f"At least one dice is required to be thrown, got {how_many}")

    dices_values = [rd.randint(1, sides) for _ in range(how_many)]
    return tuple(dices_values)


def parse_dice_request(sentence:str) -> tuple[int, int]:
    """
    Parse a string to extract the number of dices and their number of sides.

    :param sentence: a string containing the expected pattern.
    :return:
    """
    result = re.search(dice_pattern, sentence)
    if not result:
        raise ValueError(f"Dice pattern not found in string {sentence}")

    return int(result.group(1)), int(result.group(2))


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
            dices_number, dices_face = parse_dice_request(answer)
            dices_values = roll_dice(dices_number, dices_face)
            print(f"Valeurs : {dices_values}")
            print(f"Total : {sum(dices_values)}")
        except ValueError:
            print("Description non reconnue")


if __name__ == "__main__":
    interaction_loop()
