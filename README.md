# XRYO

*Liam Hall Milestone Project 4 (Django Full Stack Framework)*

This is my fourth project studying with The Code Institute.

This project focuses on all major aspects of building and deploying a website, building a responsive interactive front end UI, creating a server side web application and finally performing CRUD operations on a database.

I chose to make an e-commerce website which sells snowboard apparel. XRYO offers the following products: goggles, beanies, jumpers and t-shirts (tees). Most of what you’ll need for your next winter holiday. Most products come in a variety of colours so you can choose the one that best fits into your style.

The target audience for this website are all alpine enthusiasts, looking to upgrade their style.

XRYO doesn’t hold stock of their products and works on a dropshipping model. The products are then made to order by the manufacturer and shipped direct to the customer.

The goal of the website is to encourage users to buy more XRYO products whilst making it easy for the user to find what they are after and build a community.

To use the checkout please use the following card number and details:

**Card Number: 4242 4242 4242 4242**

**Month/Year : 04 / 24**

**CVC: 242**

**ZIP: 42424**

[Shop XRYO here](https://xryo.herokuapp.com/)


## Contents 
-   [**UX**](#UX)
    -   [User Stories](#User-Stories)
-   [**Develoyment**](#Development)
    -   [Planning](#Planning)
    -   [Ideas](#Ideas)
    -   [CRUD](#CRUD)
    -   [Templating](#Templating)
    -   [Console Logs Prints Debug and Variables](#Console-Logs-Prints-Debug-and-Variables)
    -   [Commit Messages](#Commit-Messages)
    -   [CSS Variables](#CSS-Variables)

- [**Features**](#Features)
    -   [Live Features](#Live-Features)
    -   [Features Left to Implement](#Features-Left-to-Implement)
- [**Technologies Used**](#Technologies-Used)
- [**Testing**](#Testing)
    -   [Functionality](#Functionality-Testing)
    -   [Issues and Bugs](#Issues-and-Bugs)
- [**Deployment**](#Deployment)
    -   [Local Deployment](#Cloning-Local-Development)
    -   [Remote Deployment](#Remote-Development)
- [**Credits**](#Credits)

## UX

The XRYO website allows users to search, filter and sort all products in the store so they can easily find snowboard attire that meets their requirements. Firstly, links to the major categories can be found in the main site header along with a link to view all the products. When the user lands on the view products page (filter by a category or not) they will be presented with the option to sort the products in the filter bar.
The filter bar once scrolled past will attach itself to the site header so the user can update their filter or search at any point. The current filter / sort settings can be easily identified by either; viewing the **Current** element that appears under the filter bar when an option is selected (also providing the option to clear the selected option) or in the filter / sort dropdown where the selected option will be highlighted. 

On the view products page if a product has variants then all the variants will be presented instead of a single product. These variants all link to the same product details page where the option to swap between variants is available. The selected variant will be highlighted and the images of the specific variant will be the only ones visible along with the main product images.

Viewing a product's details can be easily achieved by simply clicking any part of the product card taking the user to the product details page. Users also have the option to leave reviews on this page which updates the products rating.

Users can then add products to their bag and easily navigate to the checkout page, either from the view bag page or the site notification they receive when a product is added to the bag showing the product details and bag total. 

At checkout the user is presented with a simple and easy to fill in form which will let them know if they have made an error. The details they fill in can be saved (if they are logged in) so they can checkout quicker next time or the user can pre-fill them in on their profile page.

Once their payment has gone through the user will receive an email notification from xryowear@gmail.com with their order number and the details of the items they have ordered. They will then be presented with the order success page. If the user is logged in and didn't checkout as a guest then they will be able to view all their past orders on their profile page and get a full description of the order by clicking on an order.

Users can create a profile by clicking the profile icon in the site header which if they are not logged in will take them to the sign in page with the option to sign up. On signing up the user will receive an email with a link to verify their email.

The user may wish to continue shopping for more items and then go to view their bag before checking out to make sure they have everything. This can be done at any time by clicking the bag icon on the site header which also displays how many items are in their bag. The user will be taken to the view bag page where they can edit their bag. On this page they can update the quantity of a product or remove the product  all together.

Site admins can add, edit and delete products from the product management page, which is  only accessible to site admins (superusers). On adding a product the admin can add a product with multiple images and variants as well as images specific to that variant. On editing the product the admin can set the default image / thumbnail image for either a product or a variant. Products on the product management page can be filtered by category.

Site admins can keep users up to date with everything that's happening in the XRYO community by writing and posting to the XRYO News Blog. Users can access this page from the site header and is listed in the main site nav. Admins have the option to edit and delete blog posts by clicking the appropriate buttons on the relative post. Users are presented with the posts; the most recent at the top so they get the latest news first.

The user will receive messages from the site as they do certain actions or make errors which are presented to the user just under the site header.

## User Stories

Please find user stories and their fulfillment [here](https://github.com/LiamDHall/XRYO/blob/master/readme_documents/xryo_user_stories.pdf) 

## Development

### Planning

Please find the following links to the relevant planning documentation:

[Scope, Strategy and Structure Planning Document](https://github.com/LiamDHall/XRYO/blob/master/readme_documents/xryo_planning_document.pdf).

[Strategy Fulfilment Images](https://github.com/LiamDHall/XRYO/blob/master/readme_images/strategy_fulfilment_images).

[The Data Model and Schema](https://github.com/LiamDHall/XRYO/blob/master/readme_documents/xryo_schema_data_model_labels.pdf). 

I couldn’t find out what data type Django uses for their Foreign Keys so I have represented them as integers that are linked to the corresponding Primary Key (also an integer) of the related model/table to display a relationship. The number in the brackets next to the data type is the max number of characters allowed in that field in a maximum is set. 


[Wireframe](https://github.com/LiamDHall/XRYO/blob/master/readme_documents/xryo_wireframes.pdf). 

The wireframe may vary slightly from the live site as when developing the site the layout didn’t work or a better alternative made the site easier to use.

### Ideas

When thinking about the creation of the XRYO store I wanted to make a site where users could purchase products easily and quickly as possible. With this in mind I planned how to make the process from landing on the site to a successful checkout as easy as possible.
Users should be able to leave feedback for the company on products so the ability for users to review products is a must, this will allow the company to improve products and gather market research on what our customers like and dislike.

The brand should have the ability to inform users of news about the company and events that are going to build hype around the brand to encourage them to engage more in community events and discussions. Eventually leading to them buying more.

When users add an item to the bag they should be given an option to checkout immediately to encourage them to complete the purchase.

The user should be given feedback for the action they take on the site for example trying to access urls they aren’t allowed to be viewed or reached.

### CRUD

Site users can add, edit and update their delivery information. Users can also add reviews to products however they cannot edit or delete them. This is to stop users constantly changing their minds and changing the rating of the product. The site admin can’t edit a user’s review (except in the admin of the site) but can delete them. This is so the site admins can delete reviews if they contain swear words or offensive comments. The rating of the product submitted by the deleted review will not be removed from the product rating.

Users can create profiles by signing up to the site and create orders by going through the checkout.

Site admins have the ability to add, edit and delete products from the product management page. The admin can add multiple images and variants for a single product and/or variant.

### Templating

The webpages for this site have been created using Django templating. A base template has been created including the Doctype, head, site header and footer into which the rest of the templates extend.

Using python in an HTML file allows the ability to show specific elements to a specific user group. For example non-logged in users shouldn’t be shown the **log out** button and vice versa; the logged in user shouldn’t be shown the **log in** button. Normal users shouldn’t be shown links to pages to which only site admins should have access, such as the product management page.

Templating also reduces the overall amount of code as most elements only need to be coded once. This allows editing of the code to be a lot easier; as again there is only one instance of the code that needs to be updated. 

The ability to access variables passed by the view to the template means database objects or attributes of the object can be easily displayed to the user. Groups of objects can be looped through in the code to display the information and that code only needs to be written once.

### Console Logs Prints Debug and Variables

When testing the site; I set it to be built automatically and hosted by Heroku everytime I pushed to Github. This was to test the live site against the local preview. In doing this the site was hosted by Heroku containing console logs and print functions.

With the site in this state it was presented only to test users as I didn't want to remove or change any of them just to have to add them or revert them back at a later date. 

**There is no console logs or print functions in the live site**

The site is able to adapt to different environments by the use of environment variables.

If a DEVELOPMENT variable is in the environment variables then Django’s debug will be turned on.

** No DEVELOPMENT variable is set in the app of the live site and the debug is turned off**

If a DATABASE_URL variable is in the environment then the app will use that variable to link to the database it points to.

This variable controls which database is used. If not set, the site will use the SQLite3 database. Otherwise the site will use the database the variable is set to. 

**The DATABASE_URL is set as the link to the postgres database in the environment of the live site meaning, the live site is using the remote postgres database**

If a USE_AWS variable is present in the site's environment variables then the site will use the remote S3 bucket to store, get and upload media and static files otherwise the local storage will be used.

Whether images are set to be resized on upload is also controlled by this variable, as I couldn’t get the function that resizes them to work with the S3 bucket. 

**There is a USE_AWS variable present in the environment of the live site meaning the live site is using the S3 bucket to load and store static and media files, and images will not be resized on upload**

### Commit Messages

During the project I tried to adhere the following rules as much as possible:
-   I aimed to keep the subject line to 50 characters, but where appropriate I extended it to 72.
-   I wrapped each line of the message body at 72 characters as some repositories don't automatically wrap text to new lines.
-   If a single document was edited in the commit, I noted it in the commit in the format **document: Subject line** so when future developers look through the commits they know which document is affected.
-   I only capitalised the first letter of the subject line as some developers use filters that look for capitalisation.

### CSS Variables

I used a CSS Variable to set the primary colour of buttons throughout the site. I did this so if a developer at a later date wants to change the colour of all the primary buttons at once they only need to update one line of code. 

## Features
 
### Live Features

-	**Fix Site Header:** The user always has access to the main site nav as well as the search form.

-	**Hero Landing Page:** On first arriving to the site; the user will see a large hero image with text that quickly tells the user the purpose of the site.

-	**Product Variants:** If a product has variants, each variant is presented to the user on the **view all products** page; instead of them being displayed as a single product. All the variants are still the same product, but when clicked, will take the user to the products detail page where the user will see images specific to that variant and then the product’s image in the image carousel. The option to swap between variants is given to the user in the form of images that show the different variants which when selected reload the page to show the images specific to the selected variant. When variants are added to the bag they are treated as separate items meaning you can update the quantity of one or remove one without affecting the others. Currently in the live site the product can’t have variants and sizes if both are present for an item; the variant will take precedence and the sizes will be ignored.

-   **Swaping Image From Carousel To Preview:** On the products details page the images from the carousel can be swapped with the main image on the page by simply clicking it.

-	**Product Management:** This is a page only accessible by site admins (superusers) where products can be added, updated and deleted. The existing products can be filtered by category. When a product is clicked the admin is taken to the product edit page where they can upload more images, set default images, delete existing images or variants as well as edit and add new variants. The default image for a product  can only be set on the edit page once a new image has been uploaded due to the Image object having to be created before the attribute can be set. Setting a default image will set the default attribute of all other images in the folder to **False**.

-	**Multiple Image Uploading and Albums:** Multiple images can be uploaded in a single product creation or editing session due to a new image model being created for each one on upload. These images are then related to an album object which is then related to a specific product or variant object creating a many to many relationship via the album-image joining table. The album table is created automatically and set as the product or variant’s album on creation of the product or variant. If the product name is changed, the album name will update to match. However the file path for the images already in the album will not update. The old images will remain in the same folder in the local or remote storage. New images added to the album will have the new file path including the new album name. So the new image will be stored in a new folder in the storage.

    The change in album name has no effect on retrieving images in the old folder as the image object retains the old file path and is not updated. To clarify, the images with the old file path will still be in the album even though the name has changed, these images will still be retrievable.

-	**Image Filing system:** Images are stored in the media folder and then inside another folder whose name matches the product or variant image to which the image belongs. As mentioned in **Multiple Image Uploading and Albums** the file path of the image doesn’t update when the owning product or variant changes name; so I add the id of the parent to the album name so it could alway be identified.

-	**Product Filtering and Search:** The user can easily filter the product from the main site nav into the category of their choice. If a user uses the search bar to look at a product the resulting products can be filtered and sorted from the filter bar. Currently the search functionality means the query only searches for the search term in name and description of the product. So searching for a category name may not produce any results if the product doesn’t have the category name in its name or description

-	**Filter and Sort Bar:** This bar give the user the option to filter down their search results to a single category or sort products by the following order: **A-Z, Z-A, Rating, Price: Low-High, Price: High-Low**. Once a user scrolls past this bar it attaches itself to the site header so the user can easily change the sorting or filtering at any time. The currently selected filter or sorting will be highlighted in the dropdown and an option to clear them is presented below the bar.

-	**Blog:** Allows the user to keep the update date with everythings that’s going on with XRYO and get the latest updates on deals, sales and events. The blog is a great feature to which the site admins can post to; to share news of the XRYO community helping to grow the Company's community. The blog can be used by the admin as another platform to promote sales and events.

-	**Profile / Order History:** Uses can create an account by signing up / registering. A profile will automatically be created for them where they can fill in their default delivery details and view their order history. The user's order history will be presented with  key pieces of information about the order so the user can easily identify the one they are looking for. On clicking an order in the order history the user is taken to an adapted checkout success page where they can view the full order details. Only the owner of the order can view their order history on the profile page. 

-	**Bag:** Used by the user to store products or variants whilst they continue to shop.
Whilst on the bag page the user can update the quantity of an item or remove the item altogether. An order summary is presented to the user along with the delivery cost and grand total; with the option to checkout or keep shopping.

-	**Checkout Autofill:** The checkout page delivery information will be auto filled by the user’s default delivery information if it is set by the user in the profile app. An option to save the data entered is also offered at the bottom of the form so users can save their delivery address if it has changed.

-	**Checkout, Stripe Payment & Webhooks:** The site uses stripe to verify and process order payments. If a user inadvertently leaves the page before the checkout form has been submitted and the checkout success page has loaded, stripe will still process the order if the webhook was sent. If the payment is successful then stripe will send a webhook to the site which will be sent to the correct handler and if the order is in the database will create one after attempting to find it 5 times. The checkout form will let users know if they have made a mistake filling it out.

-	**Reviews and Product Rating:** Site users may wish to review a product which is available on the product detail page. The user has to give a score out of 5 and if they would like to add a comment about how they liked or disliked the product. On submission of the review the products rating will be updated to reflect the new review submission.

-	**Messages:** Are used throughout the site to give users feedback on actions whilst using the site. When a user adds a product to their bag a message will appear displaying the product, the amount of that product or variant is in their bag and the price of the item. This message will also show the total price of the bag info and have links to checkout for those users looking to quickly buy one item.

-	**Emails:** Are sent to users so they can verify their email address, so people can't sign up without a valid email. An email confirmation of a user’s order will be sent to them when they complete through the checkout process.

-	**Bag Count and Total in Header:** The number of items in the bag is reflected on the bag icon in the site header. The total price of all the products in the bag is also displayed next to the bag on larger screens. This total does not include the delivery charge and some test users were confused when adding a single item and the bag total not matching the product price. 

### Features Left to Implement

The following features are suggestions to improve the site for developers to include if they wish to continue developing this project or myself at a later date.

-	**Wishlist / Save Items For Later** Allow users to mark items as they see them and view the list on the profile page where they can quickly add them to the bag. Vice versa - allow the user to move items in their bag to the Save for Later section so they can order them at a later date.

-	**Image Resizing on Upload** I had this feature working in the development version of the site by once the image files where stored in the S3 bucket it stopped working so I have set it to only run when in the development environment. The idea of this feature was to make sure all images that were uploaded were the same size and would behave the same in a responsive design.

-	**Stock Control** When the store starts storing their own stock and not relying on the manufacturer to make to order, products will need to be stock controlled. Then when the stock level hits 0 the product can no longer be added to a user’s basket.

-	**Reserve Items In Bag** When a user adds an item to their bag they are not forced to checkout immediately in case someone else checkouts before them. A reserve timer should be set so users don’t hoard items in their bag. I would recommend items in a bag to be reserved for 15 mins before being added back to the general stock.

-	**Verify purchase before user can leave a review:**This will stop users being able to post lots of fake reviews. This can be achieved by only allowing users to review a product if it appears in their order history.

-	**Allow registered users to comment on blog posts:** So much more engagement would be created if users were able to comment on blog posts which would lead to community growth.


## Technologies Used

-	[HTML 5](https://en.wikipedia.org/wiki/HTML5): language used to structure and provide content of pages of the website.

-	[CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets): visual language used to style and format the html.

-	[Javascript](https://en.wikipedia.org/wiki/JavaScript) & [JQuery](https://en.wikipedia.org/wiki/JQuery): JavaScript used for frontend functionality as well as dynamically adding, removing and updating elements. 

-	[Python](https://www.python.org/): Python is used to run the back end of the web application. It is also used to query the databaseand perform CRUD operations on the database.

-	[Django](https://www.djangoproject.com/): is a python framework used to set up the web application.

-   [Heroku](https://www.heroku.com/): platform used to host the web application.

-   [SQLite3](https://www.sqlite.org/index.html): provides the development database the web application uses to store and query data.

-   [PostgreSQL](https://www.postgresql.org/): provides the deployment database the web application uses to store and query data.

-   [AWS](https://aws.amazon.com/): provides the deployment storage for static and media files.

-   [Stripe](https://stripe.com/): provides the payment system for the sites checkout. It also provides the code to receive webhooks which I have adapted to my needs

-	[Bootstrap Framework](https://getbootstrap.com/docs/4.1/layout/grid/): provides a grid system to insure a mobile-first design and responsive website which adapts to different screen sizes of devices.

-   [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): allows bootstrap and custom classes to be added to django forms.

-   [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/): checks how much of the sites python code is tested by the existing tests and provides a print out.

-   [Pillow](https://pillow.readthedocs.io/en/stable/):allows upload of images to the local or remote storage depending on which version of the site is running.


-	[Swiper JS API](https://swiperjs.com/swiper-api): provides the image carousel.

-	[Gitpod](https://gitpod.io/): the Integrated Development Environment used to write the code for this project. Also provides a preview of the website in a browser which was then used for testing.
 
-	[Gitpod Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki?hl=en): made it easier and faster to open the repository in my IDE directly from Github in a web browser.
 
-   [Git](https://git-scm.com/): used for version control and to push the control to a remote repository to be stored.
 
-   [Github](https://github.com/): used for as a repository to store the versions of the website. 
 
-	[Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html): optimise the images for the web.
 
-	[Adobe Illustrator](https://www.adobe.com/uk/products/illustrator.html): create the logo for the website.
 
-	[Google Font](https://fonts.google.com/): font for website.
 
-	[Font Awesome](https://fontawesome.com/): styles and provides icons.

-	[Flat Icon](https://www.flaticon.com/): provided the icon used in the no image photo.
 
-	[Google Chrome](https://www.google.com/intl/en_uk/chrome/), [Microsoft Edge](https://www.microsoft.com/en-us/edge), [Firefox](https://www.mozilla.org/en-GB/firefox/new/) and [Opera](https://www.opera.com): to test browser compatibility.
 
-	[Google Chrome Dev Tool](https://developers.google.com/web/tools/chrome-devtools): main tool for testing. Inspecting elements and troubleshooting.

-	[dbdesigner](https://www.dbdesigner.net/):  used to design and model the database schema
 
## Testing
 
### **HTML**

I used [W3C Markup Validation Service](https://validator.w3.org/) to check my html was valid.

**Errors**

No errors produced.

**Warnings**

No warnings produced.

### **CSS**

I used [W3C Jigsaw Validation](https://jigsaw.w3.org/css-validator/) direct input feature to check if my CSS was valid.

**Errors**

No errors produced

**Warnings**

A warning occurred for all vendor extensions.
The following warnings were produced when running my site through validation:

--primary-cta is an unknown vendor extension
-ms-flex-order is an unknown vendor extension
--primary-cta is an unknown vendor extension
-webkit-transform is an unknown vendor extension
-moz-transform is an unknown vendor extension
-ms-transform is an unknown vendor extension
-o-transform is an unknown vendor extension
-webkit-text-stroke-width is an unknown vendor extension
-webkit-text-stroke-color is an unknown vendor extension
-webkit-text-stroke-width is an unknown vendor extension
-webkit-text-stroke-color is an unknown vendor extension

I have left this code in the site to ensure compatibility with the maximum number of browsers.

**--primary-cta is an unknown vendor extension** is caused by the use of CSS Variables.

**Third Party CSS**

All other errors and warning are caused by [Swiper JS API](https://swiperjs.com/swiper-api), [Font Awesome](https://fontawesome.com/) and [Bootstrap Framework](https://getbootstrap.com/docs/4.1/layout/grid/).

On the product details page where SwiperJS is used a warning appearing the console:

The warning is below

<img src="https://github.com/LiamDHall/XRYO/blob/master/readme_images/swiper_console_warning.png">

### **JS**

I used [JS Hints](https://jshint.com/) to check my JavaScript was valid.

**Errors**

No errors produced

**Warnings**

I got the following Warnings

**template literal syntax' is only available in ES6 (use 'esversion: 6').'**

A warning that old browsers not support the use of template literal

**$ is an undefined variable** 

Produced because the validator doesn’t know how to handle JQuery.

### **Python**

I ran all code written by myself through [pep8online](http://pep8online.com/) to check if my Python was PEP8 compliant.

All code written by myself passed the PEP8 check. Some auto generated code from Django did trigger some errors. The errors were that lines were too long and over 72 characters. These lines appear in the settings.py file and are found in the **AUTH_PASSWORD_VALIDATORS** section

I have written custom tests to test the views for some of the apps for this site using the Django TestCase class. These tests do not cover 100% of the code.

I have written tests for the following apps to test the following things:

-	**Bag:** 
	-	The view’s response and the correct template is rendered
	-	A product being added to the bag enters the bag in the session and is correctly formatted by the context processor. An individual test for each product type (product with no variant or sizes, product with variant and product with size) has its own test.
	-	Updating the quantity of a product in the bag. An individual test for each product type (product with on variant or sizes, product with variant and product with size) has its own test.
	-	Removing an item from the bag. An individual test for each product type (product with no variant or sizes, product with variant and product with size) has its own test.
	
-	**Products**
	-	Test each view’s response and the correct template is rendered

-	**Home**
	-	The view’s response and the correct template is rendered

### **Functionality Testing**

#### **Links**

I have manually tested each link and they all work as intended and external links open in a new tab.
 
#### **Device Compatibility**

I have tested a number of devices in the Google Chrome Developer Tool in the Google Dev Tool: **Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, iPhon: 5/SE/6/7/8/6+/7+/8+/X, Ipad & Pro** 

The site is compatible down to devices with screens that are 318px wide.

I have tested the actual touch screen usability and accessibility on a Samsung Galaxy A40 and it works as intended.

#### **Browser Compatibility**

I have tested the site in following browsers: [Google Chrome](https://www.google.com/intl/en_uk/chrome/), [Microsoft Edge](https://www.microsoft.com/en-us/edge), [Firefox](https://www.mozilla.org/en-GB/firefox/new/) and [Opera](https://www.opera.com).

The website works the same across all the browsers.

### Issues and Bugs

#### **Variants of products not displaying on the view products page.**

Due to the django templating language using different syntax than python

**Fix: {% for variant in product.variant_set.all %} will loop through the variants of a product**

#### **When testing the removal of products from the bag, the session variable used in the test wouldn’t update even though when printed the session had the correct contents.**

**Fix: In the test the session variable had to be set again after it was updated before being self asserted**

#### **The submit button on the checkout form not disabling when pressed**

Due to the post load JS being loaded twice due to the {% block add_postload_js %} being inside the {% block content %}.

**Fix: Move the add_postload_js block out of the content block**

#### **On submitting a review for a product the form doesn’t clear**

I believe this is due to the browser caching the form data and auto filling it on reload.

**This bug is still present in the live site**

#### **Image resizing doesn’t work in the deployed/live version of the site**

Due to the images being stored in an AWS S3 bucket which I would allow the editing of files and reupload them I made a few attempts at getting the resizing to work which can being found in the following commits:

-	[f7a57b8](https://github.com/LiamDHall/XRYO/commit/f7a57b8425aa945257529b5f573dbdaf8566da2b)
-	[fd55420](https://github.com/LiamDHall/XRYO/commit/fd55420ca38fab7b7fcd3514be69b5f8bfe6199b)
-	[154f503](https://github.com/LiamDHall/XRYO/commit/154f503eac22f03763e9436ce525f32ad5db7afb)

**This feature doesn’t work when the storage for media files is set to a remote storage such as a S3 bunker, however this feature does work in the development environment where the storage is set to local**

#### **Error message that the user can’t checkout as bag is empty appears if the user press back on checkout success page**

Due to when the back button is pressed from this page it will try to take the user to the checkout page which can't be reached if the bag is empty.

The user is redirect back to other page and the error message appears

**This bug is still present in the live site**

#### **If a user typed in a product url for a product that has variants and did not specify the variant id in the url the user would be able to add the product to the bag without a variant**

Due to there being two different views to handle product and products with variants each rendering a different template. Meaning if the variant id is left off the url the wrong template is loaded for the product.

**Fix: Add redirect to the view that handles products without variants to check if the product has variant and if so redirect to the correct view**  

## Deployment

This web application is hosted on Heroku. [View Live Site](https://xryo.herokuapp.com/)

### Cloning Local Development

1. Open the Github repository - <https://github.com/LiamDHall/XRYO>
2.  Click the green drop down that says **Code**, **Download** or **Clone**.
 
    <img src="https://github.com/LiamDHall/XRYO/blob/master/readme_images/clone_button.png">
 
3.  To clone with HTTPS copy the URL in the box. <https://github.com/liamdhall/XRYO.git>
4.  Open up your Integrated Development Environment (IDE).
5.  Open your Command Line or equivalent if not already.
6.  Type **git clone** and paste the copied URL from step 3. 
    (Should look like **https://github.com/LiamDHall/XRYO.git**)
7.  If you then wanted to copy it to a specific folder add the folder name to the end.
    (Should look like **git clone https://github.com/liamdhall/XRYO.git folder-name**)
8.  Press Enter and a local clone will be created.

The following steps are then required to make the clone work as intended using Gitpod.
The following steps may vary based on the IDE you use.

9. Install the required dependencies by running **pip3 install -r requirements.txt**

10. Create a [Stripe](https://stripe.com/) account and follow the steps until you land on the dashboard then under the **Developers** tab click on API keys where you will find your stripe publishable key and your stripe secret key

11. Follow the steps in their documentation to setup a test webhook endpoint as your IDE preview checkout webhook url **(your_IDE_preview_address/checkout/wh/)**where you will get your webhook endpoint signing secret 
12. In your IDE set the following variables replacing the **placeholders** with your correct values
    	
	DEVELOPMENT === True (only set/create this variable if you want the debug on)
	SECRET_KEY === **your django secret key**
	STRIPE_PUBLIC_KEY === **your stripe publishable key**
    SECRET_KEY === **your stripe secret key**
    STRIPE_WH_SECRET === **your webhook endpoint signing secret**

13. Create a superuser by running the command line **$ python manage.py createsuperuser**
And fill in the information it asks for.
14. In command line run **python3 manage.py runserver** 
(I did have an issue after deploying the live site where the static files wouldn’t load when I went back to deployment / local version of the site. If this occurs, run **python3 manage.py runserver --insecure**)
15. A pop up will appear in the bottom right hand corner.
16. Click on **Open Browser** and the website opens in a new tab.
17. Login to the admin of the site by adding **/admin** on to the url and verify your email address in the **Email Address** section.

### Remote Development

This web application is hosted on Heroku. [View Live Site](https://xryo.herokuapp.com/)

1. Sign up to [Heroku](https://www.heroku.com/) and create a new app.
2. Set a variable in your heroku app:

	SECRET_KEY === **your django secret key**

3. On the resources tab search for **postgres** and click on **Heroku Postgres** and set it to the free plan.
4. Set a variable in your IDE as:
DATABASE_URL equal to <you postgres url> (which you can find in your heroku app variables.)

5.  Make sure you have Procfile and a requirements.txt created.
6. Your Procfile file should contain one line of code which is as follows: **web: gunicorn <your app name>.wsgi:application**

7. Run the command line **python3 manage.py migrate** to set up the database
8. Create a superuser by running the command line **$ python manage.py createsuperuser**
And fill in the information it asks for.

9. Commit to Github

10. **(If you don’t wish to store the static files in a AWS S3 bucket this step is unnecessary)** 
Set a variable in your heroku app as **DISABLE_COLLECTSTATIC** equal to 1 to stop heroku collecting static files

11. Add your new app host name to your settings.py file in the ALLOWED_HOSTS list

12. Setup Heroku git by running the command **heroku git:remote -a <your app name>
13. Commit to heroku by running the command ** git push heroku master**

14. To set up automatic deployment go to your Heroku app and under the deploy tab set the deployment method to Github and then search for your repository, then click connect. Then click the **Enable Automatic Deploys** 

**The following steps are then required to make the site work as intended and using AWS to host static files. The following steps may vary based on the IDE you use.**

15. Create a AWS account and create a new S3 bucket and make sure your bucket has public access turned on, static website hosting turned on, CORS is configured correctly, a correct security policy with all actions allowed on all resources in the bucket and contains your arn number and finally have the List Objects checked on everyone on the Access Control Tab.

16. Create an Amazon IAM user in a group that has a policy that allows them to access all resources in the new bucket. Through the creation of this user you will be given the option to download a .csv file which will contain the user API keys.

17. Set these new keys as variables in Heroku App:

AWS_ACCESS_KEY_ID  === **your Access key ID**
AWS_SECRET_ACCESS_KEY === **your Secret access key**
USE_AWS === True

18. Remove **DISABLE_COLLECTSTATIC** variable from your Heroku App
19. In setting.py set:

	AWS_STORAGE_BUCKET_NAME === **your bucket name**
	AWS_S3_REGION_NAME == **your bucket’s region**
	
20. Create a media folder in your bucket
21.  Commit and push all files to Github. Your static files should appear in your S3 bucket 
22. Login to the admin of the site by adding adding **/admin** on to the host url and verify your email address in the **Email Address** section. This will allow other users to login.

**Set up Stripe Payment**

23. Create a [Stripe](https://stripe.com/) account and follow the steps until you land on the dashboard then under the **Developers** tab click on API keys where you will find your stripe publishable key and your stripe secret key

24. Follow the steps in their documentation to setup a test webhook endpoint as your heroku app checkout webhook url **(https://your_app_name.herokuapp.com/checkout/wh/)** where you will get your webhook endpoint signing secret 
25. Set these new keys as variables in Heroku App:
    	
	STRIPE_PUBLIC_KEY === **your stripe publishable key**
SECRET_KEY === **your stripe secret key**
STRIPE_WH_SECRET === **your webhook endpoint signing secret**


**Sending Real Emails**

26. Go to your google account security settings and turn on two step verification and follow the steps. A new option under the sign in google heading called **App passwords** click it and on the app password screen set the app to **Mail**  and the device to whatever you want. Click **Generate** and you will be present with a password

27. Set these new keys as variables in Heroku App:

	GMAIL_PASSCODE === **your gmail password**
GMAIL_USER === **gmail address set up with the password**


## Credits

This project is inspired by the Code Institute mini project Boutique Ado

Third parties code has been credited in the code of the website where appropriate.

-   [skelly](https://www.codeply.com/go/J70zkpygvk): CSS to create a custom breakpoint for bootstrap.

    -   **Adapted to my needs by:**
        -   changing the screen width so that the breakpoint is active.

-   [Stripe](https://stripe.com/docs): webhooks.py is taken from the stripe documentation.

-   **Adapted to my needs by:**
        -	added an event map to decide what handler handles which webhook.
        -	added POST decorator to the function as it will only be receiving POST requests.

-   [NathanD / Akseli Palén](https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model): Provided the rating field used in the review form to stop users putting in decimals and any number over 5.

-   [Code Institute](https://codeinstitute.net/) - Provided the .theia, .gitpod.dockerfile, .gitpod.yml files in the repository which have not been modified by myself in any way.

#### Images

All images are my own and I have consent from those who are featured in them to use the photos.

### Acknowledgements

I would like to thank the Code Institute Tutor and my mentor Gerard Mcbride who supported me throughout this project.
 
I would also like to thank the following people for being test users and for helping me spell check the site:
-   Chris H
-   Sasha S
-   Liz H
-   James T
-   Emma S

I would also like to additionally thank Sasha S for allowing me to use an image of her on the landing page.

I used the following websites for my research [W3C School](https://www.w3schools.com/), [Stack Overflow](https://stackoverflow.com/), [Django Documents](https://docs.djangoproject.com/en/3.2/)  and [Stripe Documents](https://stripe.com/docs) for this project.


