from the3small import pattern_search

images = open("test_images")
patterns = open("test_patterns")

image=images.read().splitlines()
pattern=patterns.read().splitlines()

cevaps = []
for i in range(len(image)):
    print(i)
    cevap = pattern_search(pattern[i],image[i])
    cevaps.append(cevap)

print(cevaps)