import json
import os


class MemoryStore:

    def __init__(self, file_path="jarvis_memory.json"):
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

    # 🧠 OKOSÍTÁS: módszer preferencia
    def update_success(self, key, method):
        if key not in self.memory:
            self.memory[key] = {"success_count": 0, "methods": {}}

        if "methods" not in self.memory[key]:
            self.memory[key]["methods"] = {}

        self.memory[key]["methods"][method] = \
            self.memory[key]["methods"].get(method, 0) + 1

        self.memory[key]["success_count"] += 1
        self.save()
