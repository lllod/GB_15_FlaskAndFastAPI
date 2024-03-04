# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.


import random
import time
import threading
import multiprocessing
import asyncio


def list_gen():
    return [random.randint(1, 100) for _ in range(1000000)]


def elements_sum():
    num_list = list_gen()
    start_time = time.time()
    el_sum = sum(num_list)
    print(f'Elements sum: {el_sum}, time: {time.time() - start_time}')


def task_threading():
    thread = threading.Thread(target=elements_sum)
    thread.start()
    thread.join()


def task_multiprocessing():
    process = multiprocessing.Process(target=elements_sum)
    process.start()
    process.join()


async def task_async():
    num_list = list_gen()
    start_time = time.time()
    el_sum = sum(num_list)
    print(f'Elements sum: {el_sum}, time: {time.time() - start_time}')


def main():
    print('<< Потоки: >>')
    task_threading()
    print('<< Процессы: >>')
    task_multiprocessing()
    print('<< Асинхронный подход: >>')
    asyncio.run(task_async())


if __name__ == '__main__':
    main()
