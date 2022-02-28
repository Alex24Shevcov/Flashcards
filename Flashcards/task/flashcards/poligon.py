arr = ['"Russia"', '"France"']
s = ""
for i in arr:
    s += i + ", "
s = s[:len(s) - 2]

print('The hardest cards are ' + s + ". You have 10 errors answering them.")
