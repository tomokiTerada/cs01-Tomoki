score_w = float(input('กรุณาใส่คะแนนเก็บของคุณ:'))
score_m = float(input('กรุณาใส่คะแนนmidของคุณ:'))
score_f = float(input('กรุณาใส่คะแนนfinalของคุณ:'))
score=(score_f+score_m+score_w)/3.0


if score >= 80:
    grade = "A"
elif score >= 75:
    score = 'B+'
elif score >= 70:
    grade = "B"
elif score >= 65:
    grade = 'C+'
elif score >= 60:
    grade = 'C'
elif score >= 55:
    score = 'D+'
elif score >= 50:
    score = 'D'
else:
    grade = 'F'
print('เกรดของคุณคือ:', grade)