# call the elements of designed list.

a = ["Walking Dead", "Entorage", "The Sopranos", "Vampire Diaries"]
for show in a:
    print(show)


# call the each value from 25 to 50.

for i in range(25, 51):
    print(i)


# call elements of the above list with index value.

for i, show in enumerate(a):
    print(i)
    print(show)


# endless-roop program to guess the right numbers.
# end up when typed 'q' by users. call bool-value when typed numbers.
# make lists of right numbers.
# display 'correct' of 'incorrect' relying on user's numbers.
# display 'type any number of 'q' to quit this.' when typed something except nnumber or 'q'.

numbers = [12, 51, 55, 90, 94]

while True:
    answer = input("Guess a number, or 'q' to quit:")
    if answer == 'q':
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Please type a number or 'q' to quit!")
        continue
    if answer in numbers:
        print("YOU GUESSED CORRECTLY!")
    else:
        print("YOU GUESSED INCORRECTLY!")


# build new list from list1 * list2

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
multiplication = []

for i in list1:
    for j in list2:
        multiplication.append(i * j)
print(multiplication)
        
    
