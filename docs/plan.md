# Plan: Secret Auction Program (Day 9)

## Context

Udemy 100 Days of Code blind-auction CLI. The repository uses a Python `.gitignore`, an AGPL `LICENSE` and a git-ignored `.env` (tokens, never printed or committed). Python 3.13 or newer is required.

## Working method

Work on ONE milestone at a time. Each milestone is one branch (`milestone/NN-name`) and one pull request. When a milestone is finished, stop, verify it and review before starting the next. Milestones and issues are also tracked on the Gitea repository (via API, token from `.env`).

## Milestone 1 - Project scaffold and repo metadata (`milestone/01-scaffold`)

- [x] Create `src/secret_auction/__init__.py`, `tests/`, `docs/`
- [x] `pyproject.toml`: `requires-python >=3.13`, src layout, no runtime deps, `dev` extra (`pytest`), pytest config, console script
- [x] `.env.example`; `.env` and `.venv/` ignored; add `docs/doxygen/` to `.gitignore`
- [x] `constants.py`
- [x] `Doxyfile`
- [x] Set repository description and topics (`python`, `udemy`, `100-days-of-code`, `blind-auction`, `beginner`) via API
- [x] Create milestones and issues on the host (milestones M1-M4, issues #1-#12)
- [x] Verify: create `.venv`, upgrade pip, `pip install -e ".[dev]"`
- [x] Save plan and milestones in `docs/plan.md`

## Milestone 2 - Core auction logic (`milestone/02-core-logic`)

- [x] `auction.py` (Doxygen comments): `add_bid`, `find_winner` (uses `max(bids, key=bids.get)`, `ValueError` on empty)
- [x] `tests/test_auction.py`
- Verify: `pytest` passes

## Milestone 3 - CLI program (`milestone/03-cli`)

- [x] `main.py`: prompt name and numeric bid (re-prompt on invalid), bids dict kept outside the loop, "other bidders? yes/no", clear screen with newlines between bidders, announce the winner
- [x] `tests/test_main.py` with monkeypatched `input`
- Verify: `pytest`; scripted run `python -m secret_auction.main` with two bidders

## Milestone 4 - Documentation (`milestone/04-docs`)

- [ ] `README.md` from the template (Overview, Requirements, Setup incl. creating/activating `.venv` and `python -m pip install --upgrade pip`, Run, Tests, License AGPL, Links)
- [ ] `docs/flowchart.md` (Mermaid plus link to the diagrams.net chart)
- [ ] Generate Doxygen docs if `doxygen` is installed
- Verify: README commands work verbatim; `.env` stays untracked
