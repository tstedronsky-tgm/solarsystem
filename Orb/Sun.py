class Sun(object):

    def __init__(self, concrete_orb):
        self.concrete_orb = concrete_orb

    def get_model(self):
        return "models/planet_sphere"

    def get_size(self):
        return self.concrete_orb.get_size() * 2

    def get_texture(self):
        return "models/sun_1k_tex.jpg"
