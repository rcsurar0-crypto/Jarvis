import unittest
from master_agent import MasterAgent

class TestMasterAgent(unittest.TestCase):

    def test_pipeline(self):
        agent = MasterAgent()
        result = agent.run("find something")

        self.assertIn("route", result)
        self.assertIn("finder", result)
        self.assertIn("executor", result)

        self.assertIsNotNone(result["route"])
        self.assertIsNotNone(result["finder"])
        self.assertIsNotNone(result["executor"])


if __name__ == "__main__":
    unittest.main()
