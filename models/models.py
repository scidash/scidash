"""This file contains all the model classes, i.e. model families, 
from which specific models are derived."""

import inspect

import quantities as pq

from sciunit import Model,PredictionError
import capabilities as cap


class _CosmoModel(Model):
    def solar_year_duration(self):
        raise PredictionError(self,self.curr_method(back=1))

    def orbital_eccentricity(self, planet):
        raise PredictionError(self,self.curr_method(back=1),planet=planet)
            
    def num_moons(self, planet):
        raise PredictionError(self,self.curr_method(back=1),planet=planet)

    def perihelion_precession_rate(self, planet):
        raise PredictionError(self,self.curr_method(back=1),planet=planet)

    def stellar_parallax(self, star):
        raise PredictionError(self,self.curr_method(back=1),star=star)


class Ptolemy(_CosmoModel,cap.HasSun,cap.HasPlanets):
    """Cladius Ptolemy, "The Almagest", 50 A.D."""
    
    def solar_year_duration(self):
        return 365 * pq.day

    def orbital_eccentricity(self, planet):
        return 0.0

    def num_moons(self, planet):
        if planet == 'Earth':
            return 1
        else:
            return _CosmoModel.num_moons(self,planet)

    def perihelion_precession_rate(self, planet):
        return 0.0 * pq.Hz


class Copernicus(Ptolemy,cap.HasStars):
    """Nicholas Copernicus, "De revolutionibus orbium coelestium", 1543"""
    
    def solar_year_duration(self):
        return 365.25 * pq.day

    def stellar_parallax(self, star):
        return 0.0 * pq.arcsecond
    

class Kepler(Copernicus):
    """Johannes Kepler, "Astronomia nova", 1609"""
    
    def solar_year_duration(self):
        return 365.25 * pq.day

    def orbital_eccentricity(self, planet):
        if planet == 'Mars':
            return 0.0934
        elif planet == 'Saturn':
            return 0.0541
        else:
            return _CosmoModel.orbital_eccentricity(self,planet)

    def num_moons(self, planet):
        if planet == 'Jupiter':
            return 4
        elif planet == 'Earth':
            return 1
        else:
            return _CosmoModel.num_moons(self,planet)

    def perihelion_precession_rate(self, planet):
        return 0.0 * pq.Hz


class Newton(Kepler):
    """Isaac Newton, "Philosophiae Naturalis Principia Mathematica", 1687"""
            
    def perihelion_precession_rate(self, planet):
        if planet == 'Mercury':
            return (531.63 * pq.arcsecond)/(100.0 * pq.year)
        else:
            return _CosmoModel.perihelion_precession_rate(self,planet)

    def stellar_parallax(self, star):
        if star == '61 Cygni':
            return 0.314 * pq.arcsecond
        elif star == 'Promixa Centauri':
            return 0.769 * pq.arcsecond
        else:
            raise _CosmoModel.stellar_parallax(self,star)


class Einstein(Newton):
    """Albert Einstein, "The Foundation of the General Theory of Relativity"
    Annalen der Physik, 49(7):769-822, 1916."""
    
    def perihelion_precession_rate(self, planet):
        if planet == 'Mercury':
            return (574.10 * pq.arcsecond)/(100.0 * pq.year)
        else:
            return _CosmoModel.perihelion_precession_rate(self,planet)

