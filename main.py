from blossom_lib import flower_definitions
from hash_map import HashMap


print('\nWelcome to the flower library! Learn what each flower means!\n')
print('Here are the flowers in our database:')
for flower in flower_definitions:
        print(flower[0])
print("Pick a flower to learn it's meaning! type in 'quit' to exit the program")

while True:
    user_input = input('Enter flower or command: ')
    if user_input.lower() == 'quit':
          break
    

        
