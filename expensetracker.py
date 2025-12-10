expenses=[]
def add_expense():
    amount=float(input("enter amount :"))
    category=input("enter category  (food,travel,shopping) :")
    note=input("enter note :")
    expense = {
        'amount':amount,
        'category':category,
        'note':note
    }
    expenses.append(expense)
    print("expense is added sucesully :")
def view_expense():
    if not expenses:
        print("invalid expenses:")
        return
    print("\n...............all expenses...............")
    for i,exp in enumerate(expenses,1):
        print(f"{i}.${exp['amount']} | {exp['category']} | {exp["note"]}")
def total_expense():
    total=sum(s['amount'] for s in expenses)
    print(f"taotal spent :{total}")
def seperate_category():
    category=input("enter category :")
    total=sum(s['amount'] for s in expenses if s['category'].lower()==category.lower())
    print(f" category is {category},{total}")

def main():
    while True:
        print("..........All expenses..............\n")
        print("1.add expense")
        print("2.view expense")
        print("3.total expense")
        print("4.seperate category")
        print("5.exit")
        choice=input("enter ur option :")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            seperate_category()
        elif choice == "5":
            print("thank u for choose this tracker")
        else:
            print("invalid please try again :")
main()
