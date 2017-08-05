"""Setup module for project."""

from setuptools import setup

setup(
    scripts=["cards.py", "players.py", "blackjack.py"],
    entry_points={
        "console_scripts": [
            "blackjack=blackjack:main"
        ]
    }
)
