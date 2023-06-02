from blossom_lib import flower_definitions
from hash_map import HashMap

flower_hash = HashMap(len(flower_definitions))
for element in flower_definitions:
  flower_hash.assign(element[0], element[1]) 


print('\nWelcome to the flower library! Learn what each flower means!\n')
print('Here are the flowers in our database:')
for flower in flower_definitions:
        print(flower[0])
print("Pick a flower to learn it's meaning! type in 'quit' to exit the program\n")

while True:
    user_input = input('Enter flower or command: ').lower()
    if user_input.lower() == 'quit':
        break
    flower_data = flower_hash.retrieve(user_input)
    if flower_data is None:
        print('\n Sorry, that flower is not in our database, try again.\n')
    else:
        print(f"\nThe {user_input} symbolizes {flower_data}!\n")
