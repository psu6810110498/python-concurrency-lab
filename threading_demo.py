import threading
import time
import random

def task_sim(name):
    # ฟังก์ชันจำลองงานที่ต้องรอ I/O Bound
    
    print(f"เริ่มงาน: {name}")
    duration = random.uniform(1, 3)
    time.sleep(duration)
    print(f"งาน {name} เสร็จสิ้น (ใช้เวลา {duration:.2f} วินาที)")

def run_sequential():
    #กรณีรันแบบทีละอัน Sequential เพื่อเปรียบเทียบความเร็วดู
    print("\n--- เริ่มการทำงานแบบปกติ (Sequential) ---")
    start_time = time.time()
    for i in range(5):
        task_sim(f"งานที่-{i+1}")
    end_time = time.time()
    print(f"รวมเวลาทำงานแบบปกติ: {end_time - start_time:.2f} วินาที")

def run_threading():
    #กรณีรันแบบใช้ Thread เพื่อทดสอบความเร็วดู
    print("\n--- เริ่มการทำงานแบบใช้ Threading ---")
    start_time = time.time()
    threads = []
    
    # สร้าง Threads 5 อัน
    for i in range(5):
        t = threading.Thread(target=task_sim, args=(f"Thread-{i+1}",)) #เป็นการบอกให้ Thread 1 ไปทำฟังก์ชัน task_sim แต่ยังไม่เริ่มทำจนกว่าจะเจอคำสั่ง t.start()
        threads.append(t)
        t.start() # เป็นการสั่งให้ Thread 1 เริ่มทำงาน โดยจะไปทำงานพร้อมๆกับ Thread อื่นๆ
        
    # รอให้ทุก Thread ทำงานเสร็จครบก่อนไปต่อ 
    for t in threads:
        t.join()
        
    end_time = time.time()
    print(f"รวมเวลาทำงานแบบ Threading: {end_time - start_time:.2f} วินาที")

if __name__ == "__main__":
    # ลองรันเทียบกันดู
    run_sequential()
    run_threading()
