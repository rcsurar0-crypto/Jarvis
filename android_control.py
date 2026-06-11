class AndroidControl:

    def click(self, target):
        return {
            "action": "click",
            "target": target,
            "status": "simulated"
        }

    def swipe(self, direction):
        return {
            "action": "swipe",
            "direction": direction,
            "status": "simulated"
        }

    def open_app(self, app_name):
        return {
            "action": "open_app",
            "app": app_name,
            "status": "simulated"
        }

    def get_ui_state(self):
        return {
            "screen": "unknown",
            "elements": []
        }
