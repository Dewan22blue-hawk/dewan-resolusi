# import time
# import os

# # Tugas konversi infix ke prefix kelompok 5
# # By. Dewan


# def infix_to_prefix(infix_expr):
#     # Membalikkan string infix
#     infix_expr = infix_expr[::-1]

#     # Membuat kamus untuk presedensi operator
#     operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

#     # Membuat tumpukan dan daftar untuk menyimpan hasil konversi
#     stack = []
#     prefix_expr = []

#     # Melakukan iterasi pada setiap karakter dalam ekspresi infix
#     for char in infix_expr:
#         # Jika karakter adalah operand, tambahkan ke hasil konversi
#         if char.isalnum():
#             prefix_expr.append(char)
#             print(prefix_expr)

#         # Jika karakter adalah tanda kurung tutup, masukkan ke dalam tumpukan
#         elif char == ')':
#             stack.append(char)
#             print(stack)
#         # Jika karakter adalah tanda kurung buka, keluarkan operator dari tumpukan
#         elif char == '(':
#             while stack and stack[-1] != ')':
#                 prefix_expr.append(stack.pop())
#             stack.pop()
#         # Jika karakter adalah operator, keluarkan operator dengan presedensi yang lebih tinggi dari tumpukan
#         else:
#             while stack and operators.get(stack[-1], 0) > operators.get(char, 0):
#                 prefix_expr.append(stack.pop())
#             stack.append(char)

#     # Menambahkan operator yang tersisa dari tumpukan ke hasil konversi
#     while stack:
#         prefix_expr.append(stack.pop())

#     # Membalikkan hasil konversi untuk mendapatkan ekspresi prefix yang benar
#     prefix_expr = prefix_expr[::-1]

#     # Menggabungkan semua karakter menjadi satu string
#     prefix_expr = ''.join(prefix_expr)

#     return prefix_expr


# # program utama
# while True:
#     print("="*20, "Konversi Infix - Prefix", "="*20), time.sleep(0.8)
#     print("="*26, "Kelompok 4", "="*27), time.sleep(0.8)
#     try:
#         infix_expression = input("Masukkan ekspresi infix: ")

#         prefix_expression = infix_to_prefix(infix_expression)
#         print("Bentuk Ekspresi prefix: ", prefix_expression)

#     except ValueError:
#         print("inputkan yang benar")
#     except KeyboardInterrupt:
#         exit = input("\nAnda yakin untuk keluar dari program? [y/n]")
#         if exit == "y" or "Y":
#             print("Bye!")
#             break

# import time
import os


def infix_to_prefix(infix_expr):

    # Mengubah spasi menjadi tidak ada spasi dengan method replace()
    infix_expr = infix_expr.replace(" ", "")
    # Membalikkan string infix
    infix_expr = infix_expr[::-1]
    print(infix_expr)

    # Membuat array untuk memberikan nilai presedensi pd masing-masing operator (urutan prioritas dari operator)
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Membuat variabel stack yang digunakan sebagai sebuah list kosong dan daftar untuk menyimpan hasil konversi
    stack = []
    prefix_expr = []

    # Melakukan iterasi pada setiap karakter dalam ekspresi infix
    for char in infix_expr:
        # Jika karakter adalah operand, tambahkan ke hasil konversi
        if char.isalnum():
            prefix_expr.append(char)
            print("ini bagian if = ", prefix_expr)
        # Jika karakter adalah tanda kurung tutup, masukkan ke dalam list stack
        elif char == ')':
            stack.append(char)
            print("ini bagian Elif ) = ", stack)
        # Jika karakter adalah tanda kurung buka, keluarkan operator dari tumpukan list
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix_expr.append(stack.pop())
                print("ini bagian while di elif = ", prefix_expr)
            stack.pop()
            print("ini bagian Elif ( =", stack)
        # Jika karakter adalah operator, keluarkan operator dengan presedensi yang lebih tinggi dari tumpukan list
        else:
            while stack and operators.get(stack[-1], 0) > operators.get(char, 0):
                prefix_expr.append(stack.pop())
                print("ini bagian while di else = ", prefix_expr)
            stack.append(char)
            print("ini bagian Else", stack)

    # Menambahkan operator yang tersisa dari tumpukan ke hasil konversi
    while stack:
        prefix_expr.append(stack.pop())
        print("ini adalah while stack akhir =", prefix_expr)
    # Membalikkan hasil konversi untuk mendapatkan ekspresi prefix yang benar
    prefix_expr = prefix_expr[::-1]

    # Menggabungkan semua karakter menjadi satu string
    prefix_expr = ''.join(prefix_expr)

    return prefix_expr


# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Contoh penggunaan program
while True:
    # clear_screen()

    print("="*20, "Konversi Infix - Prefix", "="*20)
    print("="*26, "Kelompok 4", "="*27)
    try:
        infix_expression = input("Masukkan ekspresi infix: ")
        # clear_screen()

        prefix_expression = infix_to_prefix(infix_expression)
        print("Ekspresi prefix:", prefix_expression)

        # time.sleep(20)  # Tunggu 2 detik sebelum membersihkan layar
        # clear_screen()

    except ValueError:
        print("Input yang Anda masukkan salah.")
        # time.sleep(2)  # Tunggu 2 detik sebelum membersihkan layar
        clear_screen()

    except KeyboardInterrupt:
        exit = input("\nAnda yakin ingin keluar dari program? [y/n]")
        if exit.lower() == "y":
            print("Bye!")
            break
