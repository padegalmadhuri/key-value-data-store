# About the Key-value data store file

This is a file which can be exposed as a library that supports the basic CRD(create, read, write) operations. Data store is meant to local storage for one single process on single laptop.


# Importing
  Import the file dictionary
 ```
 import dictionary 
 ```

# Available Functions



#### create
It will create the key value data store (key is string and value is JSON object),Here 100 is time out(sec) and it is optional
```
dictionary.create("1",{"details":{"name":"Madhuri","Studying":"BE"}},100)

```

#### read 
It will get the value of the key in the datastore
```
print(dictionary.read("A"));

```
#### delete
It will delete the value by taking key.
```
dictionary.delete("A");
```

# Constraints
#### 1. With in timeout Read and Delete functions will available,after timeout Read and Delete will not applicable for the particular Key.
#### 2. The duplication of key is not possible.
#### 3. The size of the key will not exceed to 32chars.
#### 4. The size of the value is not exceed to 16KB.
#### 5. Multiple Threading is available


Go through the implementation file, to know the data store work flow. 




