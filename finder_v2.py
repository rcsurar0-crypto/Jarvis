import json
import os
from vision import Vision


# =========================
# MEMORY LAYER
# =========================
class MemoryStore:

    def __init__(self, file_path="finder_memory.json"):
        self.file_path = file_path
        self.memory = self.load()

    def load(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.memory, f, indent=2)

    def get(self, key):
        return self.memory.get(key)

    def set(self, key, value):
        self.memory[key] = value
        self.save()


# =========================
# FINDER V3 CORE
# =========================
class FinderV3:

    def __init__(self):
        self.memory = MemoryStore()
        self.vision = Vision()

    # =========================
    # MAIN ENTRY
    # =========================
    def find(self, command):

        # 1. MEMORY HIT
        cached = self.memory.get(command)
        if cached:
            return self._format_result(
                method="memory",
                confidence=1.0,
                data=cached
            )

        # 2. ACCESSIBILITY SCAN (REAL UI TREE)
        acc_result = self._accessibility_scan(command)
        if acc_result["confidence"] >= 0.85:
            self.memory.set(command, acc_result)
            return acc_result

        # 3. TEXT MATCHING
        text_result = self._text_scan(command)
        if text_result["confidence"] >= 0.65:
            self.memory.set(command, text_result)
            return text_result

        # 4. VISION (SCREEN + OCR)
        vision_result = self.vision.analyze_screen(command)
        if vision_result.get("success"):
            target = vision_result["target"]

            formatted = self._format_result(
                method="vision",
                confidence=target.get("confidence", 0.8),
                data=target
            )

            self.memory.set(command, formatted)
            return formatted

        # 5. LAST RESORT: COORDINATE GUESS
        coord_result = self._coordinate_fallback(command)
        self.memory.set(command, coord_result)
        return coord_result

    # =========================
    # ACCESSIBILITY LAYER
    # =========================
    def _accessibility_scan(self, command):

        # Simulated UI tree response (later Android fills this)
        ui_nodes = [
            {
                "text": "Search",
                "id": "search_btn",
                "bounds": (400, 900, 600, 1000),
                "confidence": 0.92
            },
            {
                "text": "OK",
                "id": "ok_btn",
                "bounds": (700, 1200, 900, 1300),
                "confidence": 0.80
            }
        ]

        best = None
        cmd = command.lower()

        for node in ui_nodes:
            score = node["confidence"]

            if node["text"].lower() in cmd:
                score += 0.05

            if score > 0.9:
                best = node
                break

        if best:
            return self._format_result(
                method="accessibility",
                confidence=best["confidence"],
                data=self._convert_bbox(best)
            )

        return self._format_result(
            method="accessibility",
            confidence=0.4,
            data=None
        )

    # =========================
    # TEXT SCAN
    # =========================
    def _text_scan(self, command):

        text_db = {
            "search": {
                "text": "Search",
                "bounds": (400, 900, 600, 1000),
                "confidence": 0.75
            }
        }

        for key, value in text_db.items():
            if key in command.lower():
                return self._format_result(
                    method="text",
                    confidence=value["confidence"],
                    data=self._convert_bbox(value)
                )

        return self._format_result(
            method="text",
            confidence=0.3,
            data=None
        )

    # =========================
    # VISION COORDINATE FALLBACK
    # =========================
    def _coordinate_fallback(self, command):

        return self._format_result(
            method="coordinate_fallback",
            confidence=0.2,
            data={
                "x1": 500,
                "y1": 1000,
                "x2": 520,
                "y2": 1020,
                "center": (510, 1010),
                "size": (20, 20)
            }
        )

    # =========================
    # BOUNDING BOX CONVERTER (PRO)
    # =========================
    def _convert_bbox(self, node):

        if "bounds" in node:
            x1, y1, x2, y2 = node["bounds"]
        else:
            x1 = y1 = x2 = y2 = 0

        return {
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "center": ((x1 + x2) // 2, (y1 + y2) // 2),
            "size": (x2 - x1, y2 - y1),
            "confidence": node.get("confidence", 0.5)
        }

    # =========================
    # FORMAT OUTPUT
    # =========================
    def _format_result(self, method, confidence, data):

        return {
            "found": True,
            "method": method,
            "confidence": confidence,
            "data": data
        }
