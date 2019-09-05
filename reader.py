#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:36:46 2019

@author: jordan
"""

import basic_pb2
import sys

def ListPeople(address_book):
    for person in address_book.people:
        print("Person.ID:", person.id)
        print("Name", person.name)
        if(person.HasField('email')):
            print("Email id:", person.email)
        for phone_number in person.phones:
            if phone_number.type == basic_pb2.Person.MOBILE:
                print ("  Mobile phone #: ")
            elif phone_number.type == basic_pb2.Person.HOME:
                print ("  Home phone #: ")
            elif phone_number.type == basic_pb2.Person.WORK:
                print ("  Work phone #: ")
            print (phone_number.number)
  
if(len(sys.argv) != 2):
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)
address_book = basic_pb2.AddressBook()

f = open(sys.argv[1], 'rb')
address_book.ParseFromString(f.read())
f.close()

ListPeople(address_book)