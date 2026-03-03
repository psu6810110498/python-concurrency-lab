import os
import subprocess
import time

def run_script(script_name):
    print(f"\n{'='*50}")
    print(f"กำลังรัน: {script_name}")
    print(f"{'='*50}")
    start = time.time()
    # รัน script แยกแบบ subprocess
    subprocess.run(["python3", script_name])
    end = time.time()
    return end - start

def main():
    print("Python Concurrency Lab!")
    print("เรากำลังจะเปรียบเทียบการทำงานของ Threading, Asyncio และ Process Pool\n")
    
    scripts = [
        "threading_demo.py",
        "asyncio_demo.py",
        "process_pool_demo.py"
    ]
    
    reports = {}
    
    for script in scripts:
        if os.path.exists(script):
            duration = run_script(script)
            reports[script] = duration
        else:
            print(f"ไม่พบไฟล์: {script}")

    print(f"\n{'='*50}")
    print("สรุปเวลาการทำงานทั้งหมด")
    print(f"{'='*50}")
    for script, duration in reports.items():
        print(f"- {script:20}: {duration:.2f} วินาที")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
