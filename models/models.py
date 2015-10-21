"""This file contains all the model classes, i.e. model families, 
from which specific models are derived."""

from sciunit import Model
from ..capabilities.__init__ import *

class Ptolemy(Model,HasSun,HasPlanets):
    """Cladius Ptolemy, "The Almagest", 50 A.D."""
    
    def solar_year_duration(self):
        return 365

    def orbital_eccentricity(self,planet):
        return 0.0

    def num_moons(self,planet):
        if planet == 'Earth':
            return 1
        else:
            return None

    def perihelion_precession_rate(self,planet):
        return 0.0

class Copernicus(Model,HasSun,HasPlanets,HasStars):
    """Nicholas Copernicus, "De revolutionibus orbium coelestium", 1543"""
    
    def solar_year_duration(self):
        return 365.25

    def orbital_eccentricity(self,planet):
        return 0.0

    def num_moons(self,planet):
        if planet == 'Earth':
            return 1
        else:
            return None

    def perihelion_precession_rate(self,planet):
        return 0.0

    def stellar_parallax(self,star):
        return 0.0
    
class Kepler(Model,HasSun,HasStars,HasPlanets):
    """Johannes Kepler, "Astronomia nova", 1609"""
    
    def solar_year_duration(self):
        return 365.25

    def orbital_eccentricity(self,planet):
        if planet == 'Mars':
            return 0.09341233
        else:
            return None

    def num_moons(self,planet):
        if planet == 'Jupiter':
            return 4
        elif planet == 'Earth':
            return 1
        else:
            return None

    def perihelion_precession_rate(self,planet):
        return 0.0

    def stellar_parallax(self,star):
        return 0.0

class Newton(Model,HasSun,HasStars,HasPlanets):
    """Isaac Newton, "Philosophiae Naturalis Principia Mathematica", 1687"""
    
    def solar_year_duration(self):
        return 365.25

    def orbital_eccentricity(self,planet):
        if planet == 'Mars':
            return 0.09341233
        else:
            return None
            
    def num_moons(self,planet):
        if planet == 'Jupiter':
            return 4
        elif planet == 'Earth':
            return 1
        else:
            return None

    def perihelion_precession_rate(self,planet):
        if planet == 'Mercury':
            return 531.63
        else:
            return None

    def stellar_parallax(self,star):
        if star == '61 Cygni':
            return 0.3136
        else:
            return None

class Einstein(Model,HasSun,HasStars,HasPlanets):
    """Albert Einstein, "The Foundation of the General Theory of Relativity"
    Annalen der Physik, 49(7):769-822, 1916."""
    
    def solar_year_duration(self):
        return 365.25

    def orbital_eccentricity(self,planet):
        if planet == 'Mars':
            return 0.09341233
        else:
            return None
            
    def num_moons(self,planet):
        if planet == 'Jupiter':
            return 4
        elif planet == 'Earth':
            return 1
        else:
            return None

    def perihelion_precession_rate(self,planet):
        if planet == 'Mercury':
            return 574.10
        else:
            return None

    def stellar_parallax(self,star):
        if star == '61 Cygni':
            return 0.3136
        else:
            return None

            