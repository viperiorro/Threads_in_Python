import unittest

from increase_number_in_file import *

class TestReadAndIncreaseFixed(unittest.TestCase):
    file_name = "../4_other/number.txt"

    def setUp(self) -> None:
        write_number(self.file_name, 0)

    def test_thread_conflict(self):
        self._test_counter(increase_number_in_file)

    def test_lock(self):
        self._test_counter(increase_number_in_file_with_counter_lock)

    def test_semaphore(self):
        self._test_counter(increase_number_in_file_with_counter_semaphore)


    def _test_counter(self, func):
        increasing_number = 100
        threads_number = 10

        # Create threads list
        # Each thread will increase the number in the file by [increasing_number] times
        thread_list = []
        for _ in range(threads_number):
            thread = threading.Thread(target=func,
                                      args=(self.file_name, increasing_number))
            thread_list.append(thread)

        # Start threads
        for thread in thread_list:
            thread.start()

        # Wait for threads to finish
        for thread in thread_list:
            thread.join()

        # Check the final number
        result = read_number(self.file_name)

        # Expected result
        expected_result = increasing_number * threads_number

        # Print results
        print(f"Expected number: {expected_result}")
        print(f"Final number: {result}")

        # Check the result
        self.assertEqual(expected_result, result, msg=f"Thread conflict issue: final number is {result}")


if __name__ == "__main__":
    unittest.main()