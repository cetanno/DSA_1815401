dict = {'Name': 'DSA', "Semester":"22/23", "Time": "1 hour 30 minutes"}
dict2 = {}

print(dict)

#HOW TO GET DATA
print("dict['Name']:", dict['Name'])
print("dict['Time']:", dict['Time'])
print("dict['Semester']:", dict['Semester'])

#HOW TO UPDATE DATA
dict['Name'] = "CIE"
print("dict['Name']:", dict['Name'])

#HOW TO ADD DATA
dict['Lecturer'] = "Dr Rashidah"
print("dict['Lecturer']:", dict['Lecturer'])

#HOW TO REMOVE DATA
del dict['Time']
# print("dict['Time']:", dict['Time']) THIS WILL GIVE AN ERROR BECAUSE THE KEY IS REMOVED
dict.clear()
# print("dict['Lecturer']:", dict['Lecturer']) THIS WILL GIVE AN ERROR BECAUSE ALL THE KEYS ARE REMOVED
print(dict)
del dict2
# print(dict2) THIS WILL GIVE AN ERROR BECAUSE THE OBJECT IS NO LONGER EXIST

print("\n\nHASH TABLE")

class HashTable:
    # INIITIAL THE HASHTABLE
    def __init__(self,size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    # HASHING FUNCTIONS
    def hash(self,key):
        return key % self.size

    def rehash(self,key):
        return (key + 1) % self.size

    # GET THE DATA USING THE KEY
    def get(self,key):
        index = self.hash(key)

        # IF THE KEY IS FOUND IMMEDIATELY
        if self.keys[index] == key:
            return self.values[index]
        else:
            # GOING THROUGH THE TABLE TO FIND THE KEY
            oghash = index
            index = self.rehash(index)
            while index is not oghash:
                if self.keys[index] == key:
                    return self.values[index]
                else:
                    index = self.rehash(index)
            return None

    def __getitem__(self,key):
        return self.get(key)

    # PUT THE ITEM INTO THE HASH TABLE
    def put(self,key,value):
        index = self.hash(key)

        # IF THE INDEX POSITION HAS NO KEY OR THE SAME KEY REQUESTED
        if self.keys[index] is None or self.keys[index] is key:
            self.keys[index] = key
            self.values[index] = value
            return
        else:
            # GOING THROUGH THE TABLE TO FIND THE EMPTY SPOT OR THE KEY
            oghash = index
            index = self.rehash(index)
            while index is not oghash:
                if self.keys[index] is None or self.keys[index] is key:
                    self.keys[index] = key
                    self.values[index] = value
                    return
                else:
                    index = self.rehash(index)
            # IF THE TABLE IS ALREADY FULL
            print("The hash table is already full")

    def __setitem__(self,key,value):
        self.put(key,value)

#   def delete(self,key):

H = HashTable(7)

H[1] = "ECIE" #THE INDEX IS 1
H[20] = "KOE"
H[98] = "IIUM" #THE INDEX IS 0
H[5] = "DSA"

print(H.keys)
print(H.values)

H[15] = "LAB" #THE INDEX IS 1
H[7] = "PYTHON" #THE INDEX IS 0

print(H.keys)
print(H.values)

H[10] = "C++" #__setitem__
H[20] = "PHP"

print(H.keys)
print(H.values)

print(H[1]) #__getitem__
print(H[20])
print(H[30])

# H.delete(10)
