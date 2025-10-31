
class Shopping_cart:
    def __init__(self,*args):
        self.items=list(args)

    def add_card(self,products,price):
        self.items.append((products,price))

    def remove_card(self, products):
        self.items = [i for i in self.items if i[0] != products]
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        #"ფასდაკლბა 10 ლარზე ზემოთ
        if total>=10:
           total=total-3.0
        return print(total)

card=Shopping_cart()
card.add_card("წყალი",2.50)
card.add_card("პური",1.30)
card.add_card("ყველი",6.80)
card.add_card("რძე",6.20)
card.remove_card("პური")

print(f"თქვენს კალათშია {card.items}")
print("საერთო ფასი არის ",end="")
card.calculate_total()

