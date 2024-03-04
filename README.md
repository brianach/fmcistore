# FMCI Store

![FMCI logo](media/logo.png)

[FMCI Store](https://fmcistore-366e47ff9414.herokuapp.com/) gives interested users and visitors the opportunity to buy FMCI merchandice as well as the ability to view facilities and services on offer to businesses and automotive product developers. 

- Visitors have access to all the published information and can create and complete orders. Visitors can also choose to register on the site.

- Registered users can access records of previous purchases in their profile. 

- Staff users can edit existing products and also add or delete products as necessary.

- Wearable merchandice can be ordered in various sizes wherewhen the option is available.

![FMCI Store](/static/readmeimg/screens.png)

&nbsp;
# Table of Contents

- [FMCI Store](#fmci-store)
- [Table of Contents](#table-of-contents)
- [Features](#features)
  - [Home Page](#home-page)
  - [Store](#store)
  - [Other](#other-offerings)
  - [Authentication](#authentication)

- [Design](#design)
  - [Database Model](#database-model)
  - [General Color Scheme](#general-color-scheme)
  - [Logo](#logo)
  - [Home](#home)
  - [Store](#store-1)
  - [Other](#other-offerings-1)

- [User Experience & Testing](#user-experience--testing)
  - [User Stories](#user-stories)
    - [Visitor Journey](#visitor-journey)
    - [User Journey](#user-journey)
    - [Staff Journey](#staff-journey)

- [Technologies](#technologies)
- [Deployment](#deployment)
  - [Deploy site using Heroku](#deploy-site-using-heroku)
  - [Deployment Procedure](#deployment-procedure)
  - [Steps to clone site](#steps-to-clone-site)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgement](#acknowledgement)
- [Notes](#notes)
  - [Map Popup Dialog](#map-popup-dialog)

---
---
&nbsp;

# Features

## Home Page

The home page contains a summary of what FMCI does preceded by a link to the main FMCI homepage. A scrolling carousel runs at the bottom of the page which displays a clickable logo for each of FMCI's partners which when clicked open the partner's home page on a separate tab. The carousel is loaded from a simple django database model which can be edited by a superuser via the admin page.

## Store

Products can be purchased from a number of cathegories on the store page. The store dropdown menu allows for viewing the products by category or viewing the entire store on a single page. Visitors can order products without having to register and account. Registered users can access and modify their contact details and also view a list of previous orders. They can also click on any individual order to see what products are contained in it. Staff users can modify the existing products, delete products or add new products as required. Both users and staff users can see that they are logged in as the login menu item changes to their full name and is highlighted for better visibility.

## Other Offerings

The site shows what onsite spaces such as desks and labs are available to interested users. A table listing the various option is displayed alongside images of the spaces on offer. Additionally, compute and development services are offered and availabe for tenant or onsite customers. Tables outlining the various offerings are available for visitors and users to view.


## Authentication

Users can register an account which gives them the ability to see their order history. Logged in users will see their full name displayed above the information banner and highllighted for visibility. 

---
---
&nbsp;

# Design

## Database Model

The FMCI databases utilizes a number of models with relationships as shown in the following diagram. 

<details><summary>ERM</summary>

![ERM](/static/readmeimg/erm.png)</details>

There are five categories of products and services of which only specific products may be purchased online. The Spaces and Services are purchases by emailing FMCI or by tenant customers and are only available on site.

## General Color Scheme

I based the color scheme on the main [FMCI](https://futuremobilityireland.ie/) webpage. Font colours were chosen to make the best use of contrast in order to assist with visbility and clarity.

<details><summary>Color Scheme</summary>

![Color Scheme](/static/readmeimg/colors.png)</details>

## Logo

The logo is FMCI's trading logo which is based on a wireless communications icon in the colours of the Irish flag.

## Home

I used a similiar layout to the "Boutique Ado" tutorial with a the previously mentioned alteration to the color pallet.

<details><summary>Homepage Mockup</summary>

![Homepage Mockup](/static/readmeimg/home.png)</details>

## Store

Again the store is based on the same Django framework as used in the Boutique Ado tutorial.

<details><summary>Store Page Mockup</summary>

![Store Page Mockup](/static/readmeimg/store.png)</details>

## Other Offerings

This uses a clean look with a relevant photograph and a table listing the various options on offer.

<details><summary>Offerings Mockup</summary>

![Offerings Mockup](/static/readmeimg/other.png)</details>

---
---
&nbsp;

# User Experience & Testing

## User Stories

Each user story has its own Agile task. In this way the implementation and the testing is integrated as one. A task may have dependencies which must be in place in order for the current task to be completed. An example of this is shown here.

### Visitor Journey
  
<details><summary>As a visitor I can use a menu to view products and services</summary>

![Menu](/static/readmeimg/visitor/visitor-menu.png)
</details>


<details><summary>As a visitor I access the store so I can purchase products</summary>

![Store](/static/readmeimg/visitor/visitor-store.png)
</details>

<details><summary>As a visitor I can select wearable products and accessories</summary>

![Accessory](/static/readmeimg/visitor/visitor-accessory.png)
</details>

<details><summary>As a visitor I can select wearable products in different sizes</summary>

![Sizes](/static/readmeimg/visitor/visitor-sizes.png)
</details>

<details><summary>As a visitor I can modify my cart and add or remove products</summary>

![Modify](/static/readmeimg/visitor/visitor-modify.png)
</details>

<details><summary>As a visitor I can checkout and complete my product purchases</summary>

![Order](/static/readmeimg/visitor/visitor-order.png)
</details>

<details><summary>As a visitor I can see that my order is processing</summary>

![Stripe](/static/readmeimg/visitor/visitor-stripe.png)
</details>

<details><summary>As a visitor I can see that my order is successfull</summary>

![Success](/static/readmeimg/visitor/visitor-success.png)
</details>

<details><summary>As a visitor I receive an order confirmation email</summary>

![Order Email](/static/readmeimg/visitor/visitor-order-email.png)
</details>

<details><summary>As a visitor I can register so that I become a site user</summary>

![Register](/static/readmeimg/visitor/visitor-register.png)
</details>

<details><summary>As a visitor I will receive a registration verification link in an email</summary>

![Registration Email](/static/readmeimg/visitor/visitor-reg-confirm-email.png)
</details>

<details><summary>As a visitor I can click a registration verification link from an email</summary>

![Registration Confirm](/static/readmeimg/visitor/user-reg-confirm.png)
</details>

<details><summary>As a visitor I can get a registration acknowledgement alert</summary>

![Validation Acknowledgement](/static/readmeimg/visitor/visitor-reg-ack.png)
</details>

### User Journey

<details><summary>As a user I can log in to my account</summary>

![Login](/static/readmeimg/user/user-login.png)
</details>

<details><summary>As a user I can see my name when logged in</summary>

![Visibility](/static/readmeimg/user/user-visible.png)
</details>

<details><summary>As a user I can view my user profile</summary>

![Profile](/static/readmeimg/user/user-profile.png)
</details>

<details><summary>As a user I can modify my profile</summary>

![Update](/static/readmeimg/user/user-profile-update.png)
</details>

<details><summary>As a user I can view details of my orders</summary>

![Orders](/static/readmeimg/user/user-orders.png)
</details>

<details><summary>As a user I can view my past orders</summary>

![Single](/static/readmeimg/user/past-orders.png)
</details>

<details><summary>As a user I can log out of my account</summary>

![Logout](/static/readmeimg/user/user-logout.png)
</details>

<details><summary>As a user I can verify I've logged out of my account</summary>

![Logout Confirmation](/static/readmeimg/user/user-logout-success.png)
</details>


### Staff Journey


<details><summary>As a staff member I can manage store products</summary>

![Manage Store](/static/readmeimg/staff/staff-store.png)
</details>

<details><summary>As a staff member I can edit store products</summary>

![Edit Product](/static/readmeimg/staff/staff-edit.png)
</details>

<details><summary>As a staff member I can delete store products with confirmation warning</summary>

![Delete Product](/static/readmeimg/staff/staff-delete.png)
</details>


<details><summary>As a staff member I can add a new product</summary>

![Add Product](/static/readmeimg/staff/staff-add.png)
</details>

<details><summary>As a staff member I can view confirm product is added</summary>

![See New Product](/static/readmeimg/staff/staff-new-product.png)
</details>


---
---
&nbsp;

# Technologies

- [HTML5](https://en.wikipedia.org/wiki/HTML5): mark-up language.
- [CSS3](https://en.wikipedia.org/wiki/CSS): styling.
- [JavaScript](https://www.javascript.com/): programming language.
- [Python 3](https://www.python.org/): programming language.
- [Django 3.2](https://www.djangoproject.com/)
  - [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/): for forms.
  - [Crispy Bootstrap5](https://pypi.org/project/crispy-bootstrap5/): bootstrap5 template pack for crispy forms.
  - [Django Forms Dynamic](https://github.com/dabapps/django-forms-dynamic): for the dynamic form using HTMX.
  - [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/): for the dynamic form.
- [Bootstrap](https://getbootstrap.com/): styling.
- [Outlook](https://outlook.com/): for email testing.
- [Stripe](https://stripe.com/): for payments and webhooks.
- [Facebook](https://facebook.com/): For SEO.
- [AWS S3](https://aws.amazon.com/pm/serv-s3): store media files.
- [GitHub](https://github.com/): for host repository.
- Lighthouse from Chrome Developer Tools for performance testing
- [Codeanywhere](https://codeanywhere.com/): online IDE.
- [GitPod](https://www.gitpod.io/): online IDE.
- [Heroku](:<https://codeanywhere.com/):> PaaS deployment site
- [Google Fonts](https://fonts.google.com/): to import fonts.
- [Font Awesome](https://fontawesome.com/): to import icons.
- [Lucidchart](https://www.drawio.com/): for the mockups and ERM.
- [GIMP](https://www.gimp.org/): to create the logo and readme screens image

&nbsp;

---

# Deployment

## Deploy site using Heroku

Deployment pre-requisites:

- ### gunicorn

- ### dj_database_url

- ### dj3-cloudinary-storage

- ### psycopag2
  
## Deployment Procedure

- ### On the Heroku dashboard, select "New" and click "Create new app"

  - Create a unique app name which will be added to allowed hosts in the project settings
  - Select your region
  - Click "Create app"
  
- ### Go to the settings tab

  - Scroll down to the config vars section and select "Reveal Config Vars"
  - DATABASE_URL should be set to your selected database (Elephant SQL or similiar)
  - Add a new config var for SECRET_KEY - create your own or use a django secret key generator
  - Add a new config var for CLOUDINARY_URL and use the "API Environment variable" from your cloudinary dashboard
  - Add a new config var for DISABLE_COLLECTSTATIC with the value of 1 (!!! REMOVE PRIOR TO FINAL DEPLOYMENT !!!)
  
- ### Create environment variables for your app
  
  Create a new env.py file in the top level directory with the following lines

    ```python
    import os  
    os.environ["DATABASE_URL"] = "the database url you set in Heroku"  
    os.environ["SECRET_KEY"] = "your chosen secret key"  
    os.environ["CLOUDINARY_URL"] = "the api you used in Heroku  
    ```

  - If not already present, create a .gitignore file and add env.py to it ( before final deployment add any other files and folders you want to exclude from the deployed app)

- ### Add the following lines to settings.py in your app

    ```python
    import os
    import dj_database_url
    if os.path.isfile('env.py'):
    import env
    ```

- ### Replace the insecure secret key with "SECRET_KEY = os.environ.get('SECRET_KEY')"

- ### Link your database by commenting out old DATABASES section and add

    ```python
    DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    ```

- ### Add Heroku to the allowed hosts to ensure site loads

  ```python
  ALLOWED_HOSTS = ['example-heroku-app-name.herokuapp.com', 'localhost']
  ```

- ### Add 'cloudinary_storage' (above 'django.contrib.staticfiles') and 'cloudinary' (below) to INSTALLED_APPS

  ```python
  'cloudinary_storage',
  'django.contrib.staticfiles',
  'cloudinary',
  ```

- ### Setup Cloudinary to store static and media files

  ```python
    STATIC_URL = '/static/'
	STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
	STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
	STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
	MEDIA_URL = '/media/'
	DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
  ```

- ### Create a Procfile in the top level directory with the below

  ```text
  web: gunicorn project_name.wsgi
  ```

- ### Create a requirements file

    ```bash
    'pip3 freeze --local > requirements.txt' 
    ```

- ### Make any outstanding migrations

  ```bash
  python3 manage.py migrate
  ```

- ### Commit and push to GitHub

- ### ENSURE THE FOLLOWING PRIOR TO FINAL DEPLOYMENT
  
  - Set DEBUG = False in project settings.py
  - Remove DISABLE_COLLECTSTATIC config var from Heroku
  
- ### Go to the Deploy tab

  - Select GitHub and confirm connection to GitHub account
  - Search for the repository and click "Connect"
  - Scroll down to the deploy options
  - Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository
  - In manual deploy, select which branch to deploy and click "Deploy Branch"
  - Heroku will start building the app
- The link to the app can be found at the top of the page by clicking "Open app"

## Steps to clone site

- In the GitHub repository, click the "Code" button.
- Select "HTTPS" and copy the URL.
- Open Git Bash and navigate to the repository where you would like to locate the cloned repository.
- Type "git clone" followed by the copied URL.
- Press enter to create the clone.
- Install required packages with the command "pip3 install -r requirements.txt"

&nbsp;

---

# Credits

## Code

- The site is based on a modified version of [Code Institute's PP4](https://github.com/Code-Institute-Solutions/Django3blog)
- The code for the Map Page is supplied by [MapBox](https://www.mapbox.com/) and is freely availabe for customizing for your own projects. I've documented how I adapted it to this site [here](#notes)
- The code for user comments was adapted from [Code Institute's PP4 Masterclass](https://www.youtube.com/watch?v=YH--VobIA8c)
- The code for authentication was adapted from [Code Institute's PP4 Masterclass](https://www.youtube.com/watch?v=YH--VobIA8c) which I modified to use modals instead of full web pages
- Deployment procedure modified from [SJeCollins](https://github.com/SJECollins/ci-pp4-pet-rx/blob/main/README.md) excellent readme and also his test procedure document

&nbsp;

---

## Media

- The logo was created in Gimp
- Social media and google map location icons are from [Font Awesome](https://fontawesome.com)
- Roboto and Lato fonts are from [Google Fonts](https://fonts.google.com)
- [Lambbdatest](https://www.lambdatest.com/) was used todo initial layout tests and device screenshots to import into Gimp

- Background and placeholder images are from [pxfuel](https://www.pxfuel.com/) and [wallpapersafari](https://wallpapersafari.com/)
  
- Well Images from [County Clare Heritage Office](https://heritage.clareheritage.org/category/places/holy-wells) and [Galway Heritage Office](https://heritage.galwaycommunityheritage.org/):
  - Tobar Éanna taken by Paddy Crowe
  - Tobar Mochulla taken by James Feeney
  - Tobar Bhríde taken by James Feeney
  - Toba na nAingeal taken by Tony Kirby

&nbsp;

---

## Acknowledgement

Thanks to the following people who have supported me:

- My mentor Brian Macharia  
- Paul Thomas O'Riordan and Laura Maycock from CI  
- Cohort team lead Jonny Davison  
- My wife and family for putting up with me  
- All the slackers on Code Institue  

&nbsp;

---

