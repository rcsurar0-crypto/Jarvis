class Verify:

    def check(self, executor_result):

        try:
            if not executor_result:
                return {
                    "success": False,
                    "method": "verify_v2",
                    "error": "no_result"
                }

            if executor_result.get("success") is True:
                return {
                    "success": True,
                    "method": "verify_v2",
                    "confidence": 0.9,
                    "state": executor_result
                }

            return {
                "success": False,
                "method": "verify_v2",
                "confidence": 0.3,
                "state": executor_result
            }

        except Exception as e:
            return {
                "success": False,
                "method": "verify_v2",
                "error": str(e)
            }
