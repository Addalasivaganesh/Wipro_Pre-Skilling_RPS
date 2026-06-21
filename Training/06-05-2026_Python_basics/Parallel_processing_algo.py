#multi processing algo

from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    with Pool(2) as p:
        result = p.map(square, numbers)
    print(result)