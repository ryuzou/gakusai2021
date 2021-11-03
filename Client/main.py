from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
import cv2
import base64
import numpy as np

"""IPADDR = "192.168.0.6"
PORT_TCP = 8000
PORT_UDP = 8092

socket_tcp = socket(AF_INET, SOCK_STREAM)
socket_tcp.connect((IPADDR, PORT_TCP))
socket_tcp.send("hello tcp world\n".encode("utf-8"))

socket_udp = socket(AF_INET, SOCK_DGRAM)
socket_udp.bind(("0.0.0.0", PORT_UDP))

buff = 1034 * 64

while True:
    data = bytes()
    data, _ = socket_udp.recvfrom(buff)
    print(data)

    """
baseImg = np.zeros((960, 1280, 3))
test_data = b'32_11_40_30&/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/wAALCAAeACgBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/AM3whquoWN2tnqukWjGa6XZdTSsW24yWG0jH45GK1/7RV9YnjsoPOVWZWO4Ft3rjHTvmo/7WdNTk0h74uXQMsSy43oOuAMggHr6VHe3ltDLb2l1qUFvC9wfsyzZ2vJj++By3PA6VWI1OS7/snw9psbXqQSxq11e7YljY/MxGPvDPGMDmq9jBqd1dXcuq2EVnlGMVgf3rJEeN4C5Iyegq8813Y28cs9o0ccUCQxIICjBezEHkZ6807SLPRrPVotekiheXy2gtbhZd4B7rgHABPJJqnqL6bcWLW92J2js5DJaQkbo1lJ52g9B3x71e0jxYYVi0pNJsbxZgfMmXIdM/w57ewrLsrqPUdcGpQaVPD5ztE1y12d7MOVKgcbfrWibi71bVJr/UvEct9dEhUjd8srjjbKT97jimRIlrHut1HDkvsAWNF/ijx2571De61pFtpl7o+h6YZNym5e7dyQ7Y+dVJ+o6ccVcuvC+pT6VFq02jX1vbi13fbLcAJHMvQOw9RyAetUrERz3jXGpyusUcMRtUtAFIU/3s9TWlY2Fu0Fz59pG95JfeVaXO4gRxt6r3YHkGn6xpN/o19cWhvo0ljtyjtHDuSTH8RBxyaq2WiW1z4Ve/hhANhfiEhnP7xmGWz/s8Hj3ptqdR1RZEutTnkhfBe3eVgmFO0EqMBiBkDNf/2Q=='.decode()
header = test_data.split("&")[0]
data = base64.b64decode(test_data.split("&")[1])

nparr = np.frombuffer(data, np.uint8)
img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)