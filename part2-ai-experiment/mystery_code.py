def calculate_grade(scores):
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
