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
            # 1. ROUTE (mit kell csinálni)
            route = self.router.route(command)

            # 2. FINDER V2 (okos döntés)
            finder_result = self.finder.find(command)

            # 3. ACTION kiválasztás
            action = route.get("data") if isinstance(route, dict) else route

            # 4. EXECUTE (végrehajtás)
            executor_result = self.executor.execute(action)

            # 5. VERIFY (ellenőrzés)
            verify_result = self.verify.check(executor_result)

            # 6. FINAL SUCCESS LOGIKA
            success = (
                executor_result.get("success") and
                verify_result.get("success")
            )

            # 7. MEMORY UPDATE (ha van success)
            if success:
                try:
                    self.finder.memory.set(command, finder_result)
                except:
                    pass

            return {
                "success": success,
                "data": {
                    "route": route,
                    "finder": finder_result,
                    "executor": executor_result,
                    "verify": verify_result
                },
                "method": "jarvis_full_loop_v2",
                "error": None
            }

        except Exception as e:

            return {
                "success": False,
                "data": None,
                "error": str(e),
                "method": "jarvis_full_loop_v2"
                    }
