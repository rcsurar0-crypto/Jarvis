import time
from finder_v3 import FinderV3
from executor_v2 import ExecutorV2


class JarvisLiveLoop:

    def __init__(self):
        self.finder = FinderV3()
        self.executor = ExecutorV2()

        self.running = True

    # =========================
    # MAIN LOOP
    # =========================
    def run(self):

        print("🟢 Jarvis Live Loop V1 STARTED")

        while self.running:

            try:
                # 👉 1. INPUT (itt most fix parancs - később AI jön)
                command = self.get_command()

                if not command:
                    time.sleep(0.5)
                    continue

                print("🧠 Command:", command)

                # 👉 2. FIND UI ELEMENT
                result = self.finder.find(command)

                print("🔍 Finder result:", result)

                # 👉 3. EXECUTE ACTION
                success = self.executor.execute(result)

                print("⚙️ Executed:", success)

                # 👉 4. small delay
                time.sleep(0.5)

            except Exception as e:
                print("❌ Error:", e)
                time.sleep(1)

    # =========================
    # COMMAND SOURCE
    # =========================
    def get_command(self):

        # 🔵 V1 SIMPLE MODE (hardcoded demo)
        # később: socket / AI / voice / telegram

        return "search"


# =========================
# START
# =========================
if __name__ == "__main__":
    bot = JarvisLiveLoop()
    bot.run()
