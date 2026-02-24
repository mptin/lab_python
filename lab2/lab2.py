def make_list(gap: list) -> list:
    ''' Получает два числа - границы промежутка и возвращает заполненный промежуток'''
    list1 = list(range(gap[0], gap[1]+1))
    return list1

def guess_number(type_of_alg: int, number: int, gap_list: list) -> list:
    '''Поиск числа в списке с помощью двух алгоритмов на выбор'''
    if number < gap_list[0] or number > gap_list[-1]:
      return None
    count_of_compare = 1
    #Алгоритм бинарного поиска в списке
    if type_of_alg == 2:
        st = 0
        fn = len(gap_list)-1
        mid = (st + fn) // 2
        while gap_list[mid] != number:
            if gap_list[mid] < number:
                st = mid + 1
            elif gap_list[mid] > number:
                fn = mid - 1
            count_of_compare += 1
            mid = (st + fn) // 2
    # Алгоритм медленного поиска в списке
    elif type_of_alg == 1:
        i = 0
        while gap_list[i] != number:
            i += 1
            count_of_compare += 1
    return gap_list[i], count_of_compare


