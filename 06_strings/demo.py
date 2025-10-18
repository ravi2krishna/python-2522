# Strings 

# define single line strings 

# single quote
s1 = 'hello'
print(s1)

# double quote
s2 = "hello"
print(s2)

# triple quote
s3 = """hello"""
s4 = '''hello'''
print(s3)
print(s4)

# define multi line strings 

# address = "house no 90
# zip 500081
# city hyderabad
# state telangana
# country india"

address = """house no 90
zip 500081
city hyderabad
state telangana
country india"""

print(address)

address = '''house no 90
zip 500081
city hyderabad
state telangana
country india'''

print(address)

# need single quote in a string -> double quotes (" ")
question = "how are you ?"
# answer = 'i'm fine' # SyntaxError
answer = "i'm fine"
print(answer)

# need double quote in a string -> single quotes (' ')
question = "how are you ?"
# answer = "i"m fine" # SyntaxError
answer = 'i"m fine'
print(answer)

# need both single & double quotes -> triple quotes (''' ''')
question = "how are you ?"
# answer = " i"m fine i'm fine " # SyntaxError
answer = '''i"m fine i'm fine '''
print(answer)

# Access String 
text = "python"
print(text)

# Access Characters Using Index 
print(text[2]) # positive index 
print(text[-1]) # negative index 

# print(text[10]) # IndexError: string index out of range

# Access all characters 
text = "python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# using loops with string 
text = "python"

for char in text:
    print(char)
    
# len() will return number of items in a object which can be used with string 
text = "python"
print("Number Of Characters: ",len(text))