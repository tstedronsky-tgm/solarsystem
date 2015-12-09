class Space(object):
    """
    Weltraum
    """
    def __init__(self):
        """
        :return: void
        """
        self.model = "models/solar_sky_sphere"
        self.size = 40
        self.texture = "models/space_tex.jpg"

    def get_model(self):
        """
        :return: das Modell der Form des Himmelskoerpers
        """
        return self.model

    def get_size(self):
        """
        :return: Groesse des Himmelskoerpers
        """
        return self.size

    def get_texture(self):
        """
        :return: Die Texture des Himmelskoerpers
        """
        return self.texture;