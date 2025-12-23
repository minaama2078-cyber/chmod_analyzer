permissions_map = {
    '0': '---',
    '1': '--x',
    '2': '-w-',
    '3': '-wx',
    '4': 'r--',
    '5': 'r-x',
    '6': 'rw-',
    '7': 'rwx'
}

chmod = input("Введите трехзначное восьмеричное число: ")

if len(chmod) != 3 or not chmod.isdigit():
    print("Ошибка: введите корректное трехзначное число.")
else:
    result = ""
    for digit in chmod:
        if digit in permissions_map:
            result += permissions_map[digit]
        else:
            print("Ошибка: число должно быть восьмеричным (0–7).")
            exit()
    print("Права доступа:", result)