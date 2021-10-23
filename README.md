# COMP3019J Assignment

### Project: Grocery List Website

### Team Members:

* Wang Yuyang 19206226
* Yang Liuxin 19206207

### Introduction

The website should allow multiple grocery shops to set up products available, along with their unit prices as well as images. 
The website should allow users to visit different shops, and put items into their basket. The website should allow users to view their basket at all times, and add/remove items from the basket. 
The website should allow users to increase/ decrease the quantity of the items while looking at their baskets. 
It should also calculate the total expenditure/cost for all items in the basket. 
Finally, it should create an itemised list of the user’s shopping bill, grouped by the shop.


### Preview this project (Deployed in Heroku)

This is a **preview version** of this project, it might contain errors or out-dated pages.
Please use python to run this project locally to see the latest website.

[http://comp3019j-web-dev.herokuapp.com/](http://comp3019j-web-dev.herokuapp.com/)


### Run this project


#### Set up environment
1. Install Python3.9
2. Using the following code to set up environment
```shell
python -V  # Print out python version for debugging
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Run this web sever

```shell
flask run
```
or

```shell
python run.py
```

or

If pipeline passed then this docker contains the same code with master:

![pipeline](https://csgitlab.ucd.ie/19206226/TEAM_20/badges/master/pipeline.svg)

```shell
docker pull echo0821/web-project:latest 
docker run -p 5000:5000 echo0821/web-project:latest
```
#### Open the web page using Chrome(Edge)
**Safari and IE is not offfically supported**

URL: http://localhost:5000

or

URL: http://127.0.0.1:5000



### Test Account

Shopper:
* Username: shop1
* Password: 123

Buyer:
* Username: buyer1
* Password: 123

### Roles in the system
1. Buyers
   1. Register in login page
   2. Can add product to his cart
   3. Can view his cart
   4. Can Make orders 
   5. Can view his orders
   6. Can't Add products
   7. Can't Manage products
2. Seller (Registered by Admin, Not allowed to be created by public register)
   1. Can Add products
   2. Can Manage products 
   3. Can view orders from his shop
   4. **Can't view his cart**
   5. Can't make orders
   6. Can confirm orders
   
### Buyer's Functionality
* Navigation bar
  * Automatically Change for different role
  * Auto hide & display flash message
* Index Page
  * Allowing user to view top-selling products
  * Allowing user to view products grouped by shops
* Shopping Cart
  * Users can add product to their shopping cart
  * Items in the cart can be removed or change quantity
  * Items can be correctly count if user add the product multiple times from detail page
* Ordering
  * User can make order from shopping cart
  * After paying, user can view the order in the order page
* User profile
  * User can change their avatar in the profile page
  * User can change their email in the profile page
  * User can change their password in the profile page

### Seller's Functionality
* Navigation bar
  * Automatically Change for different role
  * Auto hide & display flash message
* Index Page
  * Allowing user to view top-selling products
  * Allowing user to view products grouped by shops
* Product Management
  * User can add product to the system
  * User can modify product to the system
  * User can remove product to the system
* Order Management
  * User can view the order in his shop 


### Characteristic

* Responsive Layout (flex Layout)
* Allowing unregistered user to view products
* Auto redirect to login page
* CSRF Protection
* Blueprint for routing


### TODO
* Navigation bar
  * Optimize navigation bar displaying contents
    * Letting the user's avatar be displayed in navigation bar
* Index Page
  * Add a more comprehensive sidebar
    * Letting the order status be displayed in sidebar
    * Letting the sidebar display recommended products by user's preference
  * Page layout optimization
    * Add right and left sidebar for information display
  * Algorithm's optimization
    * Recommend product by user's preference (By calculate the word distance between the user's ordered product's title and the product's title on sale)
* Shopping Cart
  * Using JS to calculate the total price
  * Using AJAX to dynamically change the number of a product in shopping cart
* Ordering
  * Adding the functionality of refunding and order canceling
  * Adding alert to user when they try to "confirm delivered", when the order is not confirmed by the shopper
  * Adding the functionality of the shopper can upload the delivery express ID
  * Adding the functionality of buyer can give a comment to an order when submitting
* User profile
  * Adding the functionality of restoring his password using email 
* Product details
  * Adding the functionality of letting the shopper set up a HTML introduction in the product detail page
  * Adding an iframe to the product detail page

