# RL_Mass_Open

A simple python script to easily open a full stack of reward items in Rocket League.

I may host this as an executable at some point, but for now this will have to do.

## Installation

To get started you'll need Python3, and pip installed. There's plenty of tutorials out there so I'm not going to cover that.

Once you're all set,  you'll need to get the pyinstaller package: run `pip install pyinstaller`

Then, clone this repo (or just snag the `rl_autoloot.py` file), and with your terminal pointed to the directory of `rl_autoloot.py`, run `pyinstaller rl_autoloot.py`

This will create several folders in the same directory, the actual program executable will be in the `dist/` folder

## Usage

With Rocket League running in 'windowed' mode on your primary monitor, run the program, it should anchor near the top-right of the same screen.

In-game, navigate to the 'Reward Items' page, and select the item stack you want to open.

Bring the `rl_autoloot` program to the foreground, enter the number of items you have in that stack (or would like to open), and click the "Start Opening" button.

