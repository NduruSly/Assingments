# server.py
import socket


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 12345))
        server_socket.listen()
        print("Server listening on port 12345...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            conn.sendall(b"Hello from server!")

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()


# client.py
def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 12345))
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()


# Run either server or client based on user choice
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1].lower() == 'server':
        run_server()
    else:
        run_client()