number_list = [1, 2, 3, 4, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222, 333, 444, 555, 666, 777, 888, 999
    , 9999]

pos = -1


def search(number_list, number):
    l = 0
    u = len(number_list) - 1

    while l <= u:

        mid = (l + u) // 2

        if number == number_list[mid]:
            globals()['pos'] = mid
            return True

        else:
            if number_list[mid] < number:
                l = mid + 1

            else:
                u = mid - 1

    return False


number = 99

if search(number_list, number):
    print(f'Your Value Is At {pos} Index')

else:
    print('Not In The List!')
