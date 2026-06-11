class Verify:

    def check(self, action_result):

        if action_result is None:
            return {
                "success": False,
                "verified": False,
                "reason": "no result"
            }

        if isinstance(action_result, dict) and action_result.get("success"):
            return {
                "success": True,
                "verified": True,
                "reason": "action confirmed"
            }

        return {
            "success": False,
            "verified": False,
            "reason": "action failed or unknown"
        }
