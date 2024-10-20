import re
from typing import Callable, Generator


def generator_numbers(text_to_parse: str) -> Generator[float, None, None]:
    """Creates generator with all numbers in the text.

    :param text_to_parse: input text
    :return: generator with numbers
    """

    pattern = r"\b\d+(\.\d+)?\b"
    for match in re.finditer(pattern, text_to_parse):
        yield float(match.group())


def sum_profit(text_to_parse: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """Calculates the sum of all numbers in the text."""
    return sum(func(text_to_parse))
