class AndroidControl:

    def click(self, target):
        """
        target = bbox vagy ui elem
        """

        try:

            if isinstance(target, dict) and "bbox" in target:
                x1, y1, x2, y2 = target["bbox"]

                x = (x1 + x2) // 2
                y = (y1 + y2) // 2

                return {
                    "action": "click",
                    "x": x,
                    "y": y,
                    "method": "bounding_box_click",
                    "status": "executed"
                }

            return {
                "action": "click",
                "target": target,
                "method": "fallback_click",
                "status": "executed"
            }

        except Exception as e:
            return {
                "action": "click",
                "status": "failed",
                "error": str(e)
            }

    def swipe(self, direction):

        return {
            "action": "swipe",
            "direction": direction,
            "status": "executed"
        }

    def open_app(self, app_name):

        return {
            "action": "open_app",
            "app": app_name,
            "status": "executed"
        }

    def get_ui_state(self):

        return {
            "screen": "active",
            "elements": []
        }
