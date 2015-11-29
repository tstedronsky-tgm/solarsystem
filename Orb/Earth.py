class Earth(object):

    def __init__(self, concrete_orb):
        self.concrete_orb = concrete_orb

    def get_model(self):
        return "models/planet_sphere"

    def get_size(self):
        return self.concrete_orb.get_size()

    def get_texture(self):
        return "models/earth_1k_tex.jpg"

    def get_orbitscale(self):
        return self.concrete_orb.get_orbitscale()

    def get_yearscale(self):
        return self.concrete_orb.get_yearscale()

    def get_dayscale(self):
        return self.concrete_orb.get_dayscale()