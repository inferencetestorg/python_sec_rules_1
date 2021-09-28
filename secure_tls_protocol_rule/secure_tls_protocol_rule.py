def non_conformant1():
    import ssl
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv2)

def non_conformant2():
    import ssl
    context = ssl.wrap_socket(ssl_version=ssl.PROTOCOL_SSLv3)

def non_conformant3():
    import ssl
    context = ssl.get_server_certificate((host,port), ssl_version=ssl.PROTOCOL_TLSv1, ca_certs=None)

def non_conformant4():
    import ssl
    context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_1)

def non_conformant5():
    import ssl
    context1 = ssl.SSLContext(0)

def non_conformant6():
    import ssl
    context1 = ssl.wrap_socket(ssl_version=1)

def non_conformant7():
    import ssl
    context1 = ssl.get_server_certificate((host,port), ssl_version=3, ca_certs=None)

def non_conformant8():
    import ssl
    context1 = ssl.SSLContext(protocol=4)

def non_conformant9():
    import ssl
    protocol = ssl.PROTOCOL_TLSv1
    context1 = ssl.SSLContext(protocol=protocol)

def non_conformant10():
    import ssl
    wraper_dict = {"ssl_version":ssl.PROTOCOL_SSLv2, "ca_certs":None}
    context1 = ssl.get_server_certificate((host,port), **wraper_dict)

def non_conformant11():
    import ssl
    context1 = ssl.get_server_certificate((host,port), **{"ssl_version":ssl.PROTOCOL_SSLv2, "ca_certs":None})

def non_conformant12():
    import socket
    import ssl

    # SET VARIABLES
    packet, reply = "<packet>SOME_DATA</packet>", ""
    HOST, PORT = 'XX.XX.XX.XX', 4434

    # CREATE SOCKET
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    socketDetails = {"ssl_version":ssl.PROTOCOL_TLSv1, "ciphers":"ADH-AES256-SHA"}

    # WRAP SOCKET
    wrappedSocket = ssl.wrap_socket(sock, **socketDetails)

    # CONNECT AND PRINT REPLY
    wrappedSocket.connect((HOST, PORT))
    wrappedSocket.send(packet)
    print (wrappedSocket.recv(1280))

    # CLOSE SOCKET CONNECTION
    wrappedSocket.close()

def non_conformant13():
    import socket
    import ssl

    # SET VARIABLES
    packet, reply = "<packet>SOME_DATA</packet>", ""
    HOST, PORT = 'XX.XX.XX.XX', 4434

    # CREATE SOCKET
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    # WRAP SOCKET
    wrappedSocket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")

    # CONNECT AND PRINT REPLY
    wrappedSocket.connect((HOST, PORT))
    wrappedSocket.send(packet)
    print (wrappedSocket.recv(1280))

    # CLOSE SOCKET CONNECTION
    wrappedSocket.close()
        
def conformant1():
    import ssl
    context1 = ssl.SSLContext(ssl.PROTOCOL_TLS)

def conformant2():
    import ssl
    context0 = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv23, ciphers="ADH-AES256-SHA")
    context1 = ssl.wrap_socket(ssl_version=2)

def conformant3():
    import ssl
    context = ssl.get_server_certificate(('www.amzn.com',80), ssl_version=ssl.PROTOCOL_TLSv1_2, ca_certs=None)
    context1 = ssl.get_server_certificate(('www.amzn.com',80), ssl_version=5, ca_certs=None)

def conformant4():
    import ssl
    context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
    context1 = ssl.SSLContext(protocol=16)

def conformant5():
    import ssl
    context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
    context1 = ssl.SSLContext(protocol=17)

def conformant6():
    import ssl
    context0 = ssl.wrap_socket(sock, **{"ssl_version":ssl.PROTOCOL_TLSv23, "ciphers":"ADH-AES256-SHA"})
    context1 = ssl.wrap_socket(sock, **{"ssl_version":2, "ciphers":"ADH-AES256-SHA"})

def conformant7():
    import ssl
    wraper_dict = {"ssl_version":ssl.PROTOCOL_TLSv23, "ciphers":"ADH-AES256-SHA"}
    context0 = ssl.wrap_socket(sock, **wraper_dict)