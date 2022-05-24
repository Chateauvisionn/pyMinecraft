from ursina import *

class Block(Button):
    def __init__(self, parent=scene, position=(0,0,0)):
        self.grass_texture = load_texture("assets/textures/grass.png")
        self.snow_texture = load_texture("assets/textures/snow.png")
        super().__init__(
            parent=parent,
            model='assets/models/block.obj',
            position=position,
            origin_y=.5,
            scale=.5,
            color=color.color(0, 0, random.uniform(1,1))
        )
