from router import Router
from finder import Finder
from executor import Executor
from verify import Verify


class MasterAgent:

    def __init__(self):
        self.router = Router()
        self.finder = Finder()
        self.executor = Executor()
        self.verify = Verify()

    def run(self, command):

        try:
            route = self.router.route(command)
            finder_result = self.finder.find(command)

            action = route.get("data") if isinstance(route, dict) else route

            executor_result = self.executor.execute(action)
            verify_result = self.verify.check(executor_result)

            success = executor_result.get("success") and verify_result.get("success")

            return {
                "success": success,
                "data": {
                    "route": route,
                    "finder": finder_result,
                    "executor": executor_result,
                    "verify": verify_result
                },
                "method": "jarvis_full_loop_v1",
                "error": None
            }

        except Exception as e:

            return {
                "success": False,
                "data": None,
                "error": str(e),
                "method": "jarvis_full_loop_v1"
            }
