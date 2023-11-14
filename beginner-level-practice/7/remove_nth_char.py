s = "hello"
n = 1
new_s = ""

if (not s) or (n >= len(s)):
    print(s)
else:
    for i in range(len(s)):
        if i != n:
            new_s += s[i]

print(new_s)
