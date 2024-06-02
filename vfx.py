openList = ["[", "{", "("]
closeList = ["]", "}", ")"]

myStr = "{([{[[(  )]]})}"
stack = []
  i in myStr:
    if i in openList:
        stack.append(i)
    elif i in closeList:
        pos = closeList.index(i)
        if stack and openList[pos] == stack[-1]:
            stack.pop()
        else:

            print("Unbalanced")
            break

if len(stack) == 0:
    print("balanced")


