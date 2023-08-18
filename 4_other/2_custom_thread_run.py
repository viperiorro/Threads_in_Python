import threading
import time

class TeaMakerThread(threading.Thread):
    def __init__(self, cup_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cup_number = cup_number

    def run(self):
        print(f"Starting to make tea {self.cup_number}")
        time.sleep(2)
        print(f"Finished making tea {self.cup_number}")

class WaterBoilerThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        print("Starting to boil water")
        time.sleep(5)
        print("Finished boiling water")

def main():
    num_cups = 5
    tea_threads = []

    # Create and start tea maker threads
    for i in range(1, num_cups + 1):
        tea_thread = TeaMakerThread(i)
        tea_threads.append(tea_thread)
        tea_thread.start()

    # Create and start a water boiler thread
    water_boiler_thread = WaterBoilerThread()
    water_boiler_thread.start()

    # Wait for all tea maker threads to finish
    for tea_thread in tea_threads:
        tea_thread.join()

    # Wait for the water boiler thread to finish
    water_boiler_thread.join()

    print("All tasks have been completed!")

if __name__ == "__main__":
    main()