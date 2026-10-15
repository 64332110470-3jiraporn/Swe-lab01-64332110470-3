# Lab 1 - จิราภร สีสาวแห (64332110470-3)

วิชาวิศวกรรมซอฟต์แวร์ | ECP ปี 3 | มทร.อีสาน

## เนื้อหา

- `part2-ai-experiment/buggy_calculator.py`
- def calculate_grade(scores):
    # 1. ป้องกัน Bug กรณี scores เป็นลิสต์ว่าง (ZeroDivisionError)
    if not scores:
        return "N/A", 0.0

    # 2. แก้ไขระบบการย่อหน้า (Indentation) ให้ถูกต้องตรงตามมาตรฐาน
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade, average

scores = [85, 92, 78, 88, 95]
print(calculate_grade(scores))
print(calculate_grade([]))

- `part2-ai-experiment/mystery_code.py`
def process_data(records):
    # 1. ป้องกันกรณีส่งลิสต์ว่างมาให้คำนวณเพื่อความรวดเร็วและปลอดภัย
    if not records:
        return {}

    result = {}
    # 2. วนลูปจัดกลุ่มข้อมูลและสะสมยอดรวมแยกตาม category
    for item in records:
        key = item.get("category", "unknown")
        value = item.get("amount", 0)
        if key not in result:
            result[key] = {"total": 0, "count": 0}
        result[key]["total"] += value
        result[key]["count"] += 1

    # 3. วนลูปคำนวณหาค่าเฉลี่ยของแต่ละหมวดหมู่
    for key in result:
        result[key]["average"] = result[key]["total"] / result[key]["count"]

    return result

# ทดสอบการใช้งานด้วยข้อมูลตัวอย่าง
sample = [
    {"category": "food", "amount": 120},
    {"category": "transport", "amount": 45},
    {"category": "food", "amount": 85},
    {"category": "transport", "amount": 30},
    {"category": "entertainment", "amount": 200},
]

output = process_data(sample)
for cat, stats in output.items():
    print(f"{cat}: total={stats['total']}, count={stats['count']}, avg={stats['average']:.1f}")
    
- `part2-ai-experiment/validate_id.py`
กรณีที่ 1 - รหัส: 63332110339-5   -> ผลลัพธ์: True
กรณีที่ 2 - รหัส: 633321103395    -> ผลลัพธ์: False
กรณีที่ 3 - รหัส: 6333211033-5    -> ผลลัพธ์: False
True
False
False
False
False

## สรุปสิ่งที่เรียนได้จาก Lab 1
"จากการทำปฏิบัติการครั้งนี้ ได้เรียนรู้วิธีการทำงานร่วมกับ AI Coding Assistant อย่างมีประสิทธิภาพทั้งในด้านการช่วยวิเคราะห์อธิบายความเข้าใจในโค้ดเดิม และการช่วยสร้างโค้ดใหม่ที่มีความแม่นยำสูงด้วย Regular Expression นอกจากนี้ยังได้ฝึกทักษะการตรวจสอบความปลอดภัยของโปรแกรม เช่น ปัญหาการหารด้วยศูนย์ (Zero Division Error) และการจัดรูปแบบโค้ดตามมาตรฐานที่ถูกต้องผ่านเครื่องมือแก้ไขข้อผิดพลาด (Bug Fixing) ซึ่งช่วยเสริมทักษะการพัฒนาซอฟต์แวร์ที่มีความน่าเชื่อถือสูงและรวดเร็วยิ่งขึ้นครับ"
