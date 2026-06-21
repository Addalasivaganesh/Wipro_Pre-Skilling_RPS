
text = "aaaabbbccdddddddeeeeefffgghhijklmnnooppqqrrrssstttuuvvwwwwxxxyyyzz"

compressed = ""
count = 1

for i in range(len(text)-1):

    if text[i] == text[i+1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

compressed += text[-1] + str(count)
print(compressed)