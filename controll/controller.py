from direct.showbase.ShowBase import ShowBase

from orb.concreteOrb import ConcreteOrb
from orb.deathstar import DeathStar
from orb.earth import Earth
from orb.jupiter import Jupiter
from orb.mercury import Mercury
from orb.sun import Sun
from orb.space import Space
from orb.venus import Venus
from orb.moon import Moon

base = ShowBase()

from panda3d.core import *
from direct.gui.DirectGui import *
import sys


class World(object):

    def __init__(self):
        self.title = OnscreenText(
            text="Solarsystem - von Thomas Stedronsky und Simon Wortha",
            parent=base.a2dBottomRight, align=TextNode.A_right,
            style=1, fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.07)

        base.setBackgroundColor(0, 0, 0)

        base.disableMouse()

        props = WindowProperties()
        props.setTitle('Solarsystem')
        base.win.requestProperties(props)

        base.camera.setPos(0, 0, 70)
        base.camera.setHpr(0, -90, 0)

        # konkreter Himmelskoerper:
        self.co = ConcreteOrb()

        # dekorierte Himmelskoerper:
        self.s = Sun(self.co)
        self.merc = Mercury(self.co)
        self.v = Venus(self.co)
        self.j = Jupiter(self.co)
        self.e = Earth(self.co)
        self.mo = Moon(self.co)
        self.ds = DeathStar(self.co)

        self.showHelp = False
        self.textureOn = True

        self.loadPlanets()
        self.rotatePlanets(1.0)
        self.simRunning = True

        #Erstellen der Events
        base.accept("p", self.handlePause)
        base.accept("o", self.handleCameraTopView)
        base.accept("i", self.handleCamera1)
        base.accept("u", self.handleCamera2)
        base.accept("t", self.textureToggle)
        base.accept("1", self.slower)
        base.accept("2", self.faster)
        base.accept("h", self.showHelpView)
        base.accept("escape", sys.exit)

    def genLabelText(self, text, i):
        return OnscreenText(text=text, pos=(0.06, -.06 * (i + 0.5)), fg=(1, 1, 1, 1),
                            parent=base.a2dTopLeft,align=TextNode.ALeft, scale=.05)

    def helpOn(self):
        self.slowerEvent = self.genLabelText("[1]\tLangsamer", 1)
        self.fasterEvent = self.genLabelText("[2]\tSchneller", 2)
        self.textureEvent = self.genLabelText("[T]\tTexture an/aus", 3)
        self.cameraoption1 = self.genLabelText("[O]\tTop View", 4)
        self.cameraoption2 = self.genLabelText("[I]\tKameramode XY", 5)
        self.cameraoption3 = self.genLabelText("[U]\tKameramode Ultra", 6)
        self.pause = self.genLabelText("[P]\tPause", 7)
        self.showHelp = True

    def helpOff(self):
        self.slowerEvent.destroy()
        self.fasterEvent.destroy()
        self.textureEvent.destroy()
        self.cameraoption1.destroy()
        self.cameraoption2.destroy()
        self.cameraoption3.destroy()
        self.pause.destroy()
        self.showHelp = False

    def loadPlanets(self):

        #Festlegung der Orbits der einzelnen Planeten:
        self.orbit_root_mercury = render.attachNewNode('orbit_root_mercury')
        self.orbit_root_venus = render.attachNewNode('orbit_root_venus')
        self.orbit_root_jupiter = render.attachNewNode('orbit_root_jupiter')
        self.orbit_root_earth = render.attachNewNode('orbit_root_earth')

        self.orbit_root_moon = (
            self.orbit_root_earth.attachNewNode('orbit_root_moon'))

        #zuerst wird dir Hintegrund erstellt:
        space = Space()
        self.sky = loader.loadModel(space.get_model())
        self.sky.reparentTo(render)
        self.sky.setScale(space.get_size())
        self.sky_tex = loader.loadTexture(space.get_texture())
        self.sky.setTexture(self.sky_tex, 1)

        # Erstellung der Sonne:
        self.sun = loader.loadModel(self.s.get_model())
        self.sun.reparentTo(render)
        self.sun_tex = loader.loadTexture(self.s.get_texture())
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.setScale(self.s.get_size())

        # Erstellung von Merkur
        self.mercury = loader.loadModel(self.merc.get_model())
        self.mercury_tex = loader.loadTexture(self.merc.get_texture())
        self.mercury.setTexture(self.mercury_tex, 1)
        self.mercury.reparentTo(self.orbit_root_mercury)
        self.mercury.setPos(self.merc.get_orbitscale(), 0, 0)
        self.mercury.setScale(self.merc.get_size())

        # Erstellung der Venus
        self.venus = loader.loadModel(self.v.get_model())
        self.venus_tex = loader.loadTexture(self.v.get_texture())
        self.venus.setTexture(self.venus_tex, 1)
        self.venus.reparentTo(self.orbit_root_venus)
        self.venus.setPos(self.v.get_orbitscale(), 0, 0)
        self.venus.setScale(self.v.get_size())

        # Erstellung von Jupiter
        self.jupiter = loader.loadModel(self.j.get_model())
        self.jupiter_tex = loader.loadTexture(self.j.get_texture())
        self.jupiter.setTexture(self.jupiter_tex, 1)
        self.jupiter.reparentTo(self.orbit_root_jupiter)
        self.jupiter.setPos(self.j.get_orbitscale(), 0, 0)
        self.jupiter.setScale(self.j.get_size())

         # Erstellung des Todessterns
        self.deathstar = loader.loadModel(self.ds.get_model())
        self.deathstar.reparentTo(render)
        self.deathstar_tex = loader.loadTexture(self.ds.get_texture())
        self.deathstar.setTexture(self.deathstar_tex, 1)
        self.deathstar.setScale(self.ds.get_size())
        self.deathstar.setPos(self.ds.get_orbitscale(), 0, 0)

        # Erstellung der Erde
        self.earth = loader.loadModel(self.e.get_model())
        self.earth_tex = loader.loadTexture(self.e.get_texture())
        self.earth.setTexture(self.earth_tex, 1)
        self.earth.reparentTo(self.orbit_root_earth)
        self.earth.setScale(self.e.get_size())
        self.earth.setPos(self.e.get_orbitscale(), 0, 0)

        # Jetzt muss das Zentrum des Mondes eingerichtet werden welches die Erde ist
        self.orbit_root_moon.setPos(self.e.get_orbitscale(), 0, 0)

        # Erstellen des Mondes
        self.moon = loader.loadModel(self.mo.get_model())
        self.moon_tex = loader.loadTexture(self.mo.get_texture())
        self.moon.setTexture(self.moon_tex, 1)
        self.moon.reparentTo(self.orbit_root_moon)
        self.moon.setScale(self.mo.get_size())
        self.moon.setPos(self.mo.get_orbitscale(), 0, 0)

    def rotatePlanets(self, mod):

        self.day_period_sun = self.sun.hprInterval(20, (360, 0, 0))

        self.orbit_period_mercury = self.orbit_root_mercury.hprInterval(
            (self.merc.get_yearscale()*mod), (360, 0, 0))
        self.day_period_mercury = self.mercury.hprInterval(
            (self.merc.get_dayscale()*mod), (360, 0, 0))

        self.orbit_period_venus = self.orbit_root_venus.hprInterval(
            (self.v.get_yearscale()*mod), (360, 0, 0))
        self.day_period_venus = self.venus.hprInterval(
            (self.v.get_dayscale()*mod), (360, 0, 0))

        self.orbit_period_earth = self.orbit_root_earth.hprInterval(
            (self.e.get_yearscale()*mod), (360, 0, 0))
        self.day_period_earth = self.earth.hprInterval(
            (self.e.get_dayscale()*mod), (360, 0, 0))

        self.orbit_period_moon = self.orbit_root_moon.hprInterval(
            (self.mo.get_yearscale()*mod), (360, 0, 0))
        self.day_period_moon = self.moon.hprInterval(
            (self.mo.get_dayscale()*mod), (360, 0, 0))

        self.orbit_period_jupiter = self.orbit_root_jupiter.hprInterval(
            (self.j.get_yearscale()*mod), (360, 0, 0))
        self.day_period_jupiter = self.jupiter.hprInterval(
            (self.j.get_dayscale()*mod), (360, 0, 0))

        self.day_period_sun.loop()
        self.orbit_period_mercury.loop()
        self.day_period_mercury.loop()
        self.orbit_period_venus.loop()
        self.day_period_venus.loop()
        self.orbit_period_earth.loop()
        self.day_period_earth.loop()
        self.orbit_period_moon.loop()
        self.day_period_moon.loop()
        self.orbit_period_jupiter.loop()
        self.day_period_jupiter.loop()

    def handlePause(self):
        if self.simRunning:
            print("Pausing Simulation")
            # Sun
            if self.day_period_sun.isPlaying():
                self.togglePlanet("Sun", self.day_period_sun, None)
            if self.day_period_mercury.isPlaying():
                self.togglePlanet("Mercury", self.day_period_mercury,
                                  self.orbit_period_mercury)
            # Venus
            if self.day_period_venus.isPlaying():
                self.togglePlanet("Venus", self.day_period_venus,
                                  self.orbit_period_venus)
            # Earth and moon
            if self.day_period_earth.isPlaying():
                self.togglePlanet("Earth", self.day_period_earth,
                                  self.orbit_period_earth)
                self.togglePlanet("Moon", self.day_period_moon,
                                  self.orbit_period_moon)
            # Jupiter
            if self.day_period_jupiter.isPlaying():
                self.togglePlanet("jupiter", self.day_period_jupiter,
                                  self.orbit_period_jupiter)
        else:
            # Unpause
            print("Resuming Simulation")
            if not self.day_period_sun.isPlaying():
                self.togglePlanet("Sun", self.day_period_sun, None)
            if not self.day_period_mercury.isPlaying():
                self.togglePlanet("Mercury", self.day_period_mercury,
                                  self.orbit_period_mercury)
            if not self.day_period_venus.isPlaying():
                self.togglePlanet("Venus", self.day_period_venus,
                                  self.orbit_period_venus)
            if not self.day_period_earth.isPlaying():
                self.togglePlanet("Earth", self.day_period_earth,
                                  self.orbit_period_earth)
                self.togglePlanet("Moon", self.day_period_moon,
                                  self.orbit_period_moon)
            if not self.day_period_jupiter.isPlaying():
                self.togglePlanet("jupiter", self.day_period_jupiter,
                                  self.orbit_period_jupiter)

        # toggle self.simRunning
        self.simRunning = not self.simRunning

    def togglePlanet(self, planet, day, orbit=None, text=None):
        if day.isPlaying():
            state = " [PAUSED]"
        else:
            state = " [RUNNING]"
        self.toggleInterval(day)
        if orbit:
            self.toggleInterval(orbit)


    def toggleInterval(self, interval):
        if interval.isPlaying():
            interval.pause()
        else:
            interval.resume()

    def handleCamera1(self):
        base.enableMouse()
        base.useDrive()
        #setzt Kamera auf gewuenschte Ausgangsposition
        base.drive.node().setPos(0, -40, 0)

    def handleCamera2(self):
        base.enableMouse()
        base.useTrackball()
        #setzt Kamera auf gewuenschte Ausgangsposition
        base.trackball.node().setPos(0, 40, 0)

    def handleCameraTopView(self):
        base.disableMouse()
        base.camera.setPos(0, 0, 70)
        base.camera.setHpr(0, -90, 0)

    def showHelpView(self):
        print "help"
        if self.showHelp == True:
            self.helpOff()
        elif self.showHelp == False:
            self.helpOn()

    def slower(self):
        if(self.orbit_period_earth.getPlayRate()-1 == 0):
            self.orbit_period_earth.setPlayRate(-1)
            self.day_period_earth.setPlayRate(-1)
            self.orbit_period_mercury.setPlayRate(-1)
            self.day_period_mercury.setPlayRate(-1)
            self.orbit_period_venus.setPlayRate(-1)
            self.day_period_venus.setPlayRate(-1)
            self.orbit_period_jupiter.setPlayRate(-1)
            self.day_period_jupiter.setPlayRate(-1)
            self.orbit_period_moon.setPlayRate(-1)
            self.day_period_moon.setPlayRate(-1)
            self.day_period_sun.setPlayRate(-1)
        else:
            self.orbit_period_earth.setPlayRate(self.orbit_period_earth.getPlayRate()-1)
            self.day_period_earth.setPlayRate(self.day_period_earth.getPlayRate()-1)
            self.orbit_period_mercury.setPlayRate(self.orbit_period_mercury.getPlayRate()-1)
            self.day_period_mercury.setPlayRate(self.day_period_mercury.getPlayRate()-1)
            self.orbit_period_venus.setPlayRate(self.orbit_period_venus.getPlayRate()-1)
            self.day_period_venus.setPlayRate(self.day_period_venus.getPlayRate()-1)
            self.orbit_period_jupiter.setPlayRate(self.orbit_period_jupiter.getPlayRate()-1)
            self.day_period_jupiter.setPlayRate(self.day_period_jupiter.getPlayRate()-1)
            self.orbit_period_moon.setPlayRate(self.orbit_period_moon.getPlayRate()-1)
            self.day_period_moon.setPlayRate(self.day_period_moon.getPlayRate()-1)
            self.day_period_sun.setPlayRate(self.day_period_sun.getPlayRate()-1)

    def faster(self):
        if(self.orbit_period_earth.getPlayRate()+1 == 0):
            self.orbit_period_earth.setPlayRate(+1)
            self.day_period_earth.setPlayRate(+1)
            self.orbit_period_mercury.setPlayRate(+1)
            self.day_period_mercury.setPlayRate(+1)
            self.orbit_period_venus.setPlayRate(+1)
            self.day_period_venus.setPlayRate(+1)
            self.orbit_period_jupiter.setPlayRate(+1)
            self.day_period_jupiter.setPlayRate(+1)
            self.orbit_period_moon.setPlayRate(+1)
            self.day_period_moon.setPlayRate(+1)
            self.day_period_sun.setPlayRate(+1)
        else:
            self.orbit_period_earth.setPlayRate(self.orbit_period_earth.getPlayRate()+1)
            self.day_period_earth.setPlayRate(self.day_period_earth.getPlayRate()+1)
            self.orbit_period_mercury.setPlayRate(self.orbit_period_mercury.getPlayRate()+1)
            self.day_period_mercury.setPlayRate(self.day_period_mercury.getPlayRate()+1)
            self.orbit_period_venus.setPlayRate(self.orbit_period_venus.getPlayRate()+1)
            self.day_period_venus.setPlayRate(self.day_period_venus.getPlayRate()+1)
            self.orbit_period_jupiter.setPlayRate(self.orbit_period_jupiter.getPlayRate()+1)
            self.day_period_jupiter.setPlayRate(self.day_period_jupiter.getPlayRate()+1)
            self.orbit_period_moon.setPlayRate(self.orbit_period_moon.getPlayRate()+1)
            self.day_period_moon.setPlayRate(self.day_period_moon.getPlayRate()+1)
            self.day_period_sun.setPlayRate(self.day_period_sun.getPlayRate()+1)

    def textureToggle(self):
        if(self.textureOn == True):
            self.earth.setTextureOff()
            self.deathstar.setTextureOff()
            self.moon.setTextureOff()
            self.mercury.setTextureOff()
            self.jupiter.setTextureOff()
            self.sun.setTextureOff()
            self.venus.setTextureOff()
            self.textureOn = False
        else:
            self.earth.setTexture(self.earth_tex)
            self.deathstar.setTexture(self.deathstar_tex)
            self.moon.setTexture(self.moon_tex)
            self.mercury.setTexture(self.mercury_tex)
            self.jupiter.setTexture(self.jupiter_tex)
            self.sun.setTexture(self.sun_tex)
            self.venus.setTexture(self.venus_tex)
            self.textureOn = True

w = World()
base.run()
