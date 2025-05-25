from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def show_ip():
    # Get server IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"<h1>Server IP Address: {ip_address}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
