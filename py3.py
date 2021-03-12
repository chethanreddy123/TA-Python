
'''2- Problem Statement :
Make a Grocery List for supermarket shopping with name,
price and quantity; if the list already contains an item
then only update the price and quantity it should not
append the item name again. Ask the user his/her budget
initially and minus the budget after adding a new item in
the list. If budgets go zero/0 then no more items could
be bought and if some money left and users add items
greater than budget left then inform “over price” or any
other message. After the list is made any money left in the budget 
it should show an item within the budget from
the list made.VALIDATION is a must.'''
grocery_item = {} 
grocery_history = [] 
Budget=float(input("Enter Your budget: "))
bill=0
amount=[]
stop = False 

while not stop:
    print("1.Add an item")
    print("2.Exit")
    choice=int(input("Enter the choice :"))
    if choice==1:
        item_name = input("Enter product :\n")   
        quantity = float(input("Enter quantity :\n"))   
        cost = float(input("Enter Price :\n"))
        bill+=cost
        if(bill>Budget):
            print("Can't Buy the product ###(because budget left is %f)"%(Budget-bill+cost))
            bill=bill-cost
        else:
            amount.append(cost)
            grocery_item = {'name':item_name, 'quantity': float(quantity), 'price': float(cost)}
            grocery_history.append(grocery_item)
    else:
        stop = True
    
for i in grocery_history:
    if i["price"]<=Budget-bill:
        print("Amount left can buy you",i["name"])
print("Product name              Quantity       Price")
for index, item in enumerate(grocery_history):
    print('%s       %.2f       %.2f' % (item['name'],item['quantity'], item['price']))