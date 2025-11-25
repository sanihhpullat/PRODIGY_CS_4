import keyboard
import datetime

print("=== Educational Keylogger Demo ===")
print("This program will record keystrokes until you press ESC.")
print("Use only on a system you own, with full permission.\n")

log_file = "keylog.txt"

def on_key(event):
    with open(log_file, "a", encoding="utf-8") as f:
        key = event.name

        # Format special keys
        if len(key) > 1:
            key = f"[{key.upper()}]"

        f.write(key)

# Start the listener
keyboard.on_press(on_key)

print("Logging started... (Press ESC to stop)")

keyboard.wait("esc")

print(f"Logging stopped. Keys saved in {log_file}.")
