text: str = 'I am a teapot'
text2: str = 'I am not a Teapot'

my_slice = slice(5, 10)  # Slice object
my_slice2 = slice(None, 10)
print(text[:10])
print(text[my_slice])

print(text[5:10])
print(text2[5:10])

print(text[my_slice])

# Reverse string
my_slice3 = slice(None, None, -1)
print(text[my_slice])
print(text[::-1])
