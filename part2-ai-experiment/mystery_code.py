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
