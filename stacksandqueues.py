def bracket_checker(string_from_user):
    stack = []
    for i in string_from_user:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif i == ')' or i == ']' or i == '}':
            if len(stack) == 0:
                return False
            popped = stack.pop()
            if not (popped == '(' and i == ')') and not (popped == '[' and i == ']') and not (popped == '{' and i == '}'):
                return False
    if len(stack) == 0:
        return True
    else:
        return False


from collections import deque

def print_binary(target):
    queue = deque(['1'])
    for i in range(target):
        next = queue.popleft()
        print(next)
        new = next + '0'
        new2 = next + '1'
        queue.append(new)
        queue.append(new2)
    print(queue)

print_binary(12)
