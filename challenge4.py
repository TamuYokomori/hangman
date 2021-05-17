# output all each words contained of a tring: kamyu

a = "kamyu"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])


# write a program asking to input two strings.
# make a new string that have two place buried with above strings for each.

what = input("What did you write?:")
who = input("Who did you send it?:")

b = "I wrote {} yesterday, and sent {} it!".format(what,who)
print(b)


# replace the top character of designed string: "aldous Huxley was born in 1894."

c = "aldous Huxley was born in 1894.".title()
print(c)


# split the string: "Where? Who? "When?" by using method, and make the list.

d = "Where? Who? When?".split(" ")
print(d)


# connect the stings of list:["The", "fox", "jumped", "over", "the", "fence", "."]
# as to be a correct English string.
# needed spaces between words, no needed on the front space of period.

e = ["The", "fox", "jumped", "over", "the", "fence", "."]
f = " ".join(e)
f = f[0:-2] + "."
print(f)


# replace "s" to "$": "A screaming comes across the sky."

g = "A screaming comes across the sky."
g = g.replace("s", "$")
print(g)


# by using method, search the first "m" on the string: "Hemingway"

h = "Hemingway"
h = h.index("m")
print(h)


# make a string with your favorite speech and quote character.

i = "Steve Jobs said \"Connect the dots\"."
print(i)


#　join strings with (+) to make "three three three", and with (*) as well.

j = "three" + " three" + " three"
k = "three " * 3
k = k.strip()
print(j)
print(k)


# slice  string: "on a fine and cold day on April, any clocks hit 13:00."
# make a part string until the front of ","

l = "it was a bright cold day in April, and the clocks were striking thirteen."
l = l[:33]
print(l)
