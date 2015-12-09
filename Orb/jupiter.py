class Jupiter(object):
    """
    Jupiter
    """

    def __init__(self, concrete_orb):
        """
        :param concrete_orb:
        :return: void
        """
        self.concrete_orb = concrete_orb

    def get_model(self):
        """
        :return: das Modell der Form des Himmelskoerpers
        """
        return "models/planet_sphere"

    def get_size(self):
        """
        :return: Groesse des Himmelskoerpers
        """
        return self.concrete_orb.get_size() * 1.8

    def get_texture(self):
        """
        :return: Die Texture des Himmelskoerpers
        """
        return "models/jupiter_1k_tex.jpg"

    def get_orbitscale(self):
        """
        :return: Die Entfernung zur Sonne
        """
        return self.concrete_orb.get_orbitscale() * 1.52

    def get_yearscale(self):
        """
        :return: Wie schnell sich der Himmelskoerper um die Sonne bewegt
        """
        return self.concrete_orb.get_yearscale() * 1.881

    def get_dayscale(self):
        """
        :return: Wie schnell der Himmelskoeper rotiert
        """
        return self.concrete_orb.get_dayscale() * 1.03