from ursina import *
from lib.player import Player
from lib.gen_terrain import Terrain
import sys

app = Ursina()
window.borderless = False
window.exit_button.visible = False

# scene.fog_color = color.rgb(150,150,150)
# scene.fog_density = 0.03

sky = Sky()
player = Player()
terrain = Terrain()
terrain.gen(mode=sys.argv[1])

app.run()