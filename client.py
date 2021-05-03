import socket, json
import rtext
import os


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    os.system('cls')
    print("Menu")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choose = int(input())

    while choose != 3:
        p = int(input("input first prime    :  "))  # take input
        q = int(input("input second prime   :  "))
        check_p = rtext.prime_check(p)
        check_q = rtext.prime_check(q)
        while(((check_p==False)or(check_q==False))):
            os.system('cls')
            print("wrong prime number!")
            p = int(input("input first prime    :  "))  # take input
            q = int(input("input second prime   :  "))
            check_p = rtext.prime_check(p)
            check_q = rtext.prime_check(q)
        msg = input("input plaint text for encrypt and the number separated with ',' for decrypt : \n")

        arr = (p, q, msg, choose)
        data = json.dumps({"a": p, "b": q, "c": msg, "d": choose})
        client_socket.send(data.encode())
        data = client_socket.recv(4096)  # receive response
        enc = json.loads(data.decode())

        print('Result: ', enc.get("result"))  # show in terminal

        input("Press enter to continue ... ")  # again take input
        os.system('cls')
        print("Menu")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choose = int(input())

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()