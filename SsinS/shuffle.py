import random

letters = ['a', 'b', 'c']
Letters = []

for i in range(0, 3):
    
    flag = True
    while flag:
        valor = random.randint(0,2);
        
        if letters[valor] not in Letters:
            Letters.append(letters[valor])
            flag = False

print(Letters)