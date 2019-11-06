from statistics import mean
num1 = 1
num2 = 100
string = range(num1-1,num2+1)
rude = []
print(f"The average of list from {num1} to {num2} is {mean(string)}.")
for numList in string:
    meanT3MP = abs(mean(string)-numList)
    rude.append(meanT3MP)
print(f"The MAD is {mean(rude)}.")
print(rude)