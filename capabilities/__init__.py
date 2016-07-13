from sciunit import Capability


class HasSun(Capability):
    def solar_days(self):
        return self.unimplemented()


class HasStars(Capability):
    def stellar_parallax(self,star):
        return self.unimplemented()


class HasPlanets(Capability):
    def orbital_eccentricity(self,planet):
        return self.unimplemented()

    def num_moons(self,planet):
        return self.unimplemented()

    def perihelion_precession_rate(self,planet):
        return self.unimplemented()
