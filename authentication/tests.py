# a = 3487654
# 1

# a = 34567
# 7

# 12345
# a = input("num: ").split()
# b = []
# for i in a:
#     b.append(int(i))
#     if sum(b) >= 10:
#         print(b)
#


# numbers = input("num: ").split()
# numbers = list(map(int, numbers))
# sum_numbers = sum(numbers)
# if sum_numbers <= 10:
#     print(sum_numbers)
# else:
#     print(False)
# numbers = list(map(int, sum(numbers)))

# numbers_count = []
# for number in numbers:
#     numbers_count.append(number)
#     print(numbers_count)


numbers = list(map(int, input("num: ").split()))
sum_numbers = 0
final_list = []
for num in numbers:
    if sum_numbers + num <= 10:
        sum_numbers += num
        final_list.append(num)
    else:
        break
print(final_list)
print(sum_numbers)
