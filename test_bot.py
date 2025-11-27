import time
import sys

# A list of fake modules to load
modules = [
    "Neural Engine",
    "Data Layer",
    "Logic Core",
    "Programming Dataset"]

print("Initializing System...")

for module in modules:
    if "Dataset" in module:
        print(f"Loading {module}", end="")
        sys.stdout.flush()
        time.sleep(1)
        print(" [ERROR]")
    else:
        print(f"Loading {module}...", end="")
        sys.stdout.flush() 
        time.sleep(1)
        print(" [OK]")

print("\nSystem Online.")
