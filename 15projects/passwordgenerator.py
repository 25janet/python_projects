import random
length = 12
upper_letters = ["A", "B", "C", "D", "E", "F" , "G" , "H", "I", "J", "K", "L", "M", "N", "O" ,  "P", "Q", "R" , "S", "T", "U", "V", "W", "Y", "Z"] 
lower_letters = ["a","b", "c", "d","e","f","g", "h","i", "j", "k", "l" ,"m","n","o", "p","q", "r","s", "t", "u", "v", "w","x","y","z"]
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ["!","@","#","$","%","^","&","*","(",")","[","]","|","<",">","?"]
def generate_password():
    password = [
        random.choice(upper_letters),
        random.choice(lower_letters),
        random.choice(numbers),
        random.choice(symbols),
        ]
    all_characters = upper_letters + lower_letters + numbers + symbols
    while len(password) < length:
        password.append(random.choice(all_characters))
        
    random.shuffle(password)
    final_password = ''.join(map(str,password))
    print(final_password)

generate_password()
