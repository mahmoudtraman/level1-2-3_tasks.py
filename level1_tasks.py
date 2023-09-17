'''
Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range
'''

list_1=[]
list_2=[]
def odd_even(x,y):
    for i in range(x,y):
        if i%2==0:
            list_1.append(i)
        else:
            list_2.append(i)

a=int(input("Enter first Number : "))
b=int(input("Enter second Number : "))
odd_even(a,b)
print("list 1 = ",list_1)
print("list 2 = ",list_2)


"============================="

'''
Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y
'''
def num(x,y):
    list_1=[]
    for e in range(1,100):
        if e%x==0 and e%y==0:
            list_1.append(e)

    print("Numbers = ",list_1)        


a=int(input("First Number : "))
b=int(input("Second Number : "))
num(a,b)

"============================"
'''
Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
'''
def mul(x,y):
    for e in range(x,y+1):
        for m in range(1,13):
            print(f"{e}x{m} = ",e*m)
        print("============")         


a=int(input("Enter the Starter Number : "))       
b=int(input("Enter the Ending Number : "))       
mul(a,b)      


"================================="
'''
Create a function that takes a sentence and prints the sentence without duplicated words
'''
def sentence(sentences):
    words=sentences.split()
    list_1=[]
    for e in words:
        if e not in list_1:
            list_1.append(e)
        

    print(list_1)
    print(' '.join(list_1))



a=str(input("Enter The Sentences : "))
sentence(a)           
"====================================="


'''
Create a function that takes a sentence and prints how many words in the sentence (do not count the
spaces)
'''


def words(str):
    e=0
    for e in str:
        if (e==''):
            e+=1

    print(e) 



sentence=input("Enter the Sentences : ")           
words(sentence)

    
"==================================="

'''
Create a function that takes a sentence and word and remove the word from the sentence
'''

def word(sentence):
    word=input("Enter The Word you want To delete : ")
    sentence=sentence.replace(word , "")
    print(sentence)


text=input("Enter the Sentence : ")
word(text)

"===================================="

'''
Create a function takes a sentence and a word and prints how many time the word used in the sentence
'''


    
"============================"

'''
Create a function that takes x,y and prints all the number that can be divide by y from x to 100
'''

def devided(x,y):
    for i in range(x,100):
        if i%y==0:
            print(i)


a=int(input("Enter the starter Number : "))
b=int(input("Enter the devid Number : "))
devided(a,b)            
