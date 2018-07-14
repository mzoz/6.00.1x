# method 1
i = 0
j = -1
result = ""

while j+1 < len(s):
    if s[j] <= s[j+1]:
    	if (j+1 - i + 1) > len(result):
    		result = s[i:j+2]
    else:
        i = j+1
    j += 1

print("Longest substring in alphabetical order is: " + result)

# method 2
i = 0
j = 1
l = len(s)
result = ""

while j < l:
    if s[j-1] > s[j]:
        temp = s[i:j]
        if len(temp) > len(result):
            result = temp
        i = j
    j += 1
else:	# "abc" - "abc"
    if i == 0:
        result = s
print("Longest substring in alphabetical order is: " + result)

