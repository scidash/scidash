from __future__ import division
from sciunit import Test
from sciunit.scores import BooleanScore
from ..capabilities.__init__ import *

class SolarYear(Test):
	def __init__(self,solar_year_duration):
		self.solar_year_duration = solar_year_duration
		"""Length in days."""  

	required_capabilities = [HasSun]

	def error(self,predicted,observed):
		try:
			diff = predicted - observed
			return abs(diff)
		except TypeError:
			return None

	def run_test(self,model):
		days = model.solar_year_duration()
		error = self.error(model.solar_year_duration,self.solar_year_duration)
		score = error < 0.5
		return BooleanScore(score)

class OrbitalEccentricity(Test):
	def __init__(self,eccentricities):
		self.eccentricities = eccentricities
		"""Dictionary of observed orbital eccentricities for various planets.
		Units are arc-seconds.""" 

	required_capabilities = [HasPlanets]

	def error(self,predicted,observed):
		try:
			ratio = predicted/observed
			return 1-abs(ratio)
		except TypeError:
			return None

	def run_test(self,model):
		errors = [self.error(model.orbital_eccentricity(key),value) for key,value \
			in self.eccentricities.items()]
		score = all([error<0.05 for error in errors])
		return BooleanScore(score)

class StellarParallax(Test):
	def __init__(self,parallaxes):
		self.parallaxes = parallaxes
		"""Dictionary of observed parrallaxes for various stars.
		Units are arc-seconds.""" 

	required_capabilities = [HasStars]

	def error(self,predicted,observed):
		try:
			diff = predicted - observed
			return abs(diff/observed)
		except TypeError:
			return None

	def run_test(self,model):
		errors = [self.error(model.stellar_parallax(key),value) for key,value \
				  in self.parallaxes.items()]
		score = all([error<0.1 for error in errors])
		return BooleanScore(score)

class MoonCounts(Test):
	def __init__(self,moon_counts):
		self.moon_counts = moon_counts
		"""Dictionary of number of moons for each planet."""

	required_capabilities = [HasPlanets]

	def error(self,predicted,observed):
		try:
			return predicted - observed
		except TypeError:
			return None

	def run_test(self,model):
		errors = [self.error(model.num_moons(key),value) for key,value \
				  in self.moon_counts.items()]
		score = all([error==0 for error in errors])
		return BooleanScore(score)

class PerihelionPrecession(Test):
	def __init__(self,precession_rates):
		self.precession_rates = precession_rates
		"""Dictionary of perihelion precession rates for each planet.
		Units are arc-seconds per century."""
	
	required_capabilities = [HasSun,HasPlanets]

	def error(self,predicted,observed):
		try:
			ratio = predicted/observed
			return 1-abs(ratio)
		except TypeError:
			return None

	def run_test(self,model):
		errors = [self.error(model.perihelion_precession_rate(key),value) \
					for key,value in self.precession_rates.items()]
		score = all([error<0.01 for error in errors])
		return BooleanScore(score)

