def divisible(ivalue):

    if((ivalue % 5) == 0):
        return True
    else:
        return False  

def main():
    Result = False

    print("Enter your number:")
    iNo = int(input())

    Result = divisible(iNo)

    if(Result == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()