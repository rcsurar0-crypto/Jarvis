class Executor:
    def execute(self, action):
        if action == "FINDER":
            return {
                "executed": True,
                "action": action,
                "result": "Simulated find executed"
            }

        return {
            "executed": False,
            "action": action,
            "result": "Unknown action"
        }
