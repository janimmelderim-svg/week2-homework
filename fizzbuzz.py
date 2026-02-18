import sys
if len(sys.argv)<2:
    print("jāievada skaitlis, kas ir lielāks par 1")
    sys.exit(1)
try:
    N=int(sys.argv[1])
    if N<=0:
        raise ValueError("jāievada pozitīvs skaitlis")
except ValueError:
    print("jāievada pozitīvs skaitlis, kas lielāks par 1")
    sys.exit(1)
for i in range(1, N+1):
    if i%3==0 and i%5==0 and i%9==0:
        print("FizzBuzzJazz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%9==0:
        print("Jazz")
    else:
        print(i)