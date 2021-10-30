"""
Дан массив A[0,...,N-1]A[0,…,N−1].
Реализуйте функцию cumsum_and_erase(...), принимающую один обязательный аргумент A
и один опциональный аргумент erase, по умолчанию равный 1.

Функция должна выполнять следующие действия:

сформировать массив B[0,…,N−1], где B_i = A0 + ... + Ai -- массив частичных сумм массива A;
удалить из массива B все элементы, равные параметру erase; получить массив C;
вернуть C в качестве ответа

Постарайтесь сделать это за время O(N) без использования Numpy.
"""


def cumsum_and_erase(lst, erase=1):
    answer = []
    sm = 0
    for element in lst:
        sm += element
        if sm != erase:
            answer.append(sm)
    return answer


A = [5, 1, 4, 5, 14]
B = cumsum_and_erase(A, erase=10)
assert B == [5, 6, 15, 29], "Something is wrong! Please try again"

