class maple:
    def __version__():
        return "1.0.0"
    def plus(x,y):
        print(x+y)
    def subtract(x,y):
        print(x-y)
    def multiply(x,y):
        print(x*y)
    def divide(x,y):
        print(x/y)
    def power(x,y):
        print(x**y)
    def sqrt(x):
        print(x**0.5)
    def factorial(x):
        result = 1
        for i in range(1, x+1):
            result *= i
        print(result)
    def fibonacci(x):
        a, b = 0, 1
        for i in range(x):
            a, b = b, a + b
        print(a)
    def prime(x):
        if x > 1:
            for i in range(2, int(x**0.5) + 1):
                if (x % i) == 0:
                    print(x, "is not a prime number")
                    break
            else:
                print(x, "is a prime number")
        else:
            print(x, "is not a prime number")
    def gcd(x,y):
        while y:
            x, y = y, x % y
        print(x)
    def lcm(x,y):
        lcm = (x*y)//gcd(x,y)
        print(lcm)
    def help():
        print("maple - a simple python maple library")
        print("version: " + maple.__version__())
        print("maple.add(x,y): add two numbers")
        print("maple.subtract(x,y): subtract two numbers")
        print("maple.multiply(x,y): multiply two numbers")
        print("maple.divide(x,y): divide two numbers")
        print("maple.power(x,y): raise x to the power of y")
        print("maple.sqrt(x): find the square root of x")
        print("maple.factorial(x): find the factorial of x")
        print("maple.fibonacci(x): find the nth fibonacci number")
        print("maple.prime(x): check if x is a prime number")
        print("maple.gcd(x,y): find the greatest common divisor of x and y")
        print("maple.lcm(x,y): find the least common multiple of x and y")
        print("maple.help(): print this help message")
        print("maple.exit(): exit the program")

