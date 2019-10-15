def CheckBalancedParenthesis(exp):
    n = len(exp)
    #Create a stack: - S
    S = []

    for i in range(n):
        if exp[i] in {'(','{','['}:
            S.append(exp[i])
        elif exp[i] in {')','}',']'}:
            if (len(S)== 0) or (S[-1] + exp[i] not in {'()','{}','[]'}):
                return False
            else: 
                S.pop()
    return len(S)== 0
str=input()
print(CheckBalancedParenthesis(str))
