import threading
import sys
from threading import*
from sys import getsizeof
import time
import json

def is_json(myjson):
  try:
    json_object = json.dumps(myjson,indent=10)
    json_obj = json.loads(json_object)
  except ValueError as e:
    return False
  return True

d={} #'d' is the dictionary in which we store data


#for create operation 
def create(key,value,timeout=0):
    if key in d:
        print("error: this key ",key," already exists")
    else:
        if(key.isalpha() and is_json(value)):
            if len(d)<(1024*1024*1024) and getsizeof(value)<(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

#for read operation
          
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of ",key," has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation


def delete(key):
    if key not in d:
        print("error: given key",key," does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key",key ,"is successfully deleted")
            else:
                print("error: time-to-live of ",key," has expired") 
        else:
            del d[key]
            print("key ",key," is successfully deleted")

