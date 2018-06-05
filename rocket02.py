import maya.cmds as cmds
from pymel.core import *
import os
import random
import math


class AR_poly(object):
    use = None

    def showUI(cls, uifile):
        win = cls(uifile)
        win.create()
        return win

    def __init__(self, filepath):
        AR_poly.use = self
        self.window = '0000'
        self.uifile = filepath

    def close(self, *args):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

    def create(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

        self.window = cmds.loadUI(uiFile=self.uifile, verbose=True)
        cmds.showWindow(self.window)


class tplink(object):
    use = None

    def __init__(self):
        tplink.use = self

    def create(self, *args):

        self.obj = ls(sl=True)

        if len(self.obj) > 1:
            polyUnite()
            self.obj = ls(sl=True)

        speed = None
        ratatex = None
        try:
            speed_path = '|'.join(['OOR', 'speed'])
            speed = float(cmds.textField(speed_path, q=True, text=True))
        except:
            raise

        try:
            ratatex_path = '|'.join(['OOR', 'ratatex'])
            ratatex = float(cmds.textField(ratatex_path, q=True, text=True))
        except:
            raise

        self.mygrid = polyPlane()

        self.mygrid[0].rotateX.set(ratatex)
        self.mygrid[0].translate.set(0, 10, 10)
        self.mygrid[0].scale.set(30, 20, 20)
        select(self.mygrid[0])
        self.myem = emitter(type='surface', speed=speed, speedRandom=10, rate=0.005)
        self.mypa = particle(name='mypa')
        connectDynamic(self.mypa[0], em=self.myem)
        self.mygr = gravity(self.mypa, m=4)
        connectDynamic(self.mypa, f=self.mygr)

        particleInstancer('mypa', object=self.obj, aimDirection='velocity')
        select(self.mypa[0])
        self.myem2 = emitter(type='direction', rate=1000, spread=1, speed=4, speedRandom=3)
        self.mypa2 = particle(name='trailParticle')

        connectDynamic(self.mypa2[0], em=self.myem2)
        cmds.setAttr("trailParticleShape.lifespanMode", 2)
        self.mypa2[0].lifespanMode.set(2)
        self.mypa2[0].lifespanRandom.set(0.2)
        self.mypa2[0].particleRenderType.set(8)

        cmds.select('trailParticleShape')
        cmds.addAttr(ln="radius", at="float", min=0, max=100, dv=1)

    def change(self, *args):
        rad = None
        try:
            rad_path = '|'.join(['OOR', 'rad'])
            rad = float(cmds.textField(rad_path, q=True, text=True))
        except:
            raise

        cmds.setAttr('trailParticleShape.radius', rad)


opcc = tplink()
win = AR_poly(os.path.join(os.getenv('HOME'), 'taka.ui'))
win.create()
