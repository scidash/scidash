from sciunit import TestSuite
from ..tests.__init__ import *

suites = []

babylon = SolarYear(365.0)

brahe = OrbitalEccentricity({'Mars':0.093})

galileo = MoonCounts({'Jupiter':4})

bessel = StellarParallax({'61 Cygni':0.3136})
"""Friedrich Bessel in 1838 for the star 61 Cygni using a heliometer.
Bessel, Friedrich
"Bestimmung der Entfernung des 61sten Sterns des Schwans"
Astronomische Nachrichten, 16, 65-96 (1838)"""

leverrier = PerihelionPrecession({'Mercury':574.10})

legends = TestSuite([babylon,brahe,galileo,bessel,leverrier])

suites.append(legends)

