import unittest
from router import Router

class TestRouter(unittest.TestCase):

    def test_router_exists(self):
        router = Router()
        self.assertIsNotNone(router)

if __name__ == "__main__":
    unittest.main()
