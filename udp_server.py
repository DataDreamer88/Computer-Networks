import socket
import random

def generate_otp():
    return str(random.randint(1000, 9999))

def authenticate(userid, password, otp):
    # Simulate a simple authentication logic
    valid_user = {"username": "user123", "password": "pass123"}
    return valid_user["username"] == userid and valid_user["password"] == password and otp == generate_otp()

server_ip = "127.0.0.1"
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print("UDP Server is listening...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    data = data.decode().split(",")

    if len(data) == 3:
        userid, password, otp = data
        if authenticate(userid, password, otp):
            response = "Authentication successful"
        else:
            response = "Authentication failed"
    else:
        response = "Invalid data format"

    server_socket.sendto(response.encode(), client_address)
