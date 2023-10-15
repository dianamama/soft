import socket
import pyautogui as pg

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1],1234))
server.listen()

while True:
    user, adres = server.accept()

    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)
        if data == "dota 2":
            pg.doubleClick(335, 739)
        elif data == "bim":
                pg.hotkey("alt", "f4")
        elif data == "black":
            pg.hotkey("winleft", "r")
            a = 1
            while a <= 20:
                pg.typewrite(["backspace"])
                a = a + 1
            pg.typewrite("cmd")
            pg.typewrite(["enter"])
            pg.typewrite("shutdown -s -t 0")
            pg.typewrite(["enter"])
