# **Testing And Project Barrier Solutions**

[Return to README.md](https://github.com/KonstantinaStrantzali/FreshNow-food-corner/blob/master/README.md)

[View the live site here](https://freshnow-store.herokuapp.com/)

![Final project image home page](freshNow_store/documentation/responsive_layout.png)

## **Contents**

[Testing User Stories](#testing-user-stories)

[Code Validation](#code-validation)

[Responsiveness And Compatibility](#responsiveness-and-compatibility)

[Testing Performance](#testing-performance)
* [Lighthouse](#lighthouse)

[Project Barriers and Solutions](#project-barriers-and-solutions)
* [Solved Bugs](#solved-bugs)
* [Known Bugs](#known-bugs)

---
## **Testing User Stories**

### Regular Site User Stories

* As a site user, I want the main purpose to be clear at first glance so that I can instantly understand if this is the correct site for me.
- Website's purpose is instantly understandable, as relevant images and headers have been used to welcome the user.
![Home](/freshNow_store/documentation/screenshots/home-feature.png)
* As site user, I wish to create an account for future purchases and be able to view my payment history so that I track my payment information. 
- Users are able to create an account and view the order history on their profile
![Account](/freshNow_store/documentation/screenshots/profile-account.png)
* As site user, I wish to login or logout so that I can easily access my profile.
![Logout](/freshNow_store/documentation/screenshots/signout.png)

![Log In](/freshNow_store/documentation/screenshots/signin.png)

* As site user, I wish to receive a confirmation email after registering my new account, so I can verify that the process was successful.
 ![Verify Email](/freshNow_store/documentation/screenshots/register-account.png)

 ### Customer Shopper Stories

* As a shopper, I wish to view all the products so that I can choose what I would like to buy.
![All products](/freshNow_store/documentation/screenshots/all-products.png)

* As a shopper, I wish to search for a specific product and category so that I find what I want faster.
- Users can search by meals name and instantly find what they look for.
![Sort By Meal Name](/freshNow_store/documentation/screenshots/search-bar.png)

* As a shopper, I wish to be able to sort the products by price and calories so that I find what I want directly without wasting time on searching. 
 - Users can sort by Category, Price, Calories and Ratings.
![Sort By Name In Category](/freshNow_store/documentation/screenshots/sort.png)

* As a shopper, I wish to view products in more detail so I am aware of the full product information.
![Product details](/freshNow_store/documentation/screenshots/product-details.png)

* As a shopper,  I wish to get visual feedback when an action has been completed so that avoid making mistakes while adding, editing and deleting products.

![Message](/freshNow_store/documentation/screenshots/success-message.png)

![Message](/freshNow_store/documentation/screenshots/review-message.png)

![Message](/freshNow_store/documentation/screenshots/info-message.png)

![Message](/freshNow_store/documentation/screenshots/delete-message.png)

![Message](/freshNow_store/documentation/screenshots/add-products.png)

* As a shopper, I wish to easily add, update or delete items in my bag where I can view a summary of my orders along with the total price so that I can stick with my budget.

![Bag-review](/freshNow_store/documentation/screenshots/add-products.png)

* As a shopper, I wish to easily make a payment so that I smoothly complete the checkout. 
  - Users are able to make payments by filling their details in the checkout form.

![Checkout](/freshNow_store/documentation/screenshots/checkout.png)

### Customers Stories  (Logged in Users) 

* As a logged-in user, I want to be able to view other people's reviews so that I know if the products worth purchasing. 
* As a logged-in user, I want  to be able to add or edit my own reviews to products so that I share my opinion with the other customers.

![Checkout](/freshNow_store/documentation/screenshots/review.png) 

* As a logged-in user, I want to be able to add products to my wishlist, so that I can view those products later.
* As a logged-in user, I want to be able to delete products from my wishlist, so that I can change my mind.

![Wishlist](/freshNow_store/documentation/screenshots/wishlist.png) 

* As a logged-in user, I want to be able to save my profile details, so that I can avoid retyping my details everytime I place an order.
* As a logged-in user, I want to have order history viewable, so that I can view my past orders.

![Account](/freshNow_store/documentation/screenshots/profile-account.png)

### Creator Goals
* As a creator, I want the site to be easy to navigate.
Users can easily navigate through the site using the 2 navigation bars.

* As a creator, I want to allow users to filter through products.
![Sort By Meal Name](/freshNow_store/documentation/screenshots/search-bar.png)

* As a creator, I want to allows admins to Add/Edit/Delete products to/from the store.
Admin is able to add, edit and delete any product.
![Admin](/freshNow_store/documentation/screenshots/admin-edit-delete.png)



## **Code Validation**

### W3C Markup Validation Service:
* The HTML for this site was validated by running each page through the [W3C HTML Markup Validator](https://validator.w3.org/) and returned no errors.
    * Home
        * ![Home](/freshNow_store/documentation/validation/home-validation.png)
    * Our Story
        * ![About Us](/freshNow_store/documentation/validation/aboutUs_validation.png)
    * Products
        * ![Products](/freshNow_store/documentation/validation/products_validation.png)
    * Product Details
        * ![Product Details](/freshNow_store/documentation/validation/product_details_validation.png)
    * Profile
        * ![Profile](/freshNow_store/documentation/validation/profile_validation.png)
    * Wishlist
        * ![Wishlist](/freshNow_store/documentation/validation/wishlist_validation.png)
    * Shopping Cart
        * ![Shopping Bag](/freshNow_store/documentation/validation/bag_validation.png)
    * Checkout
        * ![Checkout](/freshNow_store/documentation/validation/checkout_validation.png)
    * Checkout Success
        * ![Checkout Success](/freshNow_store/documentation/validation/checkout_success_validation.png)
    * Login, Logout, Register
        * ![Checkout Success](/freshNow_store/documentation/validation/signin_validation.png)
    * Edit Product
        * ![Edit Product](/freshNow_store/documentation/validation/edit_product_validation.png)

### W3C CSS Validation Service:

* W3C CSS Validator used to validate CSS code for the pages below.
    * Base.css
        * ![Bace.css](/freshNow_store/documentation/validation/base.css.png)
    * Base.css
        * ![Profile](/freshNow_store/documentation/validation/profile.css.png)
    * Base.css
        * ![Checkout](/freshNow_store/documentation/validation/checkout.css.png)

---

### JSHint:
* [JSHint](https://jshint.com/) was used to test all JS files and returned no errors.

    * Bag
        * ![Bag](/freshNow_store/documentation/validation/bag%2Cjs.png)

    * Country Fields Functionality
        * ![Country Fields Functionality](/freshNow_store/documentation/validation/countries.js-validation.png)
    * Quantity Input Field
        * ![Quantity Input Field](/freshNow_store/documentation/validation/quantity-button.js-validation.png)
    * Sort
        * ![Sort](/freshNow_store/documentation/validation/sort.js-validation.png)
    * Stripe Payments
        * ![Stripe Payments](/freshNow_store/documentation/validation/stripe-js-validation.png)
          
### PEP8:
* [PEP8 online](http://pep8online.com/) is used to test Python files and returned no errors.

Alot of the Python errors were fixed during development. Some of them were auto generated by Django thus were left untouched. Also some lines were too long and could not broken up, therefore `# noqa:` was used in order for Flake8 to ignore them.

* ![Products views.py PEP8 Check](/freshNow_store/documentation/validation/pep8.png)

* The python extention was also used to test Python for PEP8 compliance with it's built in linting.
    * ./checkout/app.py - 'checkout.signals' imported but unused
        * The import is used to let Django know there is a signals module, listening for changes to automatically update the totals.
            * ![Flake8](/freshNow_store/documentation/validation/flake8.png)

[Back to Top](#testing-and-project-barrier-solutions)



## **Responsiveness And Compatibility**

Responsiveness tested  across different screen sizes and browsers. More specifically, Dev Tools used to emulate the following devices:

**Mobile Devices**
- Galaxy S5
- Galaxy S9
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 plus
- iPhone X / XS


**Tablet Devices**
- iPad
- iPad Pro

**Browsers**
- Google Chrome
- Mozilla Firefox
   
 

[Back to Top](#testing-and-project-barrier-solutions)

## **Testing Performance**

### Lighthouse

* Google Lighthouse was run on different pages returning different results. Below is an extract of the reports for the 'Home' page, 'Product Details' and 'Wishlist'

* Home
        * ![Home](/freshNow_store/documentation/validation/lighthouse-home.png)

* Product Detail
        * ![Product Detail](/freshNow_store/documentation/validation/lighthouse-2.png)

* Wishlist
        * ![Product Detail](/freshNow_store/documentation/validation/wishlisti-lighthouse.png)



## **Project Barriers and Solutions**

### Solved Bugs

1. Logout page in django-allauth didn't comply with the rest basic layout of the project and the footer couldn't stick on the bottom of the page. Thus I set an unique id to the form element of logout page, which eventually pushed the footer on the bottom.

2. When I switched my GitHub database to Heroku PostgreSQL some of my images couldn't render on HTML. I quickly realised that Heroku MEDIA_URL contained the Amazon Website Services URL instead of the link of my local directory and thus I had to changed the src path to `{{ MEDIA_URL}}image.png`.
![Bug](/freshNow_store/documentation/screenshots/images-bug.jpg)

3. While I was creating my reviews for my product, migrated the relevant models in my database and called the corresponding `Reviews.objects.all().filter(product=product)` in my product_detail function, so I could be able to render each review for each product on my HTML but I didn't get the expected result and the review values were empty. Thus I had to map a relationship between product and reviews either by adding the related_name field or by adding a syntax to access the default related_name: `product.reviews_set.all`. 

![Bug](/freshNow_store/documentation/screenshots/bug-reviews.jpg)

4. Before my project submission Heroku run some database maintenance and rotated my credentials in Gitpod so I wasnt able to open my page in the Browser after running the server in my terminal.
Thus, I had get the new database credentials from my Heroku account and update the DATABASE_URL in my Gitpod environment variables with the new postgres URI. Once I put the new DATABASE_URL in my Gitpod environment I had to stop and restart the workplace.  

![Heroku](/freshNow_store/documentation/screenshots/heroku.png)