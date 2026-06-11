class Router:
    def route(self, command):

        if "find" in command.lower():
            return {
                "success": True,
                "data": "FINDER",
                "error": None,
                "method": "keyword_match"
            }

        return {
            "success": False,
            "data": "UNKNOWN",
            "error": "No route matched",
            "method": "fallback"
        }
