expenses=[]
def add_expense():
    amount=float(input("enter amount :"))
    category=input("enter category(food,travel,shopping): ")
    note=input("enter note :")
    expense={
        'amount':amount,
        'category':category,
        'note':note
    }
    expenses.append(expense)
    print("expense added succesfully!\n")
def view_expenses():
    if not expenses:
        print("no expenses are found !\n")
        return
    print("\n.......all expense..........")
    for i,exp in enumerate(expenses,1):
        print(f"{i}.${exp['amount']} | {exp['category']} | {exp['note']}")
        print()
def total_expense():
    total=sum(e['amount'] for e in expenses)
    print(f"total spent :{total}")
def expense_by_category():
    category=input("enter category :")
    total=sum(e['amount']  for e in expenses if e['category'].lower()==category.lower())
    print(f"expense by category {category}:{total}")
def main():
    while True:
        print("........expense tracker..........")
        print("1.Add expence")
        print("2. View All expence")
        print("3. total expence")
        print("4. expence by category")
        print("5. exit")
        choice=input("enter ur choice :")
        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            total_expense()
        elif choice=="4":
            expense_by_category()
        elif choice=="5":
            print("thnak u for choosing this expense tracker")
            break
        else:
            print("invalid")
main()