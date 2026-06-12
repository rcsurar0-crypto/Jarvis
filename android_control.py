class AndroidControl:

    def click(self, target):

        if isinstance(target, dict) and "bbox" in target:

            x1, y1, x2, y2 = target["bbox"]
            x = (x1 + x2) // 2
            y = (y1 + y2) // 2

            return {
                "action": "click",
                "x": x,
                "y": y,
                "status": "ready_for_accessibility"
            }

        return {
            "action": "click",
            "target": target,
            "status": "waiting_bridge"
        }
