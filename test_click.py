import socket

# 🔥 TELEFON IP CÍME (ezt már tudod)
HOST = "192.168.0.205"

# 🔥 SOCKET PORT (Android oldalon is ez van)
PORT = 5050

def send_click(x, y):

    try:
        # kapcsolat létrehozás
        s = socket.socket()
        s.connect((HOST, PORT))

        # parancs küldése Androidnak
        message = f"click:{x},{y}"
        s.send(message.encode())

        # lezárás
        s.close()

        print("✅ Click sent:", message)

    except Exception as e:
        print("❌ Error:", e)


# 🔥 TESZT KATTINTÁS
send_click(500, 800)
