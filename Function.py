u = "string"
def main():
    x=int(input ())
    y =int(input())

    z = x+y

    print(z)

def cap():
    global u 
    a = u.capitalize()
    print(a)

if __name__ == "__main__":
    main()
    cap()