
'''
מיין את הרשימה מהגבוה לנמוך באמצעות מיון
הדפס את 3 הציונים הגבוהים ביותר (מותר כפילויות)
לאחר מכן מיין את הרשימה מהנמוך לגבוה
הדפס את 3 הציונים הנמוכים ביותר
אין להשתמש ב־set – הכפילויות חייבות להישאר
'''

grades = [78, 92, 65, 92, 81, 74, 99, 67, 88, 99]

print(sorted(grades, reverse=True))
print(sorted(grades, reverse=True)[:3])
print(sorted(grades))
print(sorted(grades)[:3])

'''
קלוט מהמשתמש מספר ת.ז. של מצביע (נניח שמדובר במספרים בין 1 ל־100)
כללים:
כל מצביע שנקלט – הכנס לרשימה בשם votes
קולטים רק את ת.ז. של המצביע, ולא את ההצבעה עצמה
ייתכן שאותו מצביע ינסה להצביע יותר מפעם אחת
הקלט מסתיים כאשר מתקבל הערך 999-
לאחר סיום הקלט:
צור set של מצביעים ייחודיים מתוך הרשימה
צור set נוסף בשם invalid_voters
עבור על כל המצביעים:
כל מצביע שהופיע יותר מפעם אחת – הסר אותו מקבוצת המצביעים החוקיים
הוסף אותו ל־invalid_voters
לבסוף הדפס:
את כל המצביעים החוקיים
את כל המצביעים הפסולים
כמה ניסיונות הצבעה היו היום (כלומר אורך הרשימה כולל כפילויות)
'''

votes = []

# input
while True:
    _id = (input('enter ID: '))
    if _id.isdigit() and len(_id) == 3:
        votes.append(_id)
    elif _id == '-999':
        break
    else:
        print('invalid ID')

# unique IDs in votes list
unique_id = []
for _id in votes:
    if votes.count(_id) == 1:
        unique_id.append(_id)
print(f'valid voters list: {unique_id}  ')

# invalid votes list
invalid_votes = set(votes) - set(unique_id)
print(f'invalid voters list: {invalid_votes} ')

# print total votes
print(f'there are {len(votes)} voting attempts in total')

