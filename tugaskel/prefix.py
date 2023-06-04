import time


def infix_to_prefix(infix_expr):
    # Membalikkan string infix
    infix_expr = infix_expr[::-1]

    # Membuat kamus untuk presedensi operator
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Membuat tumpukan dan daftar untuk menyimpan hasil konversi
    stack = []
    prefix_expr = []

    # Melakukan iterasi pada setiap karakter dalam ekspresi infix
    for char in infix_expr:
        # Jika karakter adalah operand, tambahkan ke hasil konversi
        if char.isalnum():
            prefix_expr.append(char)
        # Jika karakter adalah tanda kurung tutup, masukkan ke dalam tumpukan
        elif char == ')':
            stack.append(char)
        # Jika karakter adalah tanda kurung buka, keluarkan operator dari tumpukan
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix_expr.append(stack.pop())
            stack.pop()
        # Jika karakter adalah operator, keluarkan operator dengan presedensi yang lebih tinggi dari tumpukan
        else:
            while stack and operators.get(stack[-1], 0) > operators.get(char, 0):
                prefix_expr.append(stack.pop())
            stack.append(char)

    # Menambahkan operator yang tersisa dari tumpukan ke hasil konversi
    while stack:
        prefix_expr.append(stack.pop())

    # Membalikkan hasil konversi untuk mendapatkan ekspresi prefix yang benar
    prefix_expr = prefix_expr[::-1]

    # Menggabungkan semua karakter menjadi satu string
    prefix_expr = ''.join(prefix_expr)

    return prefix_expr


# Contoh penggunaan program
while True:
    print("="*20, "Konversi Infix - Prefix", "="*20), time.sleep(0.8)
    print("="*26, "Kelompok 4", "="*27), time.sleep(0.8)
    try:
        infix_expression = input("Masukkan ekspresi infix: ")
        prefix_expression = infix_to_prefix(infix_expression)
        print("Ekspresi prefix: ", prefix_expression)
    except ValueError:
        print("inputkan yang benar")
    except KeyboardInterrupt:
        exit = input("Anda yakin untuk keluar dari program? [y/n]")
        if exit == "y":
            print("Bye!")
            break
