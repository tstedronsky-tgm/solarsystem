import Orb

class OrbDecorator(Orb):

    def __init__(self, concrete_orb):
        self.concrete_orb = concrete_orb

    def get_model(self):
        return self.concrete_orb.get_model()

    def get_size(self):
        return self.concrete_orb.get_size()

    def get_texture(self):
        return self.concrete_orb.get_texture()
