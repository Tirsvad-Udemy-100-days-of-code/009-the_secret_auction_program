"""! @file main.py
@brief Command line interface for the secret auction program.
"""

import math

from secret_auction import constants
from secret_auction.auction import add_bid, find_winner


def clear_screen() -> None:
    """! @brief Hide previous entries by printing blank lines."""
    print("\n" * constants.CLEAR_SCREEN_LINES)


def ask_bid() -> float:
    """! @brief Ask for a bid until a valid, non-negative number is entered.
    @return The bid amount.
    """
    while True:
        try:
            amount = float(input(constants.PROMPT_BID))
        except ValueError:
            print(constants.MSG_INVALID_BID)
            continue
        if math.isfinite(amount) and amount >= 0:
            return amount
        print(constants.MSG_INVALID_BID)


def ask_more_bidders() -> bool:
    """! @brief Ask whether there are more bidders until yes/no is answered.
    @return True if more bidders exist, False otherwise.
    """
    while True:
        answer = input(constants.PROMPT_MORE_BIDDERS).strip().lower()
        if answer in constants.YES_ANSWERS:
            return True
        if answer in constants.NO_ANSWERS:
            return False
        print(constants.MSG_INVALID_ANSWER)


def main() -> None:
    """! @brief Run the blind auction: collect bids, then announce the winner."""
    print(constants.MSG_WELCOME)
    bids: dict[str, float] = {}  # kept outside the loop so bids are not lost
    more_bidders = True
    while more_bidders:
        name = input(constants.PROMPT_NAME).strip()
        add_bid(bids, name, ask_bid())
        more_bidders = ask_more_bidders()
        if more_bidders:
            clear_screen()
    winner, amount = find_winner(bids)
    print(constants.MSG_WINNER.format(name=winner, amount=amount))


if __name__ == "__main__":
    main()
