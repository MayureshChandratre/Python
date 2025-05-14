def main():
    print("Enter your Number")
    No = int(input())

    if(No < 0):
        print("Number is negative")
    elif(No > 0):
        print("Number is positive")
    else:
        print("Number is zero")

if __name__ == "__main__":
    main()