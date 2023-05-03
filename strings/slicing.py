# [start:stop:step]

s = "The quick brown fox jumped over the lazy dog."

print(s[:3])    # [0:3]
print(s[4:])    # [4:end]
print(s[::2])   # [0:end:2]
print(s[::-1])  # [0:end:-1]

print(s[-1:])   # last char
print(s[::-1])  # reverse

print(s[:-1:])  # everything EXCEPT last char

website1 = "http://google.com"
website2 = "http://wikipedia.com"

# Slice object
slice_obj = slice(7, -4)
print(website2[slice_obj])