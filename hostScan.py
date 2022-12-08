import os, platform
from datetime import datetime as dt

from sympy import ln

# net = input("enter network address: ")

operation = "Host Scanning"

net1 = []
net2 = ""
rng = []
oSystem = platform.system()
file_name = ""

def back():
    filw = open(file_name, 'w')
    filw.write("ping sweep result for network"+net2+"*")
    oper = platform.system()
    if oper == "Windows":
        pinc = "ping -n 1 "
    else:
        pinc = "ping -c 1 "

    for ip in range(rng[0], rng[1]):
        addr = net2 + str(ip)
        com = pinc + addr
        res = os.popen(com)
        for line in res.readlines():
            if(line.split("ttl").__len__() == 2):
                filw.write("\n"+addr+" ---> live")
            if(line.split("TTL").__len__() == 2):
                filw.write("\n"+addr+" ---> live")


def fun():
    net = input("Enter network address: ")
    net_1 = net.split(' ')
    net1 = net_1[0].split('.')
    global net2
    net2 = str(net1[0]) + '.' + str(net1[1]) + '.' + str(net1[2]) + '.'
    st = int(input("Enter first number for last octet: "))
    en = int(input("Enter last number for last octet: "))
    en +=1
    rng.append(st); rng.append(en)
    name = dt.isoformat(dt.now())
    global file_name
    file_name = "outputs/HostPing/"+name+".txt"
    print("Results will be written to file: ",file_name)