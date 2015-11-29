class ConcreteOrb(object):

    def __init__(self):
        self.size = 0.6
        self.orbitscale = 10
        self.yearscale = 60
        self.dayscale = self.yearscale / 365.0 * 5

    def get_model(self):
        return "models/planet_sphere"

    def get_size(self):
        return self.size

    def get_texture(self):
        return "models/sun_1k_tex.jpg"

    def get_orbitscale(self):
        return self.orbitscale

    def get_yearscale(self):
        return self.yearscale

    def get_dayscale(self):
        return self.dayscale
