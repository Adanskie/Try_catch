from pathlib import Path

cats = Path('cats.txt')
dogs = Path('dogs.txt')

try:
    storage = [cats.read_text(),dogs.read_text()]

    for get_value in storage:
        print(get_value)

except FileNotFoundError:
    print("Sorry bro")
