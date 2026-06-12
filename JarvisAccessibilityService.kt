import android.accessibilityservice.AccessibilityService
import android.view.accessibility.AccessibilityEvent

class JarvisAccessibilityService : AccessibilityService() {

    override fun onServiceConnected() {
        super.onServiceConnected()

        AccessibilityController.service = this
        println("Jarvis Accessibility connected")
    }

    override fun onAccessibilityEvent(event: AccessibilityEvent?) {
        // később: UI tracking / Vision input
    }

    override fun onInterrupt() {}
}
