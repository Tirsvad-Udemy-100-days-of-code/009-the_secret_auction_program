"""! @file auction.py
@brief Core blind auction logic (no input/output).
"""


def add_bid(bids: dict[str, float], name: str, amount: float) -> None:
    """! @brief Record a bid, replacing any earlier bid by the same bidder.
    @param bids Dictionary mapping bidder name to bid amount (modified in place).
    @param name Name of the bidder.
    @param amount Bid amount; must not be negative.
    @throws ValueError If the amount is negative.
    """
    if amount < 0:
        raise ValueError("Bid amount must not be negative.")
    bids[name] = amount


def find_winner(bids: dict[str, float]) -> tuple[str, float]:
    """! @brief Find the highest bidder.
    @param bids Dictionary mapping bidder name to bid amount.
    @return Tuple of (winner name, winning amount). The first bidder wins ties.
    @throws ValueError If there are no bids.
    """
    if not bids:
        raise ValueError("No bids have been placed.")
    winner = max(bids, key=bids.__getitem__)
    return winner, bids[winner]
