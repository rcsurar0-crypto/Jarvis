class MemoryLog:

    def __init__(self):
        self.memory = {
            "success": [],
            "fail": [],
            "rules": []
        }

    def add_success(self, key, method):
        self.memory["success"].append({
            "key": key,
            "method": method
        })

    def add_fail(self, key, reason):
        self.memory["fail"].append({
            "key": key,
            "reason": reason
        })

    def add_rule(self, rule):
        self.memory["rules"].append(rule)

    def get_memory(self):
        return self.memory
