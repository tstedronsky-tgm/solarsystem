from direct.showbase.ShowBase import ShowBase

from Orb.concreteOrb import ConcreteOrb
from Orb.deathstar import DeathStar
from Orb.earth import Earth
from Orb.mars import Mars
from Orb.mercury import Mercury
from Orb.sun import Sun
from Orb.space import Space
from Orb.venus import Venus
from Orb.moon import Moon

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

        camera.setPos(0, 0, 45)
        camera.setHpr(0, -90, 0)

        #konkreter Himmelskoerper:
        self.co = ConcreteOrb()

        #dekorierte Himmelskoerper:
        self.s = Sun(self.co)
        self.merc = Mercury(self.co)
        self.v = Venus(self.co)
        self.m = Mars(self.co)
        self.e = Earth(self.co)
        self.mo = Moon(self.co)
        self.ds = DeathStar(self.co)

        self.loadPlanets()
        self.rotatePlanets()

    def loadPlanets(self):

        #Festlegung der Orbits der einzelnen Planeten:
        self.orbit_root_mercury = render.attachNewNode('orbit_root_mercury')
        self.orbit_root_venus = render.attachNewNode('orbit_root_venus')
        self.orbit_root_mars = render.attachNewNode('orbit_root_mars')
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

        # Erstellung von Mars
        self.mars = loader.loadModel(self.m.get_model())
        self.mars_tex = loader.loadTexture(self.m.get_texture())
        self.mars.setTexture(self.mars_tex, 1)
        self.mars.reparentTo(self.orbit_root_mars)
        self.mars.setPos(self.m.get_orbitscale(), 0, 0)
        self.mars.setScale(self.m.get_size())

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

    def rotatePlanets(self):

        self.day_period_sun = self.sun.hprInterval(20, (360, 0, 0))

        self.orbit_period_mercury = self.orbit_root_mercury.hprInterval(
            (self.merc.get_yearscale()), (360, 0, 0))
        self.day_period_mercury = self.mercury.hprInterval(
            (self.merc.get_dayscale()), (360, 0, 0))

        self.orbit_period_venus = self.orbit_root_venus.hprInterval(
            (self.v.get_yearscale()), (360, 0, 0))
        self.day_period_venus = self.venus.hprInterval(
            (self.v.get_dayscale()), (360, 0, 0))

        self.orbit_period_earth = self.orbit_root_earth.hprInterval(
            self.e.get_yearscale(), (360, 0, 0))
        self.day_period_earth = self.earth.hprInterval(
            self.e.get_dayscale(), (360, 0, 0))

        self.orbit_period_moon = self.orbit_root_moon.hprInterval(
            (self.mo.get_yearscale()), (360, 0, 0))
        self.day_period_moon = self.moon.hprInterval(
            (self.mo.get_dayscale()), (360, 0, 0))

        self.orbit_period_mars = self.orbit_root_mars.hprInterval(
            (self.m.get_yearscale()), (360, 0, 0))
        self.day_period_mars = self.mars.hprInterval(
            (self.m.get_dayscale()), (360, 0, 0))

        self.day_period_sun.loop()
        self.orbit_period_mercury.loop()
        self.day_period_mercury.loop()
        self.orbit_period_venus.loop()
        self.day_period_venus.loop()
        self.orbit_period_earth.loop()
        self.day_period_earth.loop()
        self.orbit_period_moon.loop()
        self.day_period_moon.loop()
        self.orbit_period_mars.loop()
        self.day_period_mars.loop()

w = World()
base.run()
