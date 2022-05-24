from ursina import *
from lib.block import Block
from perlin_noise import PerlinNoise
from numpy import floor

class Terrain():
    def __init__(self) -> None:
        self.tWidth = 36
        self.amp = 3
        self.freq = 24
        self.terrain = Entity(model=None, collider=None)
        self.blocks = []

    def gen(self, mode: str):
        if mode == 'flat':
            for i in range(self.tWidth*self.tWidth):
                block = Block(parent=self.terrain, position=(i%32, 0, i//32))
                block.x = floor(i/self.tWidth)
                block.z = floor(i%self.tWidth)
                block.y = floor(0)
                self.blocks.append(block)
                
            for i in self.blocks:
                if i.y > 50:
                    i.texture = block.snow_texture



        elif mode == 'random':
            noise = PerlinNoise(octaves=3, seed=random.randint(0, 2147483647))
            
            for i in range(self.tWidth*self.tWidth):
                block = Block(parent=self.terrain, position=(i%32, 0, i//32))
                block.x = floor(i/self.tWidth)
                block.z = floor(i%self.tWidth)
                block.y = floor((noise( [block.x/self.freq, block.z/self.freq])) * self.amp)
                self.blocks.append(block)


            for i in self.blocks:
                if i.y > 50:
                    i.texture = block.snow_texture
                    
        else:
            print('invalid mode')
            exit(1)
        
        self.terrain.combine()
        self.terrain.collider = 'mesh'
        self.terrain.texture=block.grass_texture