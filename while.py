# i = 7
# for x in range(i):
#     for j in range(i - x - 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()
# for x in range(i - 1, 0, -1):
#     for j in range(i - x):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()


# def print_diamond(rows):
#     for i in range(rows):
#         for j in range(rows - i - 1):
#             print(" ", end="")
#         for j in range(i + 1):
#             print("*", end=" ")
#         print()

#     for i in range(rows - 1, 0, -1):
#         for j in range(rows - i):
#             print(" ", end="")
#         for j in range(i):
#             print("*", end=" ")
#         print()


# rows = int(input("Masukkan jumlah baris: "))
# print_diamond(rows)


row = 8
for x in range(row):
    for y in range(row - x - 1):
        # print(x, y, end=" ")
        print(" ", end="")
    for y in range(x+1):
        print("*", end=" ")
    print()
for x in range(row - 1, 0, -1):
    for y in range(row - x):
        print(" ", end="")
    for y in range(x):
        print("*", end=" ")
    print()

a = 5
for x in range(a):
    print(x)
