import android.accessibilityservice.AccessibilityService
import android.accessibilityservice.GestureDescription
import android.graphics.Path

object AccessibilityController {

    lateinit var service: AccessibilityService

    fun click(x: Int, y: Int) {

        val path = Path()
        path.moveTo(x.toFloat(), y.toFloat())

        val gesture = GestureDescription.Builder()
            .addStroke(GestureDescription.StrokeDescription(path, 0, 100))
            .build()

        service.dispatchGesture(gesture, null, null)
    }

    fun swipe(x1: Int, y1: Int, x2: Int, y2: Int) {

        val path = Path()
        path.moveTo(x1.toFloat(), y1.toFloat())
        path.lineTo(x2.toFloat(), y2.toFloat())

        val gesture = GestureDescription.Builder()
            .addStroke(GestureDescription.StrokeDescription(path, 0, 300))
            .build()

        service.dispatchGesture(gesture, null, null)
    }
}
