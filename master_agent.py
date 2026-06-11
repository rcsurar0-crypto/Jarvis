from router import Router
from finder import Finder
from executor import Executor

class MasterAgent:

    def run(self, command):

        router = Router()
        route = router.route(command)

        finder = Finder()
        finder_result = finder.find(command)

        executor = Executor()
        executor_result = executor.execute(route["data"])

        return {
            "success": True,
            "data": {
                "route": route,
                "finder": finder_result,
                "executor": executor_result
            },
            "method": "pipeline",
            "error": None
        }
