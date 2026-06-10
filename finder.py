class Finder:
    def find(self, target):
        target_lower = target.lower()

        # 1. ID search (szimulált)
        if "button" in target_lower:
            return {
                "found": True,
                "method": "ID",
                "confidence": 0.95,
                "target": target
            }

        # 2. TEXT search
        if "search" in target_lower or "find" in target_lower:
            return {
                "found": True,
                "method": "TEXT",
                "confidence": 0.85,
                "target": target
            }

        # 3. fallback
        return {
            "found": False,
            "method": None,
            "confidence": 0.0,
            "target": target
        }
