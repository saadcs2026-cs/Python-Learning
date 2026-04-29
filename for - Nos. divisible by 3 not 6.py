# numbers divisible by 3 not by 6 till 100
numb = 1
for numb in range(1,101):
    if numb%3==0 and numb%6!=0:
        print(numb, end=",")
