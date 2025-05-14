def stars():
    print("Enter your number:")
    value = int(input())

    for i in range(value):
        print("*",end="\t")

def main():
    stars()

if __name__ == '__main__':
    main()
