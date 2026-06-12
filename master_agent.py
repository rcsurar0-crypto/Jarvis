class Memory:

    def __init__(self):
        self.store = []

    def save(self, data):
        self.store.append(data)


class Verify:

    def check(self, executor_result):

        if executor_result.get("success"):
            return {
                "state": "SUCCESS",
                "confidence": 1.0,
                "trace": executor_result.get("trace", [])
            }

        error = executor_result.get("error", "unknown error")

        return {
            "state": "FAIL",
            "step": executor_result.get("step", "UNKNOWN"),
            "error": error,
            "cause": self.analyze(error),
            "confidence": 0.6,
            "fix_suggestion": self.suggest_fix(error),
            "trace": executor_result.get("trace", [])
        }

    def analyze(self, error):

        if "not found" in error:
            return "UI element missing"

        if "timeout" in error:
            return "execution timeout"

        if "permission" in error:
            return "missing permission"

        return "unknown cause"

    def suggest_fix(self, error):

        if "not found" in error:
            return "try accessibility fallback or OCR"

        if "timeout" in error:
            return "increase delay or retry execution"

        if "permission" in error:
            return "enable accessibility service"

        return "manual debugging needed"


class Executor:

    def execute(self, action):

        try:
            # itt később Android socket / click / swipe jön
            print(f"[EXECUTOR] action: {action}")

            return {
                "success": True,
                "step": "EXECUTOR",
                "result": "done",
                "trace": ["executor"]
            }

        except Exception as e:

            return {
                "success": False,
                "step": "EXECUTOR",
                "error": str(e),
                "trace": ["executor"]
            }


class Router:

    def route(self, command):

        return {
            "action": command,
            "type": "default"
        }


class MasterAgent:

    def __init__(self):

        self.router = Router()
        self.executor = Executor()
        self.verify = Verify()
        self.memory = Memory()

    def run(self, command):

        # 🧭 1. ROUTE
        route = self.router.route(command)
        action = route["action"]

        # ⚙️ 2. EXECUTE
        executor_result = self.executor.execute(action)

        # 🧪 3. VERIFY
        verify_result = self.verify.check(executor_result)

        # 🧠 4. MEMORY SAVE
        self.memory.save({
            "command": command,
            "route": route,
            "executor": executor_result,
            "verify": verify_result
        })

        # 🔥 5. FINAL RESULT
        return {
            "success": verify_result.get("state") == "SUCCESS",
            "route": route,
            "executor": executor_result,
            "verify": verify_result
        }


# -------------------------
# TEST RUN
# -------------------------
if __name__ == "__main__":

    agent = MasterAgent()

    result = agent.run("click button")

    print("\nFINAL RESULT:")
    print(result)
