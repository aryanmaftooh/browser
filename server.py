import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65433  # Port to listen on (non-privileged ports are > 1023)
body = (
    "<html>\n"
    "  <head><title>debugging</title></head>\n"
    "  <body>\n"
    "    <h1>TRY ME</h1>\n"
    "    <p>I am in the debugging phase</p>\n"
    "  </body>\n"
    "</html>\n"
)
response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html; charset=UTF-8\r\n"
    f"Content-Length: {len(body)}\r\n"
    "Connection: close\r\n"
    "\r\n"
)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall((response + body).encode("utf-8"))
