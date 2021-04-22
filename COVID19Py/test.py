import unittest
import COVID19Py

class COVID19PyTest(unittest.TestCase):
  def test_getLatest(self):
    actual = "%s" % (COVID19Py.COVID19().getLatest())
    expected = "{'confirmed': 142945718, 'deaths': 3043946, 'recovered': 18246755}"
    self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()