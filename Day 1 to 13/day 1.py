# DAY 1

# sorry I'm not printing hello world

print("starting python from today")

# for the single line we use comment and this is a comment

"""And for the paragraph 
we use docstring"""

# variable

a = 1
print(type(a))  # integer

b = 6.6
print(type(b))  # float (we can also use like 12/4)

c = 16j
print(type(c))  # complex (we can only use 'j')

# boolean (Boolean has only two values: True and False)

d = True
print(type(d))

e = False
print(type(e))

# string (we can use both "" and '')

question = "how are you"
print(type(question))

answer = 'Im fine'
print(type(answer))

# 1. Unicode - Unicode is a standard system that assigns a unique number (called a code point) to every character in every language, symbol, emoji, or special character — across the entire world.

python = "🐍"
print(ord(python))  # so Unicode of 🐍 is 128013

reverse = 128013
print(chr(reverse))  # with chr we can find character from Unicode

# 2. Index - we can use index for printing the specific letter we want

o = "DND"
print(o[0],o[1],o[2])  # here we assigned each letter from 0 to 2

print(o[-1], o[-2], o[-3])  # here we assigned negative index to print from backward

# slicing string

K = "i got error"
print(K[2:6:1])

# 3. Type conversion - there are two types of type conversion

# 3.1 Implicit type conversion - where Python automatically changes the type of one variable to another

score = 12
print(score / 2)  # here Python converted integer into float

# 3.2 Explicit conversion - where we manually change the type

marks = 12
marks = str(marks)
print(type(marks))  # here we converted integer to string

# we can convert almost anything from one type to another, but there are rules

V = "real"
print(bool(V))  # here for Boolean everything is True except some values

# these values will always be False no matter what:

aa = False
print(bool(aa))

bb = 0
print(bool(bb))

cc = 0.0
print(bool(cc))

dd = ""
print(bool(dd))

ee = ()
print(bool(ee))

ff = []
print(bool(ff))

gg = {}
print(bool(gg))

# these seven are the ones that will always be False — thala for a reason

# enough for today I guess
