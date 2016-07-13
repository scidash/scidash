"""Observations (experimental facts) used to parameterize tests"""

import quantities as pq

solar_year_duration = 365.25 * pq.day

# Orbital eccentricities
eccentricity = {'Mars':0.093, 
                'Saturn':0.0541506,
               }

# Perihelion precessions
precession = {'Mercury':(600 * pq.arcsecond)/(100.0 * pq.year),
             }

# Stellar parallaxes
parallax = {'61 Cygni':0.3136 * pq.arcsecond, 
            # Friedrich Bessel in 1838 using a heliometer.
            # Bessel, Friedrich
            # "Bestimmung der Entfernung des 61sten Sterns des Schwans"
            # Astronomische Nachrichten, 16, 65-96 (1838)
            'Promixa Centauri':0.7687 * pq.arcsecond,
           }