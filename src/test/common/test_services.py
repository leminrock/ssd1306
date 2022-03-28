import unittest
import time
from common import services as serv


class TestEntity(unittest.TestCase):

    def test_is_active(self):
        self.assertEqual(serv.is_active('rock_serverweb'), False)
        self.assertEqual(serv.is_active('rock_puredata'), False)
        self.assertEqual(serv.is_active('rock_jackd'), False)
        self.assertEqual(serv.is_active('NetworkManager'), True)
        self.assertEqual(serv.is_active('openvpn'), True)

    def test_systemctl(self):
        self.assertEqual(serv.systemctl('rock_serverweb', serv.START), 0)

    def test_is_active2(self):
        time.sleep(2)
        self.assertEqual(serv.is_active('rock_serverweb'), True)

    def test_systemctl(self):
        self.assertNotEqual(serv.systemctl('rock_serverweb', serv.STOP), 0)

    def test_is_active3(self):
        time.sleep(2)
        self.assertEqual(serv.is_active('rock_serverweb'), False)


if __name__ == '__main__':
    unittest.main()
