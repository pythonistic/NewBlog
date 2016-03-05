import unittest

from test.ModelTest import ModelTest
from test.QueryTest import QueryTest

suite = []
classes = [ModelTest, QueryTest]
for cls in classes:
    suite.extend(unittest.TestLoader().loadTestsFromTestCase(cls))
test_suite = unittest.TestSuite(suite)
result = unittest.TestResult()
test_suite.run(result)
print result