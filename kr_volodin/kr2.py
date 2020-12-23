import time
import os

#with open('earth.md', 'r') as f:

    #while True:
        #line = f.readline()
        #for n in range(1,14):
            #while line != '```\n' or line != '# n\n':
                #print(line, end='')
                #line = f.readline()
            #time.sleep(0.31)
        #print(50*'\n')
        #os.system('cls')
            #print('\r',end='')

line = 0



#while True:
    #line = input()
    #if line.startswith('```') or line.startswith('\n'):
        #print('\r',end='')
        #continue
    #else:
        #break
data = []
while True:
    try:
        line = input()
    except EOFError:
        print('')
    try:
        while True:
            if line.startswith('```') or line.startswith('#'):
                print('\033c', end='')
            elif line.startswith() != ('```') and line.startswith() != '#' and line.startswith() != ('\n'):
                data.append(line)
                print('\033c', end='')
            else:
                for l in data:
                    print(l, end='')
                print('\033c', end='')
                time.sleep(0.1)
                continue
    except KeyboardInterrupt:
        print('\nBye!')

line = 0
data = []
while True:
    line = input()
    if line.startswith('```') or line.startswith('\n'):
        print('\r',end='')
        continue
    else:
        break
while True
    line input()
