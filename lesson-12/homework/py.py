import threading

def is_prime(n=int):
    if n < 2:        
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end, result_list):
    local_primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            local_primes.append(i)
    result_list.extend(local_primes) 

start = int(input("Input starting position: "))
end = int(input("Input ending position: "))
thread_count = int(input("Enter the number of threads: "))
prime_numbers = []

total_numbers = end - start + 1
chunk_size = total_numbers // thread_count
threads = []

# Разделяем диапазон между потоками
for i in range(thread_count):
    sub_start = start + i * chunk_size
    # последний поток берёт всё, что осталось
    sub_end = start + (i + 1) * chunk_size - 1 if i != thread_count - 1 else end

    t = threading.Thread(target=find_primes_in_range, args=(sub_start, sub_end, prime_numbers))
    threads.append(t)
    t.start()

# Ждём завершения всех потоков
for t in threads:
    t.join()

print(prime_numbers)
