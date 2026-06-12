import android.app.Service
import android.content.Intent
import android.os.IBinder
import java.net.ServerSocket
import kotlin.concurrent.thread

class SocketBridgeService : Service() {

    private var running = true

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {

        thread {
            val server = ServerSocket(5050)

            while (running) {

                val client = server.accept()
                val input = client.getInputStream().bufferedReader().readLine()

                if (input != null) {
                    handleCommand(input)
                }

                client.close()
            }
        }

        return START_STICKY
    }

    override fun onBind(intent: Intent?): IBinder? = null


    private fun handleCommand(command: String) {

        when {

            command.startsWith("click") -> {

                val parts = command.removePrefix("click:")
                    .split(",")

                val x = parts[0].toInt()
                val y = parts[1].toInt()

                AccessibilityController.click(x, y)
            }

            command.startsWith("swipe") -> {

                val p = command.removePrefix("swipe:")
                    .split(",")

                AccessibilityController.swipe(
                    p[0].toInt(),
                    p[1].toInt(),
                    p[2].toInt(),
                    p[3].toInt()
                )
            }
        }
    }
}
