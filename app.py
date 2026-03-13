from http.server import BaseHTTPRequestHandler, HTTPServer
import os

DATA_FILE = "/data/visits.txt"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                f.write("0")

        with open(DATA_FILE, "r+") as f:
            count = int(f.read())
            count += 1
            f.seek(0)
            f.write(str(count))
            f.truncate()

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"Visit count: {count}".encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)  # nosec

print("Server running on port 8000...")
server.serve_forever()