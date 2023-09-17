'''
Transform all names to uppercase using [normal list - list comprehension - functional programming]
'''
"1--Normal List"
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

"1--normal list"
list_1=[]
for i in Names:
    list_1.append(i.upper())

print(list_1)
"====================="

"2--list comprehension"
x=str
list_2=[x.upper() for x in Names]
print(list_2)
"====================="

"3--functional programming"
for x in Names:

    upper_case=(lambda x:x)
    m=[upper_case(x.upper())]
    print(m)
"====================="    

'''
Get the names that contains 'a' in a list using [normal list - list comprehension - functional
programming]
'''

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# task 2
def contains_a(items):
    blank_list = []
    for i in items:
        if 'a' in i:
            blank_list.append(i)
    return blank_list
print(contains_a(Names))


def list_comprehension_2(items):
    return [i for i in items if 'a' in i]
print(list_comprehension_2(Names))

def check_contains_a(word):
    if 'a' in word:
        return word

functional_programming_2 = list(filter(check_contains_a, Names))
print(functional_programming_2)

"=============================="

'''
3. Get the names that starts with 't' in a list using [normal list - list comprehension - functional
programming]
'''

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']


def contain_t(namee):
    list_1=[]
    for i in namee:
        if 't' in i:
            list_1.append(i)
    return list_1    

print(contain_t(Names))        

def list_comprehenson(namee):
    return[i for i in namee if 't' in i]
print(list_comprehenson(Names))

def functional(namee):
    if 't' in namee:
       return namee
    
functional_programming=list(filter(functional,Names))
print(functional_programming)    

"======================================"

'''
5. Print a list contains the len of each word in the list using [normal list - list comprehension -
functional programming]
'''

"لو حضرتك شفت دي اشرحهالي"

"====================================="

# task 5
def task_5(items):
    lis_1 = []
    for i in items:
        lis_1.append(len(i))
    return lis_1
print(task_5(Names))


def list_comprehension_5(namee):
    return [len(i) for i in namee]
print(list_comprehension_5(Names))

functional_programming_5 = list(map(len, Names)) 
print(functional_programming_5)

"==================================="

'''
6. Unpack the list in
'''

print(Names.clear()) 

"=================================="

'''
7. a,b , a= the first index , b = rest of the list
'''

a,*b,_=Names
print(f"""
a={a}
b={b}
""")

"================================="

'''
8. a = the first index , b = the last index
'''
a,*_,b
print(f"""
a={a}
b={b}
      """)

"================================="

'''
9. a = the first index , b = the second index
'''
a,b,*c=Names
print(f"""
a={a}
b={b}
      """)