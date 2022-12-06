"""
CLI tool to fetch data from "https://xkcd.com/"

python my_task_1.py --max 87  --any 15
"""

import argparse
from random import randint
from typing import List


def number(start: int = 1, stop: int = 50, limit: int = 20) -> List[int]:
    """args:
    start (int): start value
    stop (int): end value
    limit (int): total values we want

    returns:
    List[int]: list of int random values in range(start:stop) with count limited to `limit` """

    result = [randint(start, stop + 1) for i in range(limit)]
    return result


# breakpoint()

if __name__ == '__main__':
    example = """example: python my_task_1.py --max 50 --any 20"""

    parser = argparse.ArgumentParser(description="CLI tool to fetch resource(s) from API")

    parser.add_argument("-m", "--max", type=int, help="max value")  # short forms and long forms
    parser.add_argument("-a", "--any", type=int, help="any value")  # -any not works

    args = parser.parse_args()
    print(args.max)
    print(args.any)

# breakpoint()
    a = number(1, args.max, args.any)       # a = comic_number_set
    print(a)

