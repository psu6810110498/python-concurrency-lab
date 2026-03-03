# Python Concurrency Lab (การทดลองทำงานพร้อมกันใน Python)

โปรเจกต์นี้สร้างขึ้นเพื่อศึกษาความแตกต่างของระบบ Concurrency และ Parallelism ในภาษา Python โดยเน้นการใช้งาน 3 รูปแบบหลัก ได้แก่ `Threading`, `Asyncio`, และ `Process Pool`

## 📋 สิ่งที่ได้เรียนรูั

โปรเจกต์นี้แบ่งบทเรียนออกเป็น 3 ส่วนหลักตามประเภทของงาน:

1.  **Threading (I/O-Bound)**
    - ใช้สำหรับงานที่ต้อง "รอ" เช่น การเขียนไฟล์หรือการเชื่อมต่อเครือข่าย
    - แม้ Python จะมี GIL แต่ Threading ยังช่วยให้เรา "รอพร้อมกัน" ได้
    - *ดูโค้ดได้ที่: `threading_demo.py`*

2.  **Asyncio (I/O-Bound Modern)**
    - เป็นวิธีการทำงานแบบ Single-thread concurrency (ใช้ Event Loop)
    - เหมาะมากสำหรับงาน Network API จำนวนมาก เพราะประหยัดทรัพยากรกว่าการสร้างหลายๆ Thread
    - *ดูโค้ดได้ที่: `asyncio_demo.py`*

3.  **Process Pool (CPU-Bound)**
    - ใช้สำหรับการคำนวณหนักๆ ที่ต้องใช้พลังของ CPU
    - บายพาสข้อจำกัดของ GIL โดยการสร้าง Process แยกกันจริงๆ ทำให้ใช้ CPU ได้ครบทุก Core
    - *ดูโค้ดได้ที่: `process_pool_demo.py`*

## 🚀 วิธีการรันโปรแกรม

คุณสามารถรันตัวเปรียบเทียบทั้งหมดได้ผ่านไฟล์ `main.py`:

```bash
python3 main.py
```

หรือรันแยกทีละส่วน:
- `python3 threading_demo.py`
- `python3 asyncio_demo.py`
- `python3 process_pool_demo.py`

## 📂 โครงสร้างโปรเจกต์
- `threading_demo.py`: ตัวอย่างการรันงาน I/O พร้อมกัน
- `asyncio_demo.py`: ตัวอย่างการใช้ async/await สำหรับงานระบบเครือข่าย
- `process_pool_demo.py`: ตัวอย่างการข้ามขีดจำกัด GIL เพื่อคำนวณเลขเฉพาะ
- `main.py`: โปรแกรมรวมสำหรับเปรียบเทียบเวลาทำงาน

---
นายมูฮัมหมัดฟาอีฟ ยามา 6810110498
จัดทำเพื่อการศึกษาและทำความเข้าใจเรื่อง Concurrency ใน Python
