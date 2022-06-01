import re

dice_pattern = r"(\d+)[dD](\d+)"


def parse_dice_request(sentence:str) -> tuple[int, int]:
    """
    Parse a string to extract the number of dices and their number of sides.

    :param sentence: a string containing the expected pattern.
    :return: a tuple (number_of_dices, number_of_sides)
    """
    result = re.search(dice_pattern, sentence)
    if not result:
        raise ValueError(f"Dice pattern not found in string {sentence}")

    return int(result.group(1)), int(result.group(2))
