class Finder:
    def find(self, target):
        return {
            "success": True,
            "data": {
                "found": False,
                "target": target
            },
            "method": "stub",
            "error": None
        }
