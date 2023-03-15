# לכתוב מחלקה של פריט במכולת שיש בו 3 שדות : שם, כמות , מחיר ליחידה אחת
class Product:
    # numOfProduct = 0

    def __init__(self, prodName, price):
        # Product.numOfProduct += 1
        self.prodName = prodName
        self.price = price
        self.amount = 0

    # להוסיף מטודה שמדמה קניה של הפריט בכמות מסויימת
    def buyProd(self, quantity):
        # אם הכמות הנדרשת לא תקינה יש להדפיס הודעה מתאימה. אם לא,
        # המטודה מעדכנת את הכמות החדשה של אותו הפריט. זהירות :
        # אי אפשר לקנות פריט בכמות יותר גבוהה
        # ממה שיש במכולת :במקרה כזה, הלקוח
        # יקבל כמספר הפריטים הנשארו במכולת
        # .המטודה מחזירה מחיר של הקניה.
        if quantity < 0:
            print("You can't invite less than 0")

        elif quantity > self.amount:
            otherQuntity = self.amount
            self.amount = 0
            return otherQuntity, otherQuntity * self.price

        else:
            self.amount -= quantity
            return quantity, quantity * self.price

    #-להוסיף מטודה שמחזירה מחרוזת עם שם הפריט ומחיר. למשל :
    def __str__(self):
        return self.prodName + " - " + str(self.price)

    #-להוסיף מטודה שמדמה הזמנה מספק שמעדכנת את כמות הפריט.
    # המטודה מקבלת כמות, ומעדכנת את הכמות החדשה.
    # אם הכמות שלילית, יש להדפיס הודעה מתאימה.

    def orderProd(self, quantity):
        if quantity < 0:
            print("You can't invite less than 0")
        else:
            self.amount += quantity

    #-להוסיף מטודה שמקבלת פריט אחר ומחזירה האם מדובר באותו פריט.
    # 2 פריטים מוגדרים להיות זהים אם יש להם שם זהה.


    # def sameProd(self, otherProd):
    #     if self.prodName == otherProd.prodName
    #         return True
    #     else:
    #         return False

    def __eq__(self, other):
        return self.prodName == other.prodName

