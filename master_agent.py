from router import Router
from finder_v2 import FinderV2
from executor import Executor
from verify import Verify


class MasterAgent:

    def __init__(self):
        self.router = Router()
        self.finder = FinderV2()
        self.executor = Executor()
        self.verify = Verify()

    def run(self, command):

        try:
            # 1. ROUTER
            route = self.router.route(command)

            # 2. FINDER V2 (AI decision)
            finder_result = self.finder.find(command)

            # 3. ACTION kiválasztás
            if finder_result.get("found"):
                action = finder_result.get("target")
            else:
                action = route.get("data") if isinstance(route, dict) else route

            # 4. EXECUTOR (alap végrehajtás)
            control_result = self.executor.execute(action)

            # 5. VISION FALLBACK CLICK LOGIKA
            if isinstance(finder_result, dict) and finder_result.get("method") == "vision_fallback":

                target = finder_result.get("target")

                if target:

                    control_result = self.executor.execute(target)

            # 6. VERIFY
            verify_result = self.verify.check(control_result)

            # 7. SUCCESS LOGIKA
            success = (
                control_result.get("success", False)
                and verify_result.get("success", False)
            )

            # 8. MEMORY UPDATE
            if success:
                try:
                    self.finder.memory.set(command, finder_result)
                except:
                    pass

            # 9. RETURN FULL PIPELINE
            return {
                "success": success,
                "data": {
                    "route": route,
                    "finder": finder_result,
                    "executor": control_result,
                    "verify": verify_result
                },
                "method": "jarvis_full_loop_v4",
                "error": None
            }

        except Exception as e:

            return {
                "success": False,
                "data": None,
                "error": str(e),
                "method": "jarvis_full_loop_v4"
            }
