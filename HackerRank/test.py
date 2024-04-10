

type = 'M'
words = 'mouse pad'

# splitWord = words.split('\n')
# words = splitWord[0]
i = 0


# remove spaces, and uppercase necessary characters
while i < len(words):
    if words[i] == ' ' and words[i + 1] and not i == 0:
        words[i + 1].upper()
        length = len(words)

        x = slice(i)
        words1 = words[x]

        x2 = (length * -1) + (i + 1)
        words2 = words[x2:]

        words = words1 + words2
    i += 1
    

print(words)