ans = 42
#data = np.genfromtxt("kr1.txt", delimiter='\n', dtype=np.float)
data = []
n = int(input('Введите кол-чо чисел'))
with open('kr1.txt', 'r') as f:
    for i in range(n):
        data.append(float(f.readline()))
for number in data:
    ans += 1/number
print(ans)
