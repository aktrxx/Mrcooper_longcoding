class Product():
    
    def __init__(self,productname,p_id,quantity=0,baseprice=0,location="default") -> None:
        self.p_id = p_id
        self.quantity = quantity
        self.baseprice = baseprice
        self.location = location

    def __str__(self) -> str:
        return f"{self.p_id} has {self.quantity}"
    def addQuantity(self,q):
        self.quantity += q
    def updateBase(self,newprice):
        self.baseprice += newprice
    def is_sold(self):
        if self.quantity<1:
            print("The Item is sold")
        else: print("The Item is Available")

class Fruits(Product):
    def __init__(self, productname, p_id,name, quantity=0, baseprice=0, location="default",expdate="15-04-23") -> None:
        super().__init__(productname, p_id, quantity, baseprice, location)
        self.expdate = expdate
        self.name = name
    def expDate(self):
        print(self.expDate)
class Vegetables(Product):
    def __init__(self, productname, p_id,name, quantity=0, baseprice=0, location="default",expdate="15-04-23") -> None:
        super().__init__(productname, p_id, quantity, baseprice, location)
        self.expdate = expdate
        self.name = name
    def expDate(self):
        print(self.expDate)

class Users:
    def __init__(self) -> None:
        self.users = {}
        self.farmers = {}
        self.company = {}

        pass
    def newUser(self,u_id,password):
        self.users[u_id] = password

    def newFarmer(self,f_id,password):
        self.farmers[f_id] = password
    def newCompany(self,c_id,password):
        self.company[c_id]=password
    
class Login(Users):
    def __init__(self) -> None:
        super().__init__()
    
    def __verifyUser(self,u_id,password):
        # if self.users[u_id] == password:
            print("You are logged in")
            return True
    def verifyFarmer(self,f_id,password):
        if self.farmers[f_id] == password:
            return True
    def verifyCompany(self,c_id,password):
        if self.company[c_id] == password:
            return True

class Regester(Users):
    def __init__(self) -> None:
        super().__init__()
    
    def adduser(self,u_id,password):
        self.newUser(u_id,password)
    def addCompany(self,c_id,password):
        self.newCompany(c_id,password)
    def addFarmer(self,f_id,password):
        self.addFarmer(f_id,password)

class Bidding:
    def __init__(self,start_time,end_time,p_id) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.farmer = Users
        self.product = Product(p_id)
        self.user = Users
        self.company = Users
        self.curr_max = self.product.baseprice
    def addbid(self,newbid):
        if newbid > self.curr_max:
            print("Your bid is taken, current bid: "+newbid)
            self.curr_max = newbid
    def currBid(self):
        print(self.curr_max)
    def basePrice(self):
        print(self.product.baseprice)
    def productDescription(self,p_id):
        print("For the Product "+ p_id +" " +self.product.is_sold + " at " +self.curr_max+" Bidding")
        
class Reviews():
    def __init__(self,f_id) -> None:
        pass
    def addReview(self,review):
        self.review = review
    def addReview(self,rating):
        self.review = rating
    def getReview(self,f_id):
        print(self.review[f_id])
    def getRating(self,f_id):
        print(self.rating[f_id])

class Support:
    def __init__(self) -> None:
        pass
    def askQuery(self,query):
        print(self.answers[query])



class RetailShop:
    def __init__(self, shop_name, shop_location):
        self.shop_name = shop_name
        self.shop_location = shop_location
        self.products = {}
        self.users = {}
        self.auctions = {}

    def addProduct(self, product_name, product_id, product_price, product_quantity):
        product = {"id": product_id, "price": product_price, "quantity": product_quantity}
        self.products[product_name] = product

    def getProductDetails(self, product_id):
        for product_name, product in self.products.items():
            if product["id"] == product_id:
                return f"Product Name: {product_name}, Price: {product['price']}, Quantity: {product['quantity']}"
        return "Product not found"

    def addQuantity(self, product_id, quantity):
        for product_name, product in self.products.items():
            if product["id"] == product_id:
                product["quantity"] += quantity
                return f"Added {quantity} to {product_name}. New Quantity: {product['quantity']}"
        return "Product not found"

    def is_sold(self, product_id):
        for product_name, product in self.products.items():
            if product["id"] == product_id:
                if product["quantity"] == 0:
                    return f"{product_name} is sold out."
                else:
                    return f"{product_name} is available for purchase."
        return "Product not found"

    def add_user(self, username, password):
        self.users[username] = {"password": password, "is_farmer": False}

    def login(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False

    def add_auction(self, product_id, starting_bid):
        if product_id not in self.products:
            return "Product not found"
        if self.products[product_id]["quantity"] == 0:
            return "Product is sold out"
        self.auctions[product_id] = {"starting_bid": starting_bid, "bids": []}
        return "Auction added successfully"

    def bid(self, username, product_id, bid_amount):
        if username not in self.users:
            return "User not found"
        if product_id not in self.auctions:
            return "Auction not found"
        if bid_amount <= self.auctions[product_id]["starting_bid"]:
            return "Bid must be greater than the starting bid"
        if self.users[username]["is_farmer"]:
            return "Farmers cannot bid on auctions"
        self.auctions[product_id]["bids"].append({"username": username, "bid_amount": bid_amount})
        return "Bid successful"

    

    
        
    



# ret = RetailShop(2,"hhe")
# ret.addProduct("p1",1,300,40)
# ret.addProduct("p2",2,400,30)
# ret.getProductDetails(1)
# ret.addQuantity(1,10000)
# ret.is_sold(1)
