from direct.showbase.ShowBase import ShowBase

class  Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('models/environment')
        self.model.reparentTo(render)

        self.model2 = loader.loadModel('smiley')
        self.model2.reparentTo(render)

        self.cube_texture = loader.loadTexture('block.png')
        self.cube = loader.loadModel('Cube/Cube.egg')
        self.cube.reparentTo(render)
        self.cube.setTexture(self.cube_texture)
        self.cube.setPos((50,0,0))

        

        self.model2.setPos()
        self.model2.setScale(10)

        self.model.setPos(0,20,0)



base = Game()
base.run()
        


