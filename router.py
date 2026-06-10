class Router:
    def route(self, command):
        if "find" in command.lower():
            return "FINDER"
        return "UNKNOWN"
