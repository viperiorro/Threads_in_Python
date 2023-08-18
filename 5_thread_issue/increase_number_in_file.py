import threading
import time

counter_lock = threading.Lock()  # Create lock object
counter_semaphore = threading.Semaphore(1)  # Create semaphore object


def read_number(filename):
    """Read number from file"""
    with open(filename, "r") as f:
        time.sleep(0.001)  # Simulate a long operation
        number = int(f.read().strip())
    return number


def write_number(filename, number):
    """Write number to file"""
    with open(filename, "w") as f:
        f.write(str(number))


def increase_number_in_file(filename, n):
    """
    Increase number in file by n times
    This function will cause thread conflict
    """
    for _ in range(n):
        number = read_number(filename)
        number += 1
        write_number(filename, number)


def increase_number_in_file_with_counter_lock(filename, n):
    """
    Increase number in file by n times
    Use lock to prevent thread conflict
    """
    for _ in range(n):
        with counter_lock:  # Use lock to prevent thread conflict
            number = read_number(filename)
            number += 1
            write_number(filename, number)


def increase_number_in_file_with_counter_semaphore(filename, n):
    """
    Increase number in file by n times
    Use semaphore to prevent thread conflict
    """
    for _ in range(n):
        with counter_semaphore:
            number = read_number(filename)
            number += 1
            write_number(filename, number)
