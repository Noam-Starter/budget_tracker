import datetime

expenses = []

while True:
    description = input("הכנס תיאור ההוצאה (או 'סיום' כדי לצאת): ")
    if description.strip() == "סיום":
        break

    while True:
        amount_str = input("הכנס את סכום ההוצאה: ").strip()
        try:
            amount = float(amount_str)  # ניסיון להמיר למספר
            break  # יציאה מהלולאה אם הצליח
        except ValueError:
            print("שגיאה: הכנס רק מספר ללא טקסט נוסף!")

    date = datetime.date.today()
    expenses.append((date, description, amount))

# כתיבה לקובץ לאחר איסוף כל הנתונים
with open("expenses.txt", "w", encoding="utf-8") as file:
    total = 0
    for expense in expenses:
        file.write(f"{expense[0]} | {expense[1]} | {expense[2]:.2f} ש\"ח\n")
        total += expense[2]

    file.write(f"\nסה\"כ הוצאות: {total:.2f} ש\"ח\n")

print(f"סה\"כ הוצאות: {total:.2f} ש\"ח")