import maya.cmds as cmds;

mygrid = cmds.polyPlane(name='emi')
cmds.setAttr("emi.rotateX",-45)
cmds.setAttr("emi.translateZ",10)
cmds.setAttr("emi.translateY",10)
cmds.setAttr("emi.scaleX",30)
cmds.setAttr("emi.scaleY",20)
cmds.setAttr("emi.scaleZ",20)

cmds.select('emi')
myem = cmds.emitter(name = 'myEmitter',speed = 30,speedRandom = 10,rate = 0.005)
mypa = cmds.particle(name = 'myParticle')
cmds.connectDynamic(mypa[0],em = myem)

cmds.setAttr("myEmitter.emitterType",2)

mygr = cmds.gravity(name = 'myGravity')
cmds.connectDynamic(mypa,f = mygr)
cmds.setAttr("myGravity.magnitude",4)

cmds.select('pCone1','myParticle')
cmds.particleInstancer("myParticle",object = 'pCone1',aimDirection = 'velocity')

cmds.select('myParticle')
myem2 = cmds.emitter(name = 'trailEmitter',rate = 1000,spread = 1,speed = 4,speedRandom = 3)
mypa2 = cmds.particle(name = 'trailParticle')
cmds.connectDynamic(mypa2[0],em = myem2)

cmds.setAttr("trailEmitter.emitterType",0)
cmds.setAttr("trailParticleShape.lifespanMode",2)
cmds.setAttr("trailParticleShape.lifespan",0.3)
cmds.setAttr("trailParticleShape.lifespanRandom",0.2)
cmds.setAttr("trailParticleShape.particleRenderType",8)



