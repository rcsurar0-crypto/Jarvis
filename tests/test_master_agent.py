import unittest
from master_agent import MasterAgent

class TestMasterAgent(unittest.TestCase):

    def test_pipeline_runs(self):
        agent = MasterAgent()
        result = agent.run("find something")

        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertIn("data", result)

if __name__ == "__main__":
    unittest.main()
