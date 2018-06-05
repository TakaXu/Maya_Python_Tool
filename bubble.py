from pymel import  *


class jbface_popo(object):
    def create(self,*args):
        myem = emitter(dx=1, dy=0, dz=0, sp=15.0, pos=(1, 1, 1), type='dir', speedRandom=10, rate=0.7, n='myEmitter')

        mypa = particle(n='emittedParticles', c=0.5)
        mypa[0].particleRenderType.set(4)

        connectDynamic(mypa[0], em=myem)

        pname = 'emittedParticles'
        vname = 'zhongli'

        cmds.select(cl=True)
        mygr = gravity(name=vname, dy=1.0)

        connectDynamic(mypa,f = mygr)




popo = jbface_popo()
popo.create()
