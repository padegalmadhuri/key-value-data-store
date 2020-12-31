import dictionary

dictionary.create("A",{"details":{"name":"Madhuri","Studying":"BE"}})
#to create a key with value given and with no time-to-live property


print(dictionary.read("A"));
#it returns the value of the respective key in JSONobject format


dictionary.create("AB",{"details":{"name":"Madhuri","Studying":"BE"}},100)
#to create a key with value given and with time-to-live property (number of seconds)


dictionary.create("A",{"name":"assign"})
#it returns an ERROR since the key_name already exists in the database
#To overcome this error use delete operation and recreate it


dictionary.delete("A");
#it deletes the key and its value from the database



##MULTIPLE THREADS

thread1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #any operation
thread1.start()
thread1.sleep()
thread2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #any operation
thread2.start()
thread2.sleep()
