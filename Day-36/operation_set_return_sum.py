n = int(input())
s = set(map(int, input().split()))
operation_count = int(input())
for ops in range(operation_count):
    m = input().split()
    operation =m[0]
    try:
        if operation=='remove':
            s.remove(int(m[1]))
        elif operation=='discard':
            s.discard(int(m[1]))
        else: 
            s.pop()
    except KeyError as e:
        print(f"Error: {e}")

print(sum(s))