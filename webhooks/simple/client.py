# This app receives the webhook payload and performs
# the action when a webhook is invoked.
import http.server
import socketserver


# Create a handler for incoming webhook requests
class WebhookHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        payload = self.rfile.read(content_length)

        # Process the received webhook payload
        print("Received webhook payload:", payload)

        self.send_response(200)
        self.end_headers()


# Define the server parameters and start the server
PORT = 8010
Handler = WebhookHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Webhook receiver server running on port", PORT)
    httpd.serve_forever()
