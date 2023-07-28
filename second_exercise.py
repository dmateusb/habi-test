import random

def sort_array(list):
    sorted_lists = []
    current_lists = []

    for block in list:
        if block == 0:
            if not current_lists:
                sorted_lists.append("X")

            else:
                current_lists.sort()
                sorted_lists.append("".join(str(n) for n in current_lists))

            current_lists = []
        else:
            current_lists.append(block)

    if current_lists:
        current_lists.sort()
        sorted_lists.append("".join(str(n) for n in current_lists))
    else:
        sorted_lists.append("X")

    return " ".join(sorted_lists)


myArray = [random.randint(0,4) for i in range(20)]
print(myArray)
print(sort_array(myArray))



