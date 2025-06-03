import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html; charset=UTF-8\r\n"
    "Content-Length: 138\r\n"
    "Connection: close\r\n"
    "\r\n"
    "<html>\n"
    "  <head><title>Example Page</title></head>\n"
    "  <body>\n"
    "    <h1>Hello, world!</h1>\n"
    "    <p>This is an example of an HTTP response body.</p>\n"
    "  </body>\n"
    "</html>\n"
)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(response.encode('utf-8'))