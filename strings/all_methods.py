#1 capitalize()
text = 'HELLO'
print(text.capitalize())

#2 casefold()
text = 'MARIo'
text2 = 'maRIO'
print(text.casefold())
print(text2.casefold())


#3 center(within_spaces_or_char)
text = 'Luigi'
print(text.center(20))
print(text.center(20,'.'))


#4 count(substring)
text = 'abc_abc_acd'
print(text.count('ab'))


#5 encode(string_to_bytes)
text = 'Pamela Anderson'
print(text.encode(encoding='UTF-8', errors='strict'))


#6 endswith(letter_or_tuple)
text = 'apple'
print(text.endswith('e'))
print(text.endswith(('e','a')))


#7 expandtabs()
text = 'text\ttext2\ttext3'
spaces = 20
print(text.expandtabs(spaces))


#8 find(substring) -> position or -1
text = 'Remember to comment and subscribe!'
position = text.find('subscribe')
print(text[position:])


#9 format(keywords)
text = '{subject} is doing: {action}.'
print(text.format(subject='Cat', action='meow'))
text = '{} is doing: {}.'
print(text.format('Cat', 'meow'))


#10 format_map()
coordinates = {'x':10, 'y':-5}
text = 'Coordinates: {x}, {y}'
print(text.format_map(coordinates))


#11 index(substring) throws ValueError
text = 'Astronauts recently discovered a banana on the moon?'
position = text.index('banana')
print(text[position])


#12 isalnum(string) -> boolean
text = 'alphanumeric123'
print(text.isalnum())


#13 isalpha(string)
text = 'hellokitty123'
print(text.isalpha())

#14 isascii(string)
text = 'hellokitty123'
print(text.isascii())


#15 isdecimal() # If a string is a decimal, it also a digit, and numeric
text = '123'
print(text.isdecimal())

#16 isdigit() # if a string is a digit, then it is also numeric
text = '①②③④⑤⑥'
print(text.isdigit())

#17 isnumeric()
text = '①②③④⑤⑥'
print(text.isnumeric())


#18 isidentifier()
text = 'test-sample'
print(text.isidentifier())

#19 islower()
text = 'Abc'
print(text.islower())


#20 isprintable()
text = 'text\n'
print(text.isprintable())


#21 isspace()
text = '   '
print(text.isspace())


#22 istitle()
text = 'The Video'
print(text.istitle())

#23 isupper()
text = 'BANANAS'
print(text.isupper())

#24 join()
text = '-'
print(text.join(['text1', 'text2', 'text3']))


#25 ljust()
text = 'text'
print(text.ljust(20, '_'))


#26 lower()
text = 'HELP'
print(text.lower())

#27 lstrip()
text = 'Some text.'
print(text.lstrip('Some'))

#28 & 29 maketrans() & translate()
# create a translation table
text = 'That is Bacon.'
table = text.maketrans('B', '✅')

# use the translation table
print(table)
print(text.translate(table))


#30 partition()
text = 'a+b=c'
print(text.partition('='))

#31 removeprefix()
text = 'Wazzup'
print(text.removeprefix('Wazz'))

#32 removesuffix()
text = 'Mister Everyone'
print(text.removesuffix('one'))


#33 replace()
text = 'Remember to comment!'
limit = 1 # 1st occurrence
print(text.replace('comment', 'subscribe', limit))

#34 rfind()
text = 'A: Some text. A'
# Rightmost
position = text.rfind('A')
print(position)


#35 rindex()
text = 'B: Some text. B'
print(text.rindex('B'))

#36 rjust()
text = 'text'
# fill n spaces and fill remainder with char
print(text.rjust(20, '_'))

#37 rpartition()
text = 'text=text2=text3'
print(text.rpartition('='))

#38 & 39 rsplit() & rsplit()
text = 'This is some special stuff.'
print(text.rsplit(sep=' '))
print(text.split(maxsplit=2))
print(text.rsplit(maxsplit=2))

text = 'www.website.com'
print(text.split(sep='.'))

#40 rstrip()
text = 'His name is Mario Mario'
# strips off the rightmost match
print(text.rstrip('Mario'))

#41 splitlines()
text = 'Remember to comment!\nor else...\n'
print(text.splitlines())
print(text.splitlines(keepends=True))

#42 startsWith()
text = 'Luigi'
print(text.startswith('L'))

#43 strip()
text = 'Luigi has pasta.'
print(text.strip('Luigi'))

#44 swapcase()
text = 'Luigi has pasta.'
print(text.swapcase())

#45 title()
text = 'this is a title'
print(text.title())

#46 upper()
text = 'this is a title'
print(text.upper())

#47 zfill()
text = 'text'
# Pad with zeros
print(text.zfill(20))

