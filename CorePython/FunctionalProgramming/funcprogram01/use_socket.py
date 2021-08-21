import socket


def resolve(host):
    return socket.gethostbyname(host)