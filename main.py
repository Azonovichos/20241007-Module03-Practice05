# Module 3 Practice 5

def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1:

        return first * get_multiplied_digits(int(str_number[1:]))

    if first != 0:
        return first

    return 1

a = 0
if a == 0:
    print(a)
else:
    result = get_multiplied_digits(a)
    print(result)

'''result = get_multiplied_digits(0)
print(result)'''