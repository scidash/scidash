import sys

from sciunit import TestSuite

import tests as t # 'tests' should be on path if run from 'sciunit run'

babylon = TestSuite(tests=t.babylon, name='Babylon')
brahe = TestSuite(tests=t.brahe, name='Brahe')
bessel = TestSuite(tests=t.bessel, name='Bessel')
leverrier = TestSuite(tests=t.leverrier, name='Leverrier')

# Set these test suites to be applied to all models
suites = [babylon, brahe, bessel, leverrier]
