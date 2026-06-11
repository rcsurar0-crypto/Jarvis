from router import Router
from finder import Finder
from executor import Executor


class MasterAgent:

    def run(self, command):

        try:
            router = Router()
            route = router.route(command) or {}

            finder = Finder()
            finder_result = finder.find(command)

            executor = Executor()

            action = route.get("data", "UNKNOWN")

            executor_result = executor.execute(action)

            return {
                "success": True,
                "data": {
                    "route": route,
                    "finder": finder_result,
                    "executor": executor_result
                },
                "error": None,
                "method": "v2_stable"
            }

        except Exception as e:
            return {
                "success": False,
                "data": None,
                "error": str(e),
                "method": "v2_stable"
            }
