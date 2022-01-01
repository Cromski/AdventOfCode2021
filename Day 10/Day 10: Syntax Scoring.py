with open("./smallData.txt") as file:
    haha = [xd.strip() for xd in file.readlines()]

allPossibleChars = ['[', ']', '(', ')', '{', '}', '<', '>']
print(haha)
result = 0

for j in range(len(haha)):
    stack = []
    for i in range(len(haha[j])):
        if i == 0:
            stack.append(haha[j][i])
            continue
        if haha[j][i] in ('[', '(', '<', '{'):
            stack.append(haha[j][i])
            continue

        if stack[-1] == '[' and haha[j][i] == ']':
            stack.pop()
            continue
        elif stack[-1] == '[' and haha[j][i] != ']':
            print("expected: ], but found: " + haha[j][i])
            if haha[j][i] == ')':
                result += 3
            elif haha[j][i] == '}':
                result += 1197
            else:
                result += 25137
            break

        if stack[-1] == '(' and haha[j][i] == ')':
            stack.pop()
            continue
        elif stack[-1] == '(' and haha[j][i] != ')':
            print("expected: ), but found: " + haha[j][i])
            if haha[j][i] == '>':
                result += 25137
            elif haha[j][i] == '}':
                result += 1197
            else:
                result += 57
            break

        if stack[-1] == '<' and haha[j][i] == '>':
            stack.pop()
            continue
        elif stack[-1] == '<' and haha[j][i] != '>':
            print("expected: >, but found: " + haha[j][i])
            if haha[j][i] == ')':
                result += 3
            elif haha[j][i] == '}':
                result += 1197
            else:
                result += 57
            break

        if stack[-1] == '{' and haha[j][i] == '}':
            stack.pop()
            continue
        elif stack[-1] == '{' and haha[j][i] != '}':
            print("expected: }, but found: " + haha[j][i])
            if haha[j][i] == ')':
                result += 3
            elif haha[j][i] == '>':
                result += 25137
            else:
                result += 57
            break

    if len(stack) != 0:
        for i in range(stack):
            if stack.index(stack[(i+1)]) == 1:
                
                allPossibleChars[stack.index(stack[-(i+1)])+1]






print(result)


