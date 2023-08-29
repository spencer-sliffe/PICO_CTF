#!/usr/bin/python3
        
import telnetlib
HOST = "chals.sekai.team"
PORT = 9000

tn = telnetlib.Telnet(HOST, PORT)

while True:
    print(tn.read_until(b"\n"))
    question = tn.read_until(b"=").decode()
    print(question)
    break_question = question.split(" ")
    first = int(break_question[0])
    second = int(break_question[2])
    if break_question[1] == '-':
        result = str(first - second)
        tn.write(result.encode())
    if break_question[1] == '*':
        result = str(first * second)
        tn.write(result.encode())
    if break_question[1] == '+':
        result = str(first + second)
        tn.write(result.encode())
        
        
        