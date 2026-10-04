"""! @file constants.py
@brief Constants used by the Secret Auction program.
"""

## Number of blank lines printed to hide previous bidders' entries.
CLEAR_SCREEN_LINES = 100

## Answers accepted as "yes" when asking for more bidders.
YES_ANSWERS = ("yes", "y")

## Answers accepted as "no" when asking for more bidders.
NO_ANSWERS = ("no", "n")

## Path of the file holding environment variables (tokens).
ENV_FILE = ".env"

## Name of the environment variable holding the Gitea token.
GITEA_TOKEN_ENV_VAR = "GITEA_TOKEN"

## Prompt asking for the bidder's name.
PROMPT_NAME = "What is your name? "

## Prompt asking for the bid amount.
PROMPT_BID = "What is your bid? $"

## Prompt asking whether more bidders exist.
PROMPT_MORE_BIDDERS = "Are there any other bidders? Type 'yes' or 'no'. "

## Message shown when the bid is not a valid number.
MSG_INVALID_BID = "Please enter a valid, non-negative number."

## Message shown when the yes/no answer is not understood.
MSG_INVALID_ANSWER = "Please type 'yes' or 'no'."

## Template for the winner announcement.
MSG_WINNER = "The winner is {name} with a bid of ${amount:.2f}."

## Welcome banner.
MSG_WELCOME = "Welcome to the secret auction program."
