import random as rd

rd.seed()


def roll_dice(how_many:int = 1, sides:int = 6) -> tuple[int, ...]:
    """
    Roll a number of dices.

    :param how_many: number of dices to roll, optional, default is 1.
    :param sides: number of sides per dice, optional, default is 6. Expected values are 4, 6, 8, 10, 12, 20 and 100.
    :raises ValueError: raised if the number of dices is negative or null or if the number of sides is not as expected.
    :return: a tuple of dices results
    """
    if sides not in [4, 6, 8, 10, 12, 20, 100]:
        raise ValueError(f'Non valide number of dice sides, got {sides}')

    if how_many < 1:
        raise ValueError(f"At least one dice is required to be thrown, got {how_many}")

    dices_values = [rd.randint(1, sides) for _ in range(how_many)]
    return tuple(dices_values)
