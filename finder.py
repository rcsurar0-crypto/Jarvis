import json
import os


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


class Finder:

    def __init__(self):
        self.memory = MemoryStore()

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

        # 2. SIMULATED SEARCH LOGIC (ide jön majd AutoInput / UI)
        result = self._search_ui(command)

        # 3. SAVE TO MEMORY
        if result["found"]:
            self.memory.set(command, result)

        return result

    def _search_ui(self, command):

        # 👉 IDE jön később a valódi Android UI keresés

        # fallback logika (egyszerűen most)
        if "search" in command.lower():
            return {
                "found": True,
                "method": "text_match",
                "confidence": 0.6,
                "target": "search_button"
            }

        elif "home" in command.lower():
            return {
                "found": True,
                "method": "text_match",
                "confidence": 0.7,
                "target": "home_button"
            }

        # LAST RESORT
        return {
            "found": False,
            "method": "none",
            "confidence": 0.0,
            "target": None
        }
