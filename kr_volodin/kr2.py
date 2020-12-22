import time
import os

with open('earth.md', 'r') as f:

    while True:
        line = f.readline()
        while line != '```\n':
            print(line, end='')
            line = f.readline()
        time.sleep(0.31)
        print(50*'\n')
        #os.system('cls')
        #print('\r',end='')

