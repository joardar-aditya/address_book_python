#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:08:56 2019

@author: jordan
"""

import basic_pb2
import sys

def PromptForAddress(person):
    person.id =     int(input("Enter a person's ID number"))
    person.name = input("Enter the person's name")
    email = input("Enter email address(Leave blank for None) :")
    if email != "" :
        person.email = email
    while True:
        number = input("Enter a phone number (or leave blank to finish):")
        if number == "":
            break
        phone_number = person.phones.add()
        phone_number.number = number
        
        type_ph = input("Is this a mobile, home or work phone?")
        if type_ph == "mobile" :
            phone_number.type = basic_pb2.Person.MOBILE
        elif type_ph == "home" :
            phone_number.type = basic_pb2.Person.HOME
        elif type_ph == "Work" :
            phone_number.type = basic_pb2.Person.WORK
        else :
            print("Unknown phone type; leaving as default value")
if len(sys.argv) != 2:
  print ("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
  sys.exit(-1)
addressbook = basic_pb2.AddressBook()

try:
    f = open(sys.argv[1], "rb")
    addressbook.ParseFromString(f.read())
    f.close()
except IOError :
    print(sys.argv[1] + "Could not open file. Creating a new one.")
PromptForAddress(addressbook.people.add())
f = open(sys.argv[1], "wb")
f.write(addressbook.SerializeToString())
f.close()
    
    
         