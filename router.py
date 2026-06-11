class Router:
    def route(self, command):
        if "find" in command.lower():
            return {
                "success": True,
                "data": "FINDER",
                "method": "keyword_match",
                "error": None
            }

        return {
            "success": False,
            "data": "UNKNOWN",
            "method": "fallback",
            "error": "No route matched"
        }
