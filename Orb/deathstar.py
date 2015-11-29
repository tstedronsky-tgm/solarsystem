class DeathStar(object):

    def __init__(self, concrete_orb):
        self.concrete_orb = concrete_orb

    def get_model(self):
        return "models/planet_sphere"

    def get_size(self):
        return self.concrete_orb.get_size() * 1.2

    def get_texture(self):
        return "models/deathstar.jpg"

    def get_orbitscale(self):
        return 12

    # def get_yearscale(self):
    #     return self.concrete_orb.get_yearscale()
    #
    # def get_dayscale(self):
    #     return self.concrete_orb.get_dayscale()