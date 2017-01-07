# функция, создающая  итератор разложения на  множители< 010
def decompose(number, start_from=2, set_=[]):
    if number < 10 and number >= start_from: yield set_ + [number]
    else:
        for j in range(start_from,10):
            if number % j == 0:
                for m in decompose(number//j, j, set_+[j]):
                    yield m

def reconstruct(number):
    # получаем все разложения
    all_decomps = decompose(number)
    # преобразуем их в строки, строки преобразуем в числа
    all_strings = map(lambda x: int("".join(map(str,x))),all_decomps)
    return min(all_strings)
