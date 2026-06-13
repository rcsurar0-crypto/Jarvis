package com.jarvis

import android.accessibilityservice.AccessibilityService
import android.view.accessibility.AccessibilityEvent
import android.accessibilityservice.GestureDescription
import android.graphics.Path
import android.util.Log
import java.net.ServerSocket
import kotlin.concurrent.thread

class SocketBridgeService : AccessibilityService() {

    private var serverSocket: ServerSocket? = null
    private val port = 7777

    override fun onServiceConnected() {
        super.onServiceConnected()
        startServer()
    }

    override fun onAccessibilityEvent(event: AccessibilityEvent?) {}

    override fun onInterrupt() {}

    // 🟢 SOCKET SERVER INDÍTÁS
    private fun startServer() {
        thread {
            try {
                serverSocket = ServerSocket(port)
                Log.d("SocketBridge", "Server started on port $port")

                while (true) {
                    val client = serverSocket!!.accept()
                    val input = client.getInputStream().bufferedReader().readLine()

                    Log.d("SocketBridge", "Received: $input")

                    handleCommand(input)

                    client.close()
                }

            } catch (e: Exception) {
                Log.e("SocketBridge", "Error: ${e.message}")
            }
        }
    }

    // 🟢 PARANCS FELDOLGOZÁS
    private fun handleCommand(msg: String?) {
        if (msg == null) return

        try {
            // SIMPLE FORMAT:
            // click:500:900
            // swipe:100:200:400:800

            val parts = msg.split(":")

            when (parts[0]) {

                "click" -> {
                    val x = parts[1].toInt()
                    val y = parts[2].toInt()
                    click(x, y)
                }

                "swipe" -> {
                    val x1 = parts[1].toInt()
                    val y1 = parts[2].toInt()
                    val x2 = parts[3].toInt()
                    val y2 = parts[4].toInt()
                    swipe(x1, y1, x2, y2)
                }
            }

        } catch (e: Exception) {
            Log.e("SocketBridge", "Parse error: ${e.message}")
        }
    }

    // 🟢 CLICK
    fun click(x: Int, y: Int) {
        val path = Path()
        path.moveTo(x.toFloat(), y.toFloat())

        val gesture = GestureDescription.Builder()
            .addStroke(GestureDescription.StrokeDescription(path, 0, 100))
            .build()

        dispatchGesture(gesture, null, null)
    }

    // 🟢 SWIPE
    fun swipe(x1: Int, y1: Int, x2: Int, y2: Int) {
        val path = Path()
        path.moveTo(x1.toFloat(), y1.toFloat())
        path.lineTo(x2.toFloat(), y2.toFloat())

        val gesture = GestureDescription.Builder()
            .addStroke(GestureDescription.StrokeDescription(path, 0, 300))
            .build()

        dispatchGesture(gesture, null, null)
    }
}
