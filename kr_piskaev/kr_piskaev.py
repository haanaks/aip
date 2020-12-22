import random
import collections

numbers = []
for i in range(1000):
    numbers.append(str(random.randint(-10, 10)))
choice = int(input('Выберите метод(1 или 2)'))
if choice == 1:
    print(collections.Counter(numbers))
elif choice == 2:
    count = 0
    for z in range(-10, 10):
        for i in range(1000):
            if numbers[i] == str(z):
                count += 1
        print(f"'{z}': {count} ")
        count = 0
