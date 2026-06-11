from router import Router
from finder import Finder
from executor import Executor
from verify import Verify


class MasterAgent:

    def run(self, command):

        router = Router()
        finder = Finder()
        executor = Executor()
        verify = Verify()

        try:
            # 1. ROUTE
            route = router.route(command)

            # 2. FIND
            finder_result = finder.find(command)

            # 3. ACTION PREP
            action = route.get("data") if isinstance(route, dict) else route

            # 4. EXECUTE
            executor_result = executor.execute(action)

            # 5. VERIFY
            verify_result = verify.check(executor_result)

            return {
                "success": True,
                "data": {
                    "route": route,
                    "finder": finder_result,
                    "executor": executor_result,
                    "verify": verify_result
                },
                "method": "v2_pipeline_stable",
                "error": None
            }

        except Exception as e:

            return {
                "success": False,
                "data": {
                    "route": route if "route" in locals() else None,
                    "finder": finder_result if "finder_result" in locals() else None,
                    "executor": executor_result if "executor_result" in locals() else None
                },
                "error": str(e),
                "method": "v2_pipeline_stable"
            }
