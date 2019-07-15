#sentence case
sentence = "the quick brown fox jump over the lazy dog"
words = sentence.split()
print(words)
print([len(word) for word in words])

sen = "I raza is my best friend"
wrd = sen.split()
print([len(word) for word in wrd])
print("")


#positive numbers inthe list
print("POSITIVE NUMBERS")

def pos(e):
    return e % 2 > 0
    
numbers=[12,54,33,67,24,89,11,24,47]
i=list(filter(pos,numbers))
    
print(i)
print("")


#even numbers in the list
print("EVEN NUMBERS IN THE LIST")

def even(v):
    return v % 2 == 0
    
numbers=[12,54,33,67,24,89,11,24,47]
u=list(filter(even,numbers))
print(u)
print("")

# odd list from 1 - 50
def odd(o):
    return o % 2 == 1

number = range(1,50)
l=list(filter(odd,number))
print(l)
print("")
[n for n in range(1,51,1)]
print("")

#even list from
def even1(q):
    return q % 2 == 0

number = range(1,50)
w=list(filter(even1,number))
print(w)
print("")
[b for b in range(1,51,2)]
print("")


#tuple
    
'''wor = ["hello", "my", "name", "is", "sam"]
length = [len(word) for word in wor]
wr = [word.upper() for word in wor]
tuple (zip(wor, length))'''


def factorial (z):
    if z == 1:
        return 1
    else:
        return z*factorial(z - 1)
        
factorial(4)    



