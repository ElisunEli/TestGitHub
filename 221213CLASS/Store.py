# -ליצור מחלקה של מכולת. יש בה רשימה של פריטים.
from Product import Product


class Store:

    def __init__(self):
        self.products = []

    #     #-לכתוב מטודה שמדמה הזמנת פריט חדש מספק לתוך המכולת ותכניס לתוך הרשימה את הפריט החדש.
    # לדוגמא :
    # Please enter the name of the product :
    # Chocolate
    # Please enter the price :
    # 4.5
    # Please enter amount :
    # 50
    # אם הפריט כבר היה במכולת : לא לתפוס מקום אחד חדש ברשימה אלא לעדכן את הכמות החדשה.

    def orderToStore(self):
        product = Product(input("Please enter the name of the product :"), float(input("Please enter the price :")), int(input("Please enter amount :")))
        # name = input("Please enter the name of the product :")
        # price = float(input("Please enter the price :"))
        # quantity = int(input("Please enter amount :"))

        for k in self.products:
            if k.eq(product):
                k.amount += product.amount
            return
        self.products.append(product)

    def __str__(self):

        # למשל:
        # 1 – Chocolate – 4,5 sh
        # 2 – Candies – 2,3 sh

        for k in range(len(self.products)):
            print("" + str(k + 1) + " - " + self.products[k].__str__())  # STR?

    # -להוסיף מטודה המבצעת קניה שלמה של כמה פריטים.
    # מטודה זו קוראת למטודה הקודמת עד סיום הקניה. למשל :

    def buyFromStore(self):
        recivelist = []
        total = 0
        while True :
            print("What do you want to buy?")
            self.__str__()
            print("0 – To end ")

            numOfProduct = int(input())
            if numOfProduct == 0:
                break

            print("How many you want to buy?")
            quantity = int(input())
            quantityP, price = self.products[numOfProduct - 1].buyProd(quantity)
            recivelist.append(self.products[numOfProduct - 1].__str__() + "x" + str(quantityP) + " - " + str(price))
            total += price

        print('\n'.join(map(str, recivelist)))
        print('\n', "____________________")
        print("TOTAL          ", total)

    #בתוכנית הראשית :
    # לתת תפריט פעולות למשתמש לבחור האם להזמין פריט חדש למכולת או האם לבצע קניה
    #אם מבצע קניה :
    # לתת לו לקנות את הפריטים שרוצה ולהדפיס חשבונית עם שם פריט – כמות*מחיר לאחד ומחיר עבור אותו הפריט

    def choice(self):
        while True:
            option = int(input("Please enter your choice :" + "\n" + "1 – Enter a new product" + "\n" + "2 – Begin a new order" + "\n" +"0 – To exit"))
            if option == 1:
                prodName = input("Please enter the name of the product : ")
                price = float(input("Please enter the price :"))
                amount = int(input("Please enter amount :"))
                product = Product(prodName,price)
                product.amount = amount
                self.products.append(product)
            if option == 2:
                self.buyFromStore()
            if option == 0:
                print("Good Buy")
                break










