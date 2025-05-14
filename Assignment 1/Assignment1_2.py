def ChkNum():
      print("Enter a number")
      Value1 = int(input())

      if((Value1 % 2) == 0):
          print("Even Number")
      else:
          print("Odd Number")
      
def main():
     ChkNum()

if __name__ == "__main__":
    main()