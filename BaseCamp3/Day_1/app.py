import sys

def add(a,b):
    return a+b

print(add(5,3))

if __name__ == "__main__":
    print("This is a simple addition function.")
    _=sys.argv[0]
    x=sys.argv[1]
    y=sys.argv[2]
    print(f"Arguments passed: {_},{x} {y}")
    print(add(x,y))
    print(add(float(x),float(y)))