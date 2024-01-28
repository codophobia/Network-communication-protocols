import socket


def add_numbers(num1, num2):
    return num1 + num2


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and port
    host = 'localhost'
    port = 12345

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        print('Connected to client:', addr)

        # Receive the numbers from the client
        data = client_socket.recv(1024).decode()
        num1, num2 = map(int, data.split(','))

        # Add the numbers
        result = add_numbers(num1, num2)

        # Send the result back to the client
        client_socket.send(str(result).encode())

        # Close the client connection
        client_socket.close()


if __name__ == '__main__':
    start_server()
