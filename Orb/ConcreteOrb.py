class ConcreteOrb(object):
    """
    Konkreter Himmelskoerper
    """

    def __init__(self):
        """
        :return: void
        """
        self.size = 0.6
        self.orbitscale = 10
        self.yearscale = 60
        self.dayscale = self.yearscale / 365.0 * 5

    def get_model(self):
        """
        :return: das Modell der Form des Himmelskoerpers
        """
        return "models/planet_sphere"

    def get_size(self):
        """
        :return: Groesse des Himmelskoerpers
        """
        return self.size

    def get_texture(self):
        """
        :return: Die Texture des Himmelskoerpers
        """
        return "models/sun_1k_tex.jpg"

    def get_orbitscale(self):
        """
        :return: Die Entfernung zur Sonne
        """
        return self.orbitscale

    def get_yearscale(self):
        """
        :return: Wie schnell sich der Himmelskoerper um die Sonne bewegt
        """
        return self.yearscale

    def get_dayscale(self):
        """
        :return: Wie schnell der Himmelskoeper rotiert
        """
        return self.dayscale
