def min_text(item_list):
    count = 0
    word = item_list[0]
    for i in item_list:
        if i == word:
            count += 1
            item_list.remove(i)
    print(f"{word} = {count}")

input_text = "a aa abC aa ac abc bcd a"

input_text = input_text.lower()

new_list = input_text.split()

while len(new_list) != 0:
    min_text(new_list)