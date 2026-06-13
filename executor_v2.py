import socket
import json


class ExecutorV2:

    def __init__(self, host="127.0.0.1", port=7777):
        self.host = host
        self.port = port

    # =========================
    # SOCKET SEND
    # =========================
    def send(self, message: str):
        try:
            s = socket.socket()
            s.connect((self.host, self.port))
            s.send(message.encode())
            s.close()
            return True
        except Exception as e:
            print("Socket error:", e)
            return False

    # =========================
    # CLICK (REAL TIME)
    # =========================
    def click(self, x: int, y: int):
        cmd = f"click:{x}:{y}"
        return self.send(cmd)

    # =========================
    # SWIPE (REAL TIME)
    # =========================
    def swipe(self, x1: int, y1: int, x2: int, y2: int):
        cmd = f"swipe:{x1}:{y1}:{x2}:{y2}"
        return self.send(cmd)

    # =========================
    # CLICK CENTER (FINDER INTEGRATION)
    # =========================
    def click_center(self, bbox: dict):
        center = bbox.get("center", (0, 0))
        return self.click(center[0], center[1])

    # =========================
    # FINDER + EXECUTOR CHAIN
    # =========================
    def execute(self, finder_result: dict):

        if not finder_result or not finder_result.get("found"):
            print("No target found")
            return False

        data = finder_result.get("data")

        if not data:
            print("No data")
            return False

        # auto click center
        return self.click_center(data)
