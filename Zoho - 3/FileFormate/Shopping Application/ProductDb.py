productdb = {}
class ProductDb:
  def __init__(self,productName,productquantity,productColour):
    self.productName = productName
    self.productquantity = productquantity
    self.productColour = productColour
    
def addProduct():
  productName = input("Enter product name: ").lower()
  productquantity = int(input("Enter product quantity: "))
  productColour = input("Colour of product: ")
  productID = int(input("Enter product ID : "))
  productdb[productID] = ProductDb(productName,productquantity,productColour)

def deleteProduct():
  productID = input("Enter product ID : ")
  del productdb[productID]

def increaseProductQuantity():
  productID = int(input("Enter product ID : "))
  increase = int(input("how many quantity u wanted to increase: "))
  productdb[productID].productquantity+=increase


def viewProducts():
  for id,det in productdb.items():
    print(f"ID number {id} || name {det.productName} || quantity {det.productquantity} || product colour {det.productColour}\n")
  print("Which product u wanted to buy")
  
def buyProduct():
  viewProducts()
  id = int(input("Enter product ID: "))
  quantity = int(input("Enter how much quantity u want: "))
  productdb[id].productquantity -= quantity
  print(f"Now the available quantity is {productdb[id].productquantity}")