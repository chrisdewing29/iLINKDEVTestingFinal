import unittest

from Tests.iLinkDevTesting import MainTest
# Get all tests from classes
MainTest = unittest.TestLoader().loadTestsFromTestCase(MainTest)

# Create a test suite combining all test cases
regressionSuite = unittest.TestSuite()
regressionSuite.addTest(MainTest)

smokeSuite = unittest.TestSuite()
smokeSuite.addTest(MainTest)

# Test runner
unittest.TextTestRunner(verbosity=2).run(smokeSuite)