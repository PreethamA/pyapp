import random
import time
import os
def generate_random_data():
    data = []
    for i in range(10):
        data.append(random.randint(1, 100))
    return data

if __name__ == "__main__":

    while True:
        time.sleep(30)
        print(os.getcwd())
        print(generate_random_data())