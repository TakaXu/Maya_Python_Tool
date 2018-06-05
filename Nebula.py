import maya.cmds as cmds
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

    def create(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

        self.window = cmds.loadUI(uiFile=self.uifile, verbose=True)
        cmds.showWindow(self.window)


class tplink(object):
    use = None

    def __init__(self, pname, long, shipname='ship'):

        self.pname = pname
        self.long = long


        #self.abgle = abgle
        self.name = shipname
        self.eel = []
        self.vortname = 'vortX'
        tplink.use = self



    def create(self, *args):
        agle = None
        try:
            path = '|'.join(['box','getagle'])
            agle = float(cmds.textField(path,q=True,text=True))
        except:raise

        abgle = (math.pi / 180) * agle


        self.kkk =int( 180/agle)

        high = None
        try :
            high_path = '|'.join(['box','gethigh'])
            high = float(cmds.textField(high_path,q = True,text = True))
        except : raise



        pnumber = None
        try:
            pnumber_path = '|'.join(['box','getpnumber'])
            pnumber = int(cmds.textField(pnumber_path,q=True,text = True))
        except:raise


        for i in range(pnumber):
            self.eel.append((random.uniform(-1, 1), random.uniform(-1*high, high), random.uniform(-1 * self.long, self.long)))
        for i in range(self.kkk):
            for i in range(pnumber):
                cos = math.cos(abgle * i)
                sin = math.sin(abgle * i)
                self.eel.append((self.eel[i][0] * cos + self.eel[i][2] * sin, self.eel[i][1],
                                 self.eel[i][2] * cos - self.eel[i][0] * sin))

        cmds.particle(jbp=self.eel, n=self.name, c=1)

        cmds.setAttr("%sShape.particleRenderType" % self.name, 4)







    def link(self, *args):
        cmds.vortex(n=self.vortname, pos=(0, 0, 0), m=5, ay=1, att=1, mxd=-1, vsw=360, tsr=0.5)

        cmds.connectAttr('%s.outputForce[0]' % self.vortname, '%sShape.inputForce[0]' % self.name)
        cmds.connectAttr('%sShape.fieldData' % self.name, '%s.inputData[0]' % self.vortname)
        cmds.connectAttr('%sShape.ppFieldData[0]' % self.name, '%s.inputPPData[0]' % self.vortname)
opcc = tplink( pname='fut', long=20)
win = AR_poly(os.path.join(os.getenv('HOME'), 'poly.ui'))
win.create()
