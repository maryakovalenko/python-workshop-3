test_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(f"список: {test_list}")
test_item = input("Введите искомую строку: ")

def check_list(test_list, test_item):
    count = 0
    for i in range(len(test_list)):
        if test_list[i] == test_item:
            count += 1
            if count == 2:
                return i
    else:
        return -1

print(f"ответ: {check_list(test_list, test_item)}")