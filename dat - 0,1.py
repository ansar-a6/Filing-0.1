opt = ""; File = "dat.txt"
def write():
    he = open(File,"a")
    p_name = str(input("Enter product name: "))
    he.write(p_name + "\n")
    price = str(input("Enter the price: "))
    he.write(price + "\n")
    print("date foramt: 01/01/23")
    date = str(input("Enter date: "))
    he.write(date + "\n")
    he.close()

def read():
    file_1 = open(File,"r")
    product_name = "";product_price = 0.0
    total = 0.0;date = "";das = "-"
    for line in file_1:
      product_name = line.rstrip()
      line = file_1.readline()
      product_price = line.rstrip()
      total += float(product_price)
      line = file_1.readline();date = line.rstrip()
      print("%-30s" % product_name,end="")
      print(":","%16.2f" % float(product_price),end="")
      print("%17s" % date)
    print(das * 65);print("Total:",round(total,3))
    file_1.close()

while (opt != 0):
    print("0: Exit");print("1: Enter data");print("2: Print data")
    opt = int(input())
    if (opt == 0):
        exit
    elif (opt == 1):
        write()
    elif (opt == 2):
        read()
