import socket
import sys


def sendRequest():
    HOST = "142.250.72.206"  # The server's hostname or IP address
    PORT = 80  # The port used by the server
    httpRequest = (
        "GET / HTTP/1.1\r\n"
        "Host: facebook\r\n"
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n"
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
        "Accept-Language: en-US,en;q=0.5\r\n"
        "Accept-Encoding: gzip, deflate\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(httpRequest.encode("utf-8"))
        m = s.recv(1024)
        while True:
            data = s.recv(1024)
            if data == b"":
                break
            else:
                m = m + data
        return m.decode("utf-8")

    # return data.decode("utf-8")


if __name__ == "__main__":
    response_output = open("httpRecieved.html", "w")
    sys.stdout = response_output
    r = sendRequest()
    nlc = 0
    for i in range(len(r)):
        if r[i] == "\n":
            nlc += 1
        if nlc == 6:
            p = i
            break
    print(r[p::])
    response_output.close()
