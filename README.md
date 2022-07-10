<div align ="center">

# **FreshNow Food Delivery**

</div>

[View the live site here](https://freshnow-store.herokuapp.com/)

<div align ="center">

![Final project image home page](freshNow_store/documentation/responsive_layout.png)

</div>

## **Introduction**

Welcome to FreshNow store, an e-commerce site was built to fill the requirements of the final project part of my studies on Web Developer Application Diploma. 
This is a fully responsive website, developed by utilising the principles of UX design and using HTML, CSS, Bootstrap, JavaScript, jQuery, Python, Django technologies as well as  SQL database through Heroku PostgreSQL and Stripe online test payments.
FreshNow is a full-stack site based around a business logic used to control a centrally-owned dataset and accepts purchases via Stripe test card details. For further details on cards numbers click [here](https://stripe.com/docs/testing#cards).

## **Contents**

[User Experience (UX)](#user-experience-ux)
* [User Stories](#user-stories)

[Design](#design)
* [Colour Scheme](#colour-scheme)
* [Typography](#typography)
* [Imagery](#imagery)
* [Wireframes](#wireframes)
* [Features](#features)
* [Future Features](#future-features)

[Information Architecture](#information-architecture)
* [Database Design](#database-design)

[Technologies Used](#technologies-used)
* [Languages Used](#languages-used)
* [Site Design](#site-design)
* [Hosting](#hosting)
* [Databases Platform and Cloud Storage](#databases-platform-and-cloud-storage)
* [Frameworks and Libraries](#frameworks-and-libraries)
* [Other Technologies](#other-technologies)
* [Testing](#testing)

[Deployment](#deployment)
* [Requirements for Deployment](#requirements-for-deployment)
* [Initial Deployment](#initial-deployment)
* [How to Fork it](#how-to-fork-it)
* [Making a Local Clone](#making-a-local-clone)

[Testing and Project Barrier Solutions](#testing-and-project-barrier-solutions)

[Credits](#credits)
* [Code](#code)
* [Content](#content)
* [Media](#media)
* [Acknowledgements](#acknowledgements)

---
## **User Experience (UX)**

### Regular Site User Stories
* As a site user, I want the main purpose to be clear at first glance so that I can instantly understand if this is the correct site for me.
* As site user, I wish to create an account for future purchases and be able to view my payment history so that I track my payment information. 
* As site user, I wish to login or logout so that I can easily access my profile.
* As site user, I wish to receive a confirmation email after registering my new account, so I can verify that the process was successful.

### Customer Shopper Stories
* As a shopper, I wish to view all the products so that I can choose what I would like to buy.
* As a shopper, I wish to search for a specific product and category so that I find what I want faster.
* As a shopper, I wish to be able to sort the products by price and calories so that I find what I want directly without wasting time on searching. 
* As a shopper, I wish to view products in more detail so I am aware of the full product information.
* As a shopper,  I wish to get visual feedback so  an action has been completed so that avoid making mistakes while adding, editing and deleting products.
* As a shopper, I wish to easily add, update or delete items in my bag where I can view a summary of my orders along with the total price so that I can stick with my budget.
* As a shopper, I wish to easily make a payment so that I smoothly complete the checkout. 

 
### Customers Stories  (Logged in Users) 
* As a logged-in user, I want to be able to view other people's reviews so that I know if the products worth purchasing. 
* As a logged-in user, I want  to be able to add or edit my own reviews to products so that I share my opinion with the other customers.
* As a logged-in user, I want to be able to add products to my wishlist, so that I can view those products later.
* As a logged-in user, I want to be able to delete products from my wishlist, so that I can change my mind.
* As a logged-in user, I want to be able to save my profile details, so that I can avoid retyping my details everytime I place an order.
* As a logged-in user, I want to have order history viewable, so that I can view my past orders.


### Creator Goals
* As a creator, I want the site to be easy to navigate.
* As a creator, I want to allow users to filter through products.
* As a creator, I want to allows admins to Add/Edit/Delete products to/from the store.

## **Design**

### Colour Scheme
* The website uses the colours found...
  * [Colour Palette - Coolers.co](https://coolors.co/0f5520-fffaea-990b16-6c9c79)
  ![Colour Palette](/freshNow_store/documentation/FreshNow%20Color%20Palette.png)

### Typography

* The website uses two fonts from [Google Fonts](https://fonts.google.com/?query=Suwannaphum).
  [....]

### Imagery

* The icons of the site were taken from font-awesome and used in logo and cards for styling, emphasizing the costumed fields and impoving the site's readability.
* All the images used for the site's products were taken from Unsplash which offers royalty free images. 
* The Home page image which gives a nice and visually appealing background have been taken from Unsplash and aims to show the products in an irresistible manner. 
* The About Us page image was taken from Usplash and aims to give the user intuitive information about the restaurant. 

### Wireframes
Although the project relied on the wireframes below, there are some differences between the them and the final wedsite due to change of mind for different/better UI and functionality. The wireframes show the desktop, mobile and tablet for view for this project:

* [Home](documentation/wireframes/home.png)
* [About Us](documentation/wireframes/our_story.png)---
* [Sign Up](documentation/wireframes/register-wireframe.png)
* [Log In](documentation/wireframes/signin-wireframe.png)
* [My Profile](documentation/wireframes/profile.png)----
* [Wishlist](documentation/wireframes/wishlist-wireframe.png)
* [Products Detail](documentation/wireframes/product-details-wireframe.png)
* [Product and Reviews](documentation/wireframes/product_and_reviews.png)----
* [Shopping Cart](documentation/wireframes/shopping-bag-wireframe.png)
* [Checkout](documentation/wireframes/checkout-wireframes.png)
* [Order Success](documentation/wireframes/order_success.png)---
* [Add Products](documentation/wireframes/add_product.png)---

## Features

* Home
  * Hero Image
  * List of Categories that lead to the Categorized Products when clicked
  * ![Home](/freshNow_store/documentation/screenshots/home-feature.png)

* Navigation Bar
  * ![Navigarion Bar](/freshNow_store/documentation/screenshots/navigation-bar.png)

* Footer
  * ![Footer](/freshNow_store/documentation/screenshots/footer.png)

* About Us
  * ![About Us](/freshNow_store/documentation/screenshots/about-us.png)

* View a List of Products
  * Sort the List of Products by:
    * _Calories_ (low - high / high - low)
    * _Price_ (low - high / high - low)
    * _Ratings_ (low - high / high - low)
    * ![Sort By Name In Category](/freshNow_store/documentation/screenshots/sort.png)

* Search Bar
  * Sort by meal name:
    * ![Sort By Meal Name](/freshNow_store/documentation/screenshots/search-bar.png)

* View product Details
  * ![Product details](/freshNow_store/documentation/screenshots/product-details.png)
  

* Add Products to Shopping Cart
 * ![Product Details](/freshNow_store/documentation/screenshots/add-products.png)

* Update quantity and delete Products from Shopping Cart
  * ![Update, Delete Products from Cart](/freshNow_store/documentation/screenshots/update-delete-product.png)

* Make purchases of the products in the Shopping Cart
  * If the payment fails, the user is directed back to the checkout form and is shown a message that the payment failed.
  * If the payment succeeds, the user gets a success message and redirects to a page containing all the order details.
  * Ability for a registered user to save their details after making a purchase.
  * ![Checkout](/freshNow_store/documentation/screenshots/checkout.png)

  * ![Checkout Success](/freshNow_store/documentation/screenshots/success-checkout.png)

* Profile
  * Update Profile
  * User's order history is saved on their profile.
  * ![Update Profile and Order History](/freshNow_store/documentation/screenshots/user-profile.png)

* Register/Sign In
* Sign Out
* Email Verification
  * ![Register, Sign In, Sign Out, Verify Email](/freshNow_store/documentation/screenshots/register-account.png)

* Wishlist (for the logged in user)
  * Add or remove items from the Wishlist
  * Display wishlisted items with a red heart on Wishlist page
  * ![Wishlist](/freshNow_store/documentation/screenshots/add-wishlist.png)

  * ![Wishlist](/freshNow_store/documentation/screenshots/wishlist.png)

* Diplay of Reviews with Username and the Date it was added, for each Product 
* Submit Reviews (for the logged in user)
* Edit Review
  * ![ Edit Review](/freshNow_store/documentation/screenshots/review.png)

  * ![ Submit Review](/freshNow_store/documentation/screenshots/submit-review.png)


* Store owner has the ability to add / edit and delete Products
  * ![Update, Delete](documentation/screenshots/update-delete-product.png)
  * ![Add Product](documentation/screenshots/add-product.png)


* 404 Page Not Found
* 500 Internal Server Error
  * ![404 Page Not Found](documentation/screenshots/iphone375/error404.png)

---


### Future Features

[.....]
* Contact Page

[Back to Top](#la-fraschetta)

## **Information Architecture**

### Navigation bar

The navigation bar changes depending on user status and screen size:

| Nav Link | Logged Out | Logged In (User) | Logged In (Admin) |
|-------|-----|-----|-----|
| Logo (small screen) | &#10060; | &#10060; | &#10060; |
| Logo (large screen) | &#9989; | &#9989; | &#9989; |
| Home | &#9989; | &#9989; | &#9989; |
|Dropdown list of meals categories | &#9989; | &#9989; | &#9989; |
| About Us | &#9989; | &#9989; | &#9989; |
| Search Bar | &#9989; | &#9989; | &#9989; |
| My Account | &#9989; | &#9989; | &#9989; |
| My Account dropdown - Login | &#9989; | &#10060; | &#10060; |
| My Account dropdown - Register | &#9989; | &#10060; | &#10060; |
| My Account dropdown - Profile | &#10060; | &#9989; | &#9989; |
| My Account dropdown - Log Out | &#10060; | &#9989; | &#9989; |
| My Account dropdown - Add Product | &#10060; | &#10060; | &#9989; |
| Wishlist | &#10060; | &#9989; | &#9989; |
| Shopping Basket Icon | &#9989; | &#9989; | &#9989; |