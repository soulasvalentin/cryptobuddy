# testing docs: https://realpython.com/python-testing/

import mock
import unittest

from shared import table_service
from shared import version

class TestVersion(unittest.TestCase):
    def test_version_non_empty(self):
        self.assertIsNotNone(version.current_version, 'Version is not defined')
        
    def test_version_format(self):
        self.assertRegex(version.current_version, r'^[0-9]*\.[0-9]*\.[0-9]*$', 'Version has incorrect format')

if __name__ == '__main__':
    unittest.main()