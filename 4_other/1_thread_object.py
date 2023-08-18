import threading
from time import sleep

def make_tea():
    for i in range(5):
        print(f"Making tea {i+1}")
        sleep(0.1)


# Create a new thread for making tea
tea_thread = threading.Thread(target=make_tea, name="TeaThread")

# Display main thread information
print("Main thread information")
print(f" - Main thread name: {threading.main_thread().name}")
print(f" - Is thread alive? {threading.main_thread().is_alive()}")
print(f" - Is thread a daemon? {threading.main_thread().daemon}")
print(f" - Thread ID: {threading.main_thread().ident}")
print()

# Display thread information before starting
print("Thread information before starting")
print(f" - Thread name: {tea_thread.name}")
print(f" - Is thread alive? {tea_thread.is_alive()}")
print(f" - Is thread a daemon? {tea_thread.daemon}")
print(f" - Thread ID: {tea_thread.ident}")
print()

# Start the thread
print("Starting thread")
tea_thread.start()

# Display thread information after starting
sleep(0.5) # Allow some time for the thread to start
print()
print("Thread information after starting")
print(f" - Thread name: {tea_thread.name}")
print(f" - Is thread alive? {tea_thread.is_alive()}")
print(f" - Is thread a daemon? {tea_thread.daemon}")
print(f" - Thread ID: {tea_thread.ident}")
print()

# Wait for the thread to finish
print("Waiting for thread to finish")
print()
tea_thread.join()

# Display thread information after finishing
print("Thread finished")
print(f" - Thread name: {tea_thread.name}")
print(f" - Is thread alive? {tea_thread.is_alive()}")
print(f" - Is thread a daemon? {tea_thread.daemon}")
print(f" - Thread ID: {tea_thread.ident}")
print()
