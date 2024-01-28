import socket


def add_numbers(a, b):
    # Connect to the server
    server_address = ('localhost', 12345)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    # Send the numbers to the server
    message = f"{a},{b}"
    client_socket.sendall(message.encode())

    # Receive the result from the server
    result = client_socket.recv(1024).decode()

    # Close the connection
    client_socket.close()

    return int(result)


if __name__ == '__main__':
    # Test the client
    num1 = 5
    num2 = 7
    print(f"Request: {num1} + {num2}")
    output = add_numbers(5, 7)
    print(f"Result: {output}")
