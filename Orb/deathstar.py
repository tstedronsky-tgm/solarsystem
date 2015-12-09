class DeathStar(object):
    """
    Todesstern
    """

    def __init__(self, concrete_orb):
        """
        :param concrete_orb: Himmelskoerper der dekoriert wird
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
        return self.concrete_orb.get_size() * 1.2

    def get_texture(self):
        """
        :return: Die Texture des Himmelskoerpers
        """
        return "models/deathstar.jpg"

    def get_orbitscale(self):
        """
        :return: Die Entfernung zur Sonne
        """
        return 12.5