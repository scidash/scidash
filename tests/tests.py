from __future__ import division

import quantities as pq

import sciunit
from sciunit.scores import BooleanScore, RatioScore
from sciunit.converters import RangeToBoolean
import capabilities as cap


class _CosmoTest(sciunit.Test):
    score_type = BooleanScore
    primary_key = None
    units = pq.dimensionless

    def validate_observation(self, observation):
        """Observation should be a dictionary of containing the length of a 
        a solar year in units with the dimension of time.""" 
        key = self.primary_key
        assert key in observation, "%s not found in %s test observation" % \
                                   (key,self.__class__.__name__)
        value = observation[key]
        if type(observation[key]) is tuple:
            value = value[1]
        if self.units is not pq.dimensionless:
            assert isinstance(value,pq.Quantity), \
                ("Key '%s' of observation for '%s' test is not an instance of "
                 "quantities.Quantity" ) % (key,self.__class__.__name__)
            assert value.simplified.units == \
                   self.units.simplified.units, \
                ("Key '%s' of observation for '%s' test does not have units of "
                 "%s" % (key,self.__class__.__name__,self.units))
        
    def compute_score(self, observation, prediction, verbose=True):
        key = self.primary_key
        obs,pred = observation[key],prediction[key]
        if isinstance(self,_CosmoEntityTest):
            obs = obs[1]
        error = RatioScore.compute(obs,pred)
        score = RangeToBoolean(0.9,1.1).convert(error)
        return score


class _CosmoEntityTest(_CosmoTest):
    entity_type = None

    def validate_observation(self, observation):
        super(_CosmoEntityTest,self).validate_observation(observation)
        assert type(observation[self.primary_key]) is tuple, \
         "Observation for key %s must be a (%s,value) tuple" % \
            (self.entity_type,self.primary_key)


class SolarYear(_CosmoTest):
    required_capabilities = [cap.HasSun]
    primary_key = 'duration'
    units = pq.s

    def generate_prediction(self, model, verbose=True):
        days = model.solar_year_duration()
        return {self.primary_key:days}


class OrbitalEccentricity(_CosmoEntityTest):
    required_capabilities = [cap.HasPlanets]
    primary_key = 'eccentricity'
    entity_type = 'planet'
    units = pq.dimensionless

    def generate_prediction(self, model, verbose=True):
        planet,value = self.observation[self.primary_key]
        eccentricity = model.orbital_eccentricity(planet)
        return {self.primary_key:eccentricity}


class StellarParallax(_CosmoEntityTest):
    required_capabilities = [cap.HasStars]
    primary_key = 'parallax'
    units = pq.arcsecond
    entity_type = 'star'

    def generate_prediction(self, model, verbose=True):
        star,value = self.observation[self.primary_key]
        parallax = model.stellar_parallax(star)
        return {self.primary_key:parallax}


class PerihelionPrecession(_CosmoEntityTest):
    required_capabilities = [cap.HasSun,cap.HasPlanets]
    primary_key = 'precession'
    entity_type = 'planet'
    units = pq.Hz

    def generate_prediction(self, model, verbose=True):
        planet,value = self.observation[self.primary_key]
        precession = model.perihelion_precession_rate(planet)
        return {self.primary_key:precession}


'''
class MoonCounts(CosmoTest):
    def __init__(self, moon_counts):
        self.moon_counts = moon_counts
        """Dictionary of number of moons for each planet."""

    required_capabilities = [cap.HasPlanets]

    def error(self, predicted, observed):
        try:
            return predicted - observed
        except TypeError:
            return None

    def run_test(self, model):
        errors = [self.error(model.num_moons(key),value) for key,value \
                  in self.moon_counts.items()]
        score = all([error==0 for error in errors])
        return BooleanScore(score)
'''
