class Space(object):
    def __init__(self):

        self.model = "models/solar_sky_sphere"
        self.size = 40
        self.texture = "models/stars_1k_tex.jpg"

    def get_model(self):
        return self.model

    def get_size(self):
        return self.size

    def get_texture(self):
        return self.texture;