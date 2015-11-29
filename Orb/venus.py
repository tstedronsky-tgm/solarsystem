class Venus(object):

    def __init__(self, concrete_orb):
        self.concrete_orb = concrete_orb

    def get_model(self):
        return "models/planet_sphere"

    def get_size(self):
        return self.concrete_orb.get_size() * 0.932

    def get_texture(self):
        return "models/venus_1k_tex.jpg"

    def get_orbitscale(self):
        return self.concrete_orb.get_orbitscale() * 0.72

    def get_yearscale(self):
        return self.concrete_orb.get_yearscale() * 0.615

    def get_dayscale(self):
        return self.concrete_orb.get_dayscale() * 243