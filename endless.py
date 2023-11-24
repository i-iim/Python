import threading



def calculate_sum(start, end):
    a = 0.0
    b = start

    while b != end:
        b = b + 1
        a = a + 1 / b
        print(a)

# Get the input from the user
c = int(input("Enter a number: "))

# Create four threads
threads = []
for i in range(4):
    start = 1
    end = c
    thread = threading.Thread(target=calculate_sum, args=(start, end))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()