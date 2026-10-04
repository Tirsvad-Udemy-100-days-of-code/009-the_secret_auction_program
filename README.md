# 🚀 Secret Auction Program

A beginner-friendly Python program that runs a blind auction: bidders enter their name and bid one after another, the screen is cleared between bidders, and the highest bidder wins.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)

## 🧭 Overview

This is the Day 9 project of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*. Each bidder enters a name and a bid, which are stored in a dictionary (name → bid). After each bidder the program asks whether there are more bidders and, if so, clears the screen so the next bidder cannot see earlier bids. When everyone has bid, the program announces the winner.

See the [program flowchart](docs/flowchart.md) and the [plan and milestones](docs/plan.md).

## 📋 Requirements

- Python 3.13 or newer
- No runtime dependencies
- `pytest` for the tests (installed by the `dev` extra)
- [Doxygen](https://www.doxygen.nl/) (optional, to generate the API documentation)

## 🛠️ Setup

Create and activate a local virtual environment, upgrade pip, then install the project with its development tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## ▶️ Run

With the virtual environment active:

```bash
python -m secret_auction.main
```

or use the installed command:

```bash
secret-auction
```

## 🧪 Tests

```bash
python -m pytest
```

To generate the API documentation (output in `docs/doxygen/`):

```bash
doxygen Doxyfile
```

## 📄 License

Licensed under the GNU Affero General Public License v3.0 — see [LICENSE](LICENSE).

## 🔗 Links

- [Repository](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/009-the_secret_auction_program)
- [Documentation](docs/)
- [Issue tracker](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/009-the_secret_auction_program/issues)
