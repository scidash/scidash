from . import tests as t
from . import observations as obs

# Initialize several tests
babylon = t.SolarYear({'duration':
                        obs.solar_year_duration},
                       name='Solar Year')

planets = ['Mars', 'Saturn']
brahe = [t.OrbitalEccentricity({'eccentricity':
                                (planet,obs.eccentricity[planet])
                               }, name='Ecc. %s' % planet) \
         for planet in planets]

stars = ['Promixa Centauri', '61 Cygni']
bessel = [t.StellarParallax({'parallax':
                             (star,obs.parallax[star])
                            }, name='Prlx. %s' % star) \
         for star in stars]

leverrier = t.PerihelionPrecession({'precession':
                                    ('Mercury',obs.precession['Mercury'])},
                                   name='Phln. Mercury')

#galileo = t.MoonCounts({'moons':
#                        ['Jupiter',obs.jupiter_moons]
#                       })

# Don't run any of these tests independenly of suites
tests = []