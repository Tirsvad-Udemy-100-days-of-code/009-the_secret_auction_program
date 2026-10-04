import pytest

from secret_auction.auction import add_bid, find_winner


def test_add_bid_stores_amount():
    bids = {}
    add_bid(bids, "Ann", 10)
    assert bids == {"Ann": 10}


def test_add_bid_replaces_existing_bidder():
    bids = {"Ann": 10}
    add_bid(bids, "Ann", 20)
    assert bids == {"Ann": 20}


def test_add_bid_rejects_negative():
    with pytest.raises(ValueError):
        add_bid({}, "Ann", -1)


def test_find_winner_returns_highest():
    assert find_winner({"Ann": 10, "Bob": 25.5, "Cy": 3}) == ("Bob", 25.5)


def test_find_winner_tie_first_wins():
    assert find_winner({"Ann": 10, "Bob": 10}) == ("Ann", 10)


def test_find_winner_empty_raises():
    with pytest.raises(ValueError):
        find_winner({})
