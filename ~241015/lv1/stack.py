import sys

n = int(sys.stdin.readline().strip())
stack = []
output = []

for _ in range(n):
    command = sys.stdin.readline().split()
    cmd_type = command[0]

    if cmd_type == "push":
        stack.append(int(command[1]))
    elif cmd_type == "pop":
        output.append(str(stack.pop()) if stack else "-1")
    elif cmd_type == "size":
        output.append(str(len(stack)))
    elif cmd_type == "empty":
        output.append("1" if not stack else "0")
    elif cmd_type == "top":
        output.append(str(stack[-1]) if stack else "-1")

print('\n'.join(output))
