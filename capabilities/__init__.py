from sciunit import Capability

class HasSun(Capability):
    def solar_days(self):
        raise NotImplemented("")

class HasStars(Capability):
    def stellar_parallax(self,star):
        raise NotImplemented("")

class HasPlanets(Capability):
    def orbital_eccentricity(self,planet):
        raise NotImplemented("")

    def num_moons(self,planet):
        raise NotImplemented("")

    def perihelion_precession_rate(self,planet):
        raise NotImplemented("")
