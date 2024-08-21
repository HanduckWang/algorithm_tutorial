k = int(input())
s = input()

s = s[len(s)-k:] + s[:len(s)-k]
print(s)

