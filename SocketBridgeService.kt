import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.ServerSocket
import kotlin.concurrent.thread

class SocketBridgeService : Thread() {

    var running = true

    override fun run() {

        val server = ServerSocket(5050)

        while (running) {

            val client = server.accept()

            val reader = BufferedReader(InputStreamReader(client.getInputStream()))

            val line = reader.readLine()

            if (line != null) {
                handleCommand(line)
            }

            client.close()
        }
    }

    private fun handleCommand(command: String) {

        // Példa: "click:500,800"
        if (command.startsWith("click")) {

            val parts = command.split(":")[1].split(",")

            val x = parts[0].toInt()
            val y = parts[1].toInt()

            AccessibilityController.click(x, y)
        }

        if (command.startsWith("swipe")) {

            val parts = command.split(":")[1].split(",")

            AccessibilityController.swipe(
                parts[0].toInt(),
                parts[1].toInt(),
                parts[2].toInt(),
                parts[3].toInt()
            )
        }
    }
}
