import json
import os
from vision import Vision


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


class FinderV2:

    def __init__(self):
        self.memory = MemoryStore()
        self.vision = Vision()   # 👁 VISION HOZZÁKÖTÉS

    def find(self, command):

        # 1. MEMORY CHECK
        cached = self.memory.get(command)

        if cached:
            return {
                "found": True,
                "method": "memory",
                "confidence": 1.0,
                "data": cached
            }

        # 2. DECISION TREE
        candidates = self._generate_candidates(command)

        best = self._select_best(candidates)

        # 3. VISION FALLBACK (ha gyenge a találat)
        if not best.get("found") or best.get("confidence", 0) < 0.7:

            vision_result = self.vision.analyze_screen(command)

            if vision_result.get("success"):

                target = vision_result.get("target")

                return {
                    "found": True,
                    "method": "vision_fallback",
                    "confidence": target.get("confidence", 0.8),
                    "target": target
                }

        # 4. SAVE MEMORY
        if best.get("found"):
            self.memory.set(command, best)

        return best

    # -------------------------
    # DÖNTÉSI FA + CONFIDENCE
    # -------------------------

    def _generate_candidates(self, command):

        candidates = []
        text = command.lower()

        if "id" in text:
            candidates.append({
                "method": "id",
                "confidence": 0.95,
                "found": True,
                "target": "ui_by_id"
            })

        if "text" in text:
            candidates.append({
                "method": "text",
                "confidence": 0.60,
                "found": True,
                "target": "ui_by_text"
            })

        if "screen" in text:
            candidates.append({
                "method": "screenshot",
                "confidence": 0.50,
                "found": True,
                "target": "ui_by_screen"
            })

        return candidates

    def _select_best(self, candidates):

        if not candidates:
            return {
                "found": False,
                "method": "none",
                "confidence": 0.0,
                "target": None
            }

        best = max(candidates, key=lambda x: x["confidence"])

        return {
            "found": True,
            "method": best["method"],
            "confidence": best["confidence"],
            "target": best["target"]
            }
