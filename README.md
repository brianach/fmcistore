# FMCI Store

![FMCI logo](media/logo.png)

[FMCI Store](https://fmcistore-366e47ff9414.herokuapp.com/) gives interested users and visitors the opportunity to buy FMCI merchandice as well as the ability to view facilities and services on offer to businesses and automotive product developers.Visitors have access to all the available information.

Registered users can access records of previous purchases in their profile. Staff users can edit existing products and alos add or delete products as necessary. Staff users can also view and edit orders as may be required at the request of customers.

Wearable merchandice can be ordered in various sizes where available.

![FMCI Store](/media/screens.png)

# Table of Contents

- [FMCI Store](#wells)
- [Table of Contents](#table-of-contents)
- [Features](#features)
  - [Home Page](#home-page)
  - [Authentication](#authentication)
- [Design](#design)
  - [Database Model](#database-model)
  - [General Color Scheme](#general-color-scheme)
  - [Logo](#logo)
  - [Home](#home)
  - [User Authentication](#user-authentication)
- [User Experience](#user-experience)
- [Testing](#testing)
  - [User Stories](#user-stories)
  - [Desktop](#desktop)
      - [Content Page](#content-page)
    - [Authentication](#authentication-1)
  - [Tablet](#tablet)
      - [Content Page](#content-page-1)
    - [Authentication](#authentication-2)
  - [Mobile](#mobile)
      - [Content Page](#content-page-2)
    - [Authentication](#authentication-3)
  - [Map Interaction](#map-interaction)
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

# Features

## Home Page

The home page contains a summary of what FMCI does preceded by a link to the main FMCI homepage. A scrolling carousel runs at the bottom of the page which displays a clickable logo for each of FMCI's partners which when clicked open the partner's home page on a separate tab. The carousel is loaded from a simple django database model which can be edited by a superuser via the admin page.


## Authentication

Users can register an account which gives them the ability to see their order history. Logged in users will see their full name displayed as dropdown link at the top of the navbar from where they can see a link to their profile, or to logout.

---

# Design

## Database Model

The FMCI databases utilizes a number of models with relationships as shown in the following diagram. 

<details>
<summary>ERM</summary>

![ERM](/static/readmeimg/erm.png)

</details>

There are five categories of goods and services of which only goods may be purchased online. The Spaces and Services are purchases by emailing or by tenant customers only availabe on site.

## General Color Scheme

I based the color scheme on the main [FMCI](https://futuremobilityireland.ie/) webpage. Font colours were chosen to make the best use of contrast in order to assist with visbility and clarity.

<details>
<summary>Color Scheme</summary>

![Color Scheme](/static/readmeimg/colors.png)

</details>

## Logo

The logo is FMCI's tradin logo which is based on a wireless communications icon in the colours of the Irish flag.

## Home

I used a similiar layout to the "Boutique Ado" tutorial with a the previously mentioned alteration to the color pallet.

<details>

<summary>Homepage Mockup</summary>

![Homepage Mockup](/static/readmeimg/home.png)

</details>

<details>

<summary>Store Page Mockup</summary>

![Store Page Mockup](/static/readmeimg/store.png)

</details>


---

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

![Accessory](/static/readmeimg/visitor/visitor-sizes.png)
</details>

<details><summary>As a visitor I can modify my cart and add or remove products</summary>

![Accessory](/static/readmeimg/visitor/visitor-modify.png)
</details>

<details><summary>As a visitor I can checkout and complete my product purchases</summary>

![Accessory](/static/readmeimg/visitor/visitor-order.png)
</details>

<details><summary>As a visitor I can see that my order is processing</summary>

![Accessory](/static/readmeimg/visitor/visitor-stripe.png)
</details>

<details><summary>As a visitor I can see that my order is successfull</summary>

![Accessory](/static/readmeimg/visitor/visitor-success.png)
</details>

<details><summary>As a visitor I receive an order confirmation email</summary>

![Accessory](/static/readmeimg/visitor/visitor-order-email.png)
</details>

<details><summary>As a visitor I can register so that I become a site user</summary>

![Accessory](/static/readmeimg/visitor/visitor-register.png)
</details>

<details><summary>As a visitor I will receive a registration verification link in an email</summary>

![Accessory](/static/readmeimg/visitor/visitor-reg-confirm-email.png)
</details>

<details><summary>As a visitor I can click a registration verification link from an email</summary>

![Accessory](/static/readmeimg/visitor/user-reg-confirm.png)
</details>

<details><summary>As a visitor I can get a registration acknowledgement alert</summary>

![Accessory](/static/readmeimg/visitor/visitor-reg-ack.png)
</details>

### User Journey

<details><summary>As a user I can log in to my account</summary>

![Accessory](/static/readmeimg/user/user-login.png)
</details>

<details><summary>As a user I can see my name when logged in</summary>

![Accessory](/static/readmeimg/user/user-visible.png)
</details>

<details><summary>As a user I can view my user profile</summary>

![Accessory](/static/readmeimg/user/user-profile.png)
</details>

<details><summary>As a user I can modify my profile</summary>

![Accessory](/static/readmeimg/user/user-profile-update.png)
</details>

<details><summary>As a user I can view details of my orders</summary>

![Accessory](/static/readmeimg/user/user-orders.png)
</details>

<details><summary>As a user I can view my past orders</summary>

![Accessory](/static/readmeimg/user/past-orders.png)
</details>

<details><summary>As a user I can log out of my account</summary>

![Accessory](/static/readmeimg/user/user-logout.png)
</details>

### Authentication

<details>
<summary>Login Modal</summary>

![Home](media/mob/login-mob.png)

</details>

<details>
<summary>Logout Modal</summary>

![Home](media/mob/logout-mob.png)

</details>

<details>
<summary>Register Modal</summary>

![Home](media/mob/reg-mob.png)

</details>

&nbsp;

## Map Interaction

The map, with its markers indicating the locations of the wells, is really the main event in this application. The map itself uses [mapbox gl](https://www.mapbox.com/) and there are explanatory [notes](#notes) at the end of this document detailing how it(mapbbox), python and javascript all hangs together. The marker popup works in the same way on all devices and consists of three elements, Popup Title, Excerpt and a Google Maps Link to the loction.
<details>
<summary>Popup Title</summary>

![Home](media/lap/popup-lnk1.png)

</details>

The popup title becomes an active link when there is a related content record in the database. Otherwise it is a plain heading when there is not. You can see the link to the post content appear in the bottom right of the screen in the Popup Title screenshot.

<details>
<summary>Google Map Link</summary>

![Home](media/lap/popup-lnk2.png)

</details>

By clicking on the <span style="color: rgb(168, 109, 0);">*'open location in google maps'*</span> button, a new google maps page opens with the location set as a destination allowing the user to click on the *'Directions'* link to navigate to the lcoation.

<details>
<summary>Google Map Window</summary>

![Home](media/lap/gmap.png)

</details>

&nbsp;

---

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
  - [Coverage](https://github.com/nedbat/coveragepy/tree/6.5.0): for measuring code coverage of Python tests.

- [Bootstrap](https://getbootstrap.com/): styling.
- [Cloudinary](https://cloudinary.com/): store static and media files.
- [GIT](https://git-scm.com/): for version control.
- [GitHub](https://github.com/): for host repository.
- Lighthouse from Chrome Developer Tools for performance testing
- [Codeanywhere](https://codeanywhere.com/): online IDE.
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

