class Finder:

    def find(self, target):

        if self.has_id(target):
            return {
                "success": True,
                "data": {"method": "ID", "confidence": 0.95, "target": target},
                "error": None
            }

        if self.has_text(target):
            return {
                "success": True,
                "data": {"method": "TEXT", "confidence": 0.7, "target": target},
                "error": None
            }

        if self.has_accessibility(target):
            return {
                "success": True,
                "data": {"method": "ACCESSIBILITY", "confidence": 0.6, "target": target},
                "error": None
            }

        if self.can_see_screen(target):
            return {
                "success": True,
                "data": {"method": "OCR_SCREEN", "confidence": 0.4, "target": target},
                "error": None
            }

        return {
            "success": True,
            "data": {"method": "COORDINATE", "confidence": 0.1, "target": target},
            "error": None
        }

    def has_id(self, target):
        return True

    def has_text(self, target):
        return False

    def has_accessibility(self, target):
        return False

    def can_see_screen(self, target):
        return False
