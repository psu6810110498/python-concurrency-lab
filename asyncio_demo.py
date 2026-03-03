import asyncio
import time
import random

async def fetch_data(name):
    # ฟังก์ชันแบบ Coroutine (async)
    # ใช้สำหรับงาน I/O เช่น การรอข้อมูลจาก API
    print(f"กำลังดึงข้อมูล: {name}")
    # ใช้ asyncio.sleep แทน time.sleep 
    # เพื่อไม่ให้ 'หยุด' การทำงานของทั้ง Thread
    # แต่เป็นการ 'ปล่อย' ให้งานอื่นทำแทนระหว่างรอ
    delay = random.uniform(1, 2)
    await asyncio.sleep(delay)
    print(f"ดึงข้อมูล {name} สำเร็จ (ใช้เวลา {delay:.2f} วินาที)")
    return f"Data from {name}"

async def run_async_demo():
    print("\n--- เริ่มการทำงานแบบ Asyncio  ---")
    start_time = time.time()
    
    # สร้างรายการงาน (Tasks) หลายอันพร้อมกัน
    tasks = [
        fetch_data("API-เซิร์ฟเวอร์-1"),
        fetch_data("API-เซิร์ฟเวอร์-2"),
        fetch_data("API-เซิร์ฟเวอร์-3"),
        fetch_data("API-เซิร์ฟเวอร์-4"),
        fetch_data("API-เซิร์ฟเวอร์-5")
    ]
    
    # รันทุกงานพร้อมกันและรอผลลัพธ์
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"\nผลรวมข้อมูล: {results}")
    print(f"รวมเวลาทำงานแบบ Asyncio: {end_time - start_time:.2f} วินาที")

if __name__ == "__main__":
    # การรันโค้ด async ต้องรันผ่าน Event Loop
    asyncio.run(run_async_demo())
