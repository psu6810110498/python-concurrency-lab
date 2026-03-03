import multiprocessing
import time

def is_prime(n):
    # ฟังก์ชันคำนวณงานหนัก CPU BOUND : ตรวจสอบว่าเป็นเลขเฉพาะหรือไม่
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def run_sequential(numbers):
    print("\n--- เริ่มการคำนวณแบบปกติ (Sequential) ---")
    start_time = time.time()
    results = [is_prime(n) for n in numbers]
    end_time = time.time()
    print(f"รวมเวลาทำงานแบบปกติ: {end_time - start_time:.2f} วินาที")
    return results

def run_multiprocessing(numbers):
    print("\n--- เริ่มการคำนวณแบบใช้ Process Pool (Parallel) ---")
    start_time = time.time()
    
    # ใช้จำนวน CPU Core ที่เครื่องเรามี
    num_cores = multiprocessing.cpu_count()
    print(f"ใช้จำนวน CPU: {num_cores} cores")
    
    # สร้าง Pool ของ Process (แยก Memory กันอย่างเด็ดขาด)
    with multiprocessing.Pool(processes=num_cores) as pool:
        # กระจายงาน (numbers) ให้แต่ละ Process ทำ
        results = pool.map(is_prime, numbers)
        
    end_time = time.time()
    print(f"รวมเวลาทำงานแบบ Multi-processes: {end_time - start_time:.2f} วินาที")
    return results

if __name__ == "__main__":
    # รายการตัวเลขขนาดใหญ่ที่ต้องการตรวจสอบ
    numbers_to_check = [10**7 + i for i in range(500)]
    
    # รันเทียบกัน
    run_sequential(numbers_to_check)
    run_multiprocessing(numbers_to_check)
