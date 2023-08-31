"""
3.1 Design a basic hash function. Here I have designed a custom hash function. The built in python function hash() takes an object as an arguement and returns a hash value.
Then it calculates the index by taking the remainder of the hash code divided by the array size.  
The 'data' parameter is the data that I will hash.
The 'array_size' parameter sets the size of the hash table.

def custom_hash (data, array_size):
hash_code = hash(data)
index = hash_code % array_size
return index

3.2 Walkthrough with No Hash Collision

Next, using the insert() function, I created a hash table with key-value pairs.
Here there are no collisions as each key maps to a unique index in the hash table.
I created the table with 10 empty slots. The custom_hash() function determins the index for each key. 

hash_table = [None] * 10  

insert(hash_table, "shoes", "trainers")        # Hashes to index 4
insert(hash_table, "jacket", "leather")        # Hashes to index 1
insert(hash_table, "sunglasses", "black")      # Hashes to index 6
insert(hash_table, "hat", "beanie")            # Hashes to index 3

print(hash_table)

3.3 Walkthrough with Hash Collision

Here, using a similar layout as earlier, I have two different keys hash to the same index. 
I created an empty hash table with 7 slots this time. 
A collision is caused with the previous entry and it hashes to an index of 0.
If I was to fix this collision I would use a linear probing or open addressing method.

def custom_hash (data, array_size):
hash_code = hash(data)
index = hash_code % array_size
return index
hash_table = [None] * 7
insert(hash_table, "jacket", "jacket")
insert(hash_table, "hat", "hat")
print(hash_table)

"""

