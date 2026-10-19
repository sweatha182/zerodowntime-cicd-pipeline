
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def check_health():
    return {
        "status": "healthy",
        "service": "NovaPay",
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404, "Not Found")
            return

        response = json.dumps(check_health()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), HealthHandler)
    print("NovaPay health endpoint running on port 8000")
    server.serve_forever()
