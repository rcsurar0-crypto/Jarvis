import time


class Vision:

    def analyze_screen(self, screenshot_data):

        """
        Ez a modul:
        - kap egy képernyő “snapshot”-ot (később valódi screenshot lesz)
        - visszaad UI elemeket + confidence score-t
        """

        try:

            # 🔍 1. SZIMULÁLT UI FELISMERÉS
            ui_elements = self._detect_ui_elements(screenshot_data)

            # 🎯 2. LEGJOBB CÉLPONT KIVÁLASZTÁS
            best_target = self._select_best(ui_elements)

            return {
                "success": True,
                "method": "vision_v1",
                "elements": ui_elements,
                "target": best_target,
                "timestamp": time.time()
            }

        except Exception as e:

            return {
                "success": False,
                "method": "vision_v1",
                "error": str(e),
                "elements": [],
                "target": None
            }

    # -------------------------
    # UI DETECTION (SZIMULÁCIÓ)
    # később: OCR / ML / screenshot AI
    # -------------------------

    def _detect_ui_elements(self, screenshot_data):

        # 👉 MOST MÉG SZABÁLY ALAPÚ
        # később: valódi image recognition

        elements = []

        text = str(screenshot_data).lower()

        if "search" in text:
            elements.append({
                "type": "button",
                "name": "search",
                "confidence": 0.90,
                "bbox": (100, 200, 300, 260)
            })

        if "home" in text:
            elements.append({
                "type": "button",
                "name": "home",
                "confidence": 0.85,
                "bbox": (10, 700, 120, 780)
            })

        if "send" in text:
            elements.append({
                "type": "button",
                "name": "send",
                "confidence": 0.80,
                "bbox": (800, 1500, 950, 1600)
            })

        return elements

    # -------------------------
    # DÖNTÉS LOGIKA
    # -------------------------

    def _select_best(self, elements):

        if not elements:
            return {
                "found": False,
                "confidence": 0.0,
                "target": None
            }

        best = max(elements, key=lambda x: x["confidence"])

        return {
            "found": True,
            "confidence": best["confidence"],
            "target": best,
            "method": "vision_confidence_select"
        }
