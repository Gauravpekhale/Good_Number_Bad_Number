"""
Program To find a number is good or bad ;

"""


"""
function name : Is_Digit_7()
Work          : Check That a given Number Contain 7 as a digit 
Return        : Boolean value True/False
"""
def Is_Digit_7(n):
    flag=False
    while n>0:
        if n%10==7:
            flag=True
            break
        n=n/10
    return flag
"""
function name : Is_Good_Number()
Work          : Check the number is divisible and not contain 7 as a digit in that number.  
Return        : Boolean value True/False

"""
def Is_Good_Number(n):
    Decision=False
    if n % 7 ==0 and not Is_Digit_7(n):
        Decision=True
    return Decision
"""
function name : main()
Work          : Entry Point function
Return        : none
"""
def main():
    n=int(input())
    decision=Is_Good_Number(n)
    print(decision)
"""
Starter Of main thread : 
"""
if __name__=="__main__":
    main()

# Output of Above Code
"""
INPUT : 14
OUTPUT:True

INPUT : 7
OUTPUT:False

INPUT : 21
OUTPUT:True

INPUT : 700
OUTPUT:False

"""