#!/usr/local/bin/python3

import pyVmomi

import pyVim 
from pyVim import connect

si = connect.SmartConnect(host="192.168.199.200",user="root",pwd= '1111111')

message = "Hello Python world!"

print (message)


message = "Hello Python world! This is second Hellow world"
print (message)



name = "ada lovelace"
print (name.title())
print (name.upper())
print (name.lower())


frist_name = "ada"
last_name = "lovelace"

full_name = frist_name + " " +last_name

print(full_name)

print(full_name.title())

print(full_name.capitalize())


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)
