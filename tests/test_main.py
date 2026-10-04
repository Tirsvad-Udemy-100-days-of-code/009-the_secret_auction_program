from secret_auction import constants
from secret_auction.main import ask_bid, ask_more_bidders, main


def feed(monkeypatch, answers):
    it = iter(answers)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(it))


def test_ask_bid_reprompts_on_invalid(monkeypatch, capsys):
    feed(monkeypatch, ["abc", "-5", "nan", "12.5"])
    assert ask_bid() == 12.5
    assert capsys.readouterr().out.count(constants.MSG_INVALID_BID) == 3


def test_ask_more_bidders(monkeypatch, capsys):
    feed(monkeypatch, ["maybe", "Y"])
    assert ask_more_bidders() is True
    assert constants.MSG_INVALID_ANSWER in capsys.readouterr().out
    feed(monkeypatch, ["no"])
    assert ask_more_bidders() is False


def test_main_announces_highest_bidder_and_clears_screen(monkeypatch, capsys):
    feed(monkeypatch, ["Ann", "10", "yes", "Bob", "25.5", "yes", "Cy", "3", "no"])
    main()
    out = capsys.readouterr().out
    assert "The winner is Bob with a bid of $25.50." in out
    assert out.count("\n" * constants.CLEAR_SCREEN_LINES) == 2


def test_main_single_bidder(monkeypatch, capsys):
    feed(monkeypatch, ["Ann", "7", "n"])
    main()
    assert "The winner is Ann with a bid of $7.00." in capsys.readouterr().out
