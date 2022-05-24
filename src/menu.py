from ursina import *

app = Ursina()
window.borderless = False
window.exit_button.visible = False

print("Menu isn't ready yet, start the game with game.py (args for world gen: \"flat\" or \"random\")")

buttonsd = {
    "Random generated world": None,
    "Flat world": None,
}

buttons = ButtonList(buttonsd)

app.run()