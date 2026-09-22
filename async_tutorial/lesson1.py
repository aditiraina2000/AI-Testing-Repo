import asyncio
import time

def sync_func(my_num: int)-> int:
    print(f"Sync function started with {my_num}")
    time.sleep(2)  # Simulate a blocking operation
    print(f"Sync function finished with {my_num}")
    return my_num * 2

async def main():
    print("Async function started")
    print(sync_func(5))  # This will block the event loop


if __name__ == "__main__":
    asyncio.run(main())