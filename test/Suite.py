import unittest

from test.ModelTest import ModelTest
from test.QueryTest import QueryTest
from test.NewBlogTest import NewBlogTest

suite = []
classes = [ModelTest, QueryTest, NewBlogTest]
for cls in classes:
    suite.extend(unittest.TestLoader().loadTestsFromTestCase(cls))
test_suite = unittest.TestSuite(suite)
result = unittest.TestResult()
test_suite.run(result)
print result