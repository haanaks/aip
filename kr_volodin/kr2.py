import time

line, data = 0, []
while True:
    try:
        line = input()
        if line.startswith('#') or line == '\n':
            continue
        data.append(line)
    except EOFError:
        break
while True:
    for l in data:
        try:
            if l.startswith('```'):
                #print('\033c',end='')
                print('\r', end='')
            print(l, end='')
            time.sleep(0.3)
        except KeyboardInterrupt:
            print('\nBye!')




