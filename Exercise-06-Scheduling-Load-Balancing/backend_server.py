from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"Task-scheduling lab backend: {socket.gethostname()}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    print("Backend listening on 0.0.0.0:8080")
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
