# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте потоки.
# Используйте процессы.
# Используйте асинхронный подход.


from pathlib import Path
import time
import threading
import multiprocessing
import asyncio


def count_words(file: Path, start_time):
    with open(file, encoding='utf-8') as f:
        text = f.read()
        print(f"In file {file.name} {len(text.split())} words - {time.time() - start_time} ")


def task_threading(path: Path):
    start_time = time.time()
    files = [file for file in path.iterdir() if file.is_file()]
    threads = []
    for file in files:
        thread = threading.Thread(target=count_words, args=[file, start_time])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def task_multiprocessing(path: Path):
    start_time = time.time()
    files = [file for file in path.iterdir() if file.is_file()]
    processes = []
    for file in files:
        process = multiprocessing.Process(target=count_words, args=[file, start_time])
        processes.append(process)
        process.start()
    for thread in processes:
        thread.join()


async def task_async(path: Path):
    start_time = time.time()
    files = [file for file in path.iterdir() if file.is_file()]
    for file in files:
        with open(file, encoding='utf-8') as f:
            text = f.read()
            print(f"In file {file.name} {len(text.split())} words - {time.time() - start_time} ")


def main():
    Path(Path.cwd() / 'testfiles').mkdir(exist_ok=True)
    path = Path(Path.cwd() / 'testfiles')
    print('<< Потоки: >>')
    task_threading(path)
    print('<< Процессы: >>')
    task_multiprocessing(path)
    print('<< Асинхронный подход: >>')
    asyncio.run(task_async(path))


if __name__ == '__main__':
    main()
