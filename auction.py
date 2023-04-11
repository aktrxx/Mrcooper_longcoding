from shop import RetailShop

retail_shop = RetailShop("Shop Name", "Shop Location")
retail_shop.add_user("user1", "password1")
retail_shop.add_user("user2", "password2")
retail_shop.add_user("farmer1", "password3")
print(retail_shop.login("user1", "password1"))
print(retail_shop.login("user2", "password3")) 

retail_shop.addProduct("p1", 1, 300, 40)
retail_shop.addProduct("p2", 2, 400, 30)
print(retail_shop.getProductDetails(1)) 