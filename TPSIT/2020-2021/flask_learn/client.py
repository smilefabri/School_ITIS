import socket


host = "localhost"
port = 5000

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

headers = """\
POST /login HTTP/1.1\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Host: {host}\r
Connection: close\r
\r\n"""

body = 'username=fabri&password=1234568'                                 
body_bytes = body.encode('utf-8')

header_bytes = headers.format(

    content_type="application/x-www-form-urlencoded",
    content_length=len(body_bytes),
    host=str(host) + ":" + str(port)

).encode('utf-8')

payload = header_bytes + body_bytes


sock.sendall(payload)

print(sock.recv(1024))

sock.close()