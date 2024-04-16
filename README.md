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

- [SEO & Marketing](#seo--marketing)
  - [SEO](#seo)
  - [Marketing](#marketing)
  - [Newsletter](#newsletter)

- [User Experience & Testing](#user-experience--testing)
  - [Agile Tracker](#agile)
  - [User Stories](#user-stories)
    - [Visitor Journey](#visitor-journey)
    - [User Journey](#user-journey)
    - [Staff Journey](#staff-journey)
  - [Stripe Payments](#stripe-payments-webhooks)
  - [Email Verification](#email-verification)
  - [Lighthouse Testing](#lighthouse-testing)

- [Technologies](#technologies)

- [Deployment](#deployment)
  - [Deploy site using Heroku](#deploy-site-using-heroku)
  - [Deployment Procedure](#deployment-procedure)
  - [Steps to clone site](#steps-to-clone-site)

- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgement](#acknowledgement)

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

# SEO & Marketing

## SEO

For the purposes of PP5 a facebook page is provided here [FMCI Store](https://www.facebook.com/people/FMCI-Store/61557020310153/)

<details><summary>Facebook Page Screenshot</summary>

![Facebook](/static/readmeimg/fbook.png)

</details>

### Relevant code from webpage

```html
<link rel="preconnect" href="https://region1.google-analytics.com">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-9988CFHBCY" defer></script>
<script defer>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-9988CFHBCY');
</script>

<meta name="google-site-verification" content="L33apRDqRtPi1I8nHWeQhXlwDacsbGytSjistzBgvfE" />
{% block meta %}
<meta http-equiv="X-UA-Compatible" content="ie=edge" />
<meta charset="utf-8" />
<meta
name="viewport"
content="width=device-width, initial-scale=1, shrink-to-fit=no"
/>
<meta name="robots" content="index, nofollow">
<meta name="keywords" content="FMCI, fmci, future,  mobility, campus">
<meta name="description" content="Storefront CI Project for FMCI">
```

## Marketing

### Online Platforms

LinkedIn would be the main vehicle for social media in order to target and engage the relevant audience and market. Instagram and Facebook would alo be utilised and a facebook page is provided cuurrently.

### Target Market

The target market is OEMs, new startups and automotive research organisations. 

### Goals of the business

As a platform for automotive research the goal is to provide merchandise online and at events to draw attention to FMCI and to increase awareness in the industry and in general.

### Similiar Businesses

In terms of FMCI's business offering there aren't many if any competing businesses. FMCI provides a bespoke automotive testing platform as a service to the automotive industry, OEMs and new startups. Some specific aspects of FMCIs services are provided by AWS, Google, Heroku, Connected Hubs, WeWork etc.


## Newsletter

Visitors and users can signup to a newsletter to receive news, developments and other relevant information.

<details><summary>Newsletter Screenshot</summary> 

![Newsletter Screenshot](/static/readmeimg/newsletter.png)
</details>

---
---
&nbsp;

# User Experience & Testing

## Agile

I used [GitPod Project](https://github.com/users/brianach/projects/8) to as my Agile tracker

## User Stories

There are three levels of user stories: visitor, user and staff. The stories are linked to agile tasks which can be seen below. Agile tasks cover one or more stpes on each of the user stories and journeys. Below we can see the agile tasks followed by the journey steps included in that task. The task view itself shows the code commits that were made to implement the task and a list of the steps completed. Below is an edited example of [Agile Task 42 - Add Checkout App](https://github.com/brianach/fmcistore/issues/42)

<details><summary>Edited Example</summary> 

![Example](/static/readmeimg/task-steps.png)
</details>

### Visitor Journey

[Agile Task 39 - Add Store App](https://github.com/brianach/fmcistore/issues/39)  
<details><summary>As a visitor I can use a menu to view products and services</summary>

![Menu](/static/readmeimg/visitor/visitor-menu.png)
</details>

<details><summary>As a visitor I access the store so I can purchase products </summary>

 
![Store](/static/readmeimg/visitor/visitor-store.png)
</details>


<details><summary>As a visitor I can select wearable products and accessories</summary>

![Accessory](/static/readmeimg/visitor/visitor-accessory.png)
</details>

 
<details><summary>As a visitor I can select wearable products in different sizes</summary>

![Sizes](/static/readmeimg/visitor/visitor-sizes.png)
</details>
&nbsp;

[Agile Task 34 - Add Cart App](https://github.com/brianach/fmcistore/issues/34)
<details><summary>As a visitor I can modify my cart and add or remove products</summary>

![Modify](/static/readmeimg/visitor/visitor-modify.png)
</details>
&nbsp;

[Agile Task 42 - Add Checkout App](https://github.com/brianach/fmcistore/issues/42)
<details><summary>As a visitor I can checkout and complete my product purchases</summary>

![Order](/static/readmeimg/visitor/visitor-order.png)
</details>

<details><summary>As a visitor I can see that my order is processing</summary>

![Stripe](/static/readmeimg/visitor/visitor-stripe.png)
</details>

<details><summary>As a visitor I can see that my order is successfull</summary>

![Success](/static/readmeimg/visitor/visitor-success.png)
</details>
&nbsp;

[Agile Task 51 - Add Email Functionality](https://github.com/brianach/fmcistore/issues/51)
<details><summary>As a visitor I receive an order confirmation email</summary>

![Order Email](/static/readmeimg/visitor/visitor-order-email.png)
</details>
&nbsp;

[Agile Task 48 - Add Profiles App](https://github.com/brianach/fmcistore/issues/48)
<details><summary>As a visitor I can register so that I become a site user</summary>

![Register](/static/readmeimg/visitor/visitor-register.png)
</details>

<details><summary>As a visitor I will receive a registration verification link in an email</summary>

![Registration Email](/static/readmeimg/visitor/visitor-reg-confirm-email.png)
</details>

<details><summary>As a visitor I can click a registration verification link from an email</summary>

![Registration Confirm](/static/readmeimg/visitor/user-reg-confirm.png)
</details>
&nbsp;

[Agile Task 50 - Add Toasts](https://github.com/brianach/fmcistore/issues/50)
<details><summary>As a visitor I can get a registration acknowledgement alert</summary>

![Validation Acknowledgement](/static/readmeimg/visitor/visitor-reg-ack.png)
</details>

### User Journey

[Agile Task 48 - Add Profiles App](https://github.com/brianach/fmcistore/issues/48)
<details><summary>As a user I can log in to my account</summary>

![Login](/static/readmeimg/user/user-login.png)
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
&nbsp;

[Agile Task 56 - Show Full Name on navbar when logged in](https://github.com/brianach/fmcistore/issues/56)
<details><summary>As a user I can see my name when logged in</summary>

![Visibility](/static/readmeimg/user/user-visible.png)
</details>
&nbsp;

[Agile Task 50 - Add Toasts](https://github.com/brianach/fmcistore/issues/50)

<details><summary>As a user I can verify I've logged out of my account</summary>

![Logout Confirmation](/static/readmeimg/user/user-logout-success.png)
</details>


### Staff Journey

[Agile Task 49 -Implement Store Management](https://github.com/brianach/fmcistore/issues/49)

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

## Stripe Payments Webhooks

Stripe is being used to complete purchases. In order to verify that payments are processed correctly Stripe's webhooks are utilised.

<details><summary>Sample Webhooks List</summary>

![Sample Webhooks List](/static/readmeimg/stripe-list.png)</details>

---

## Email Verification

Email is used to verify user registration and to confirm purchases for visitiors and users. 

### Registration Verification Email

<details><summary>Email Verification</summary>

![Email Verification](/static/readmeimg/visitor/visitor-reg-confirm-email.png)</details>

### Order Confirmation Email

<details><summary>Order Confirmation</summary>

![Order Confirmation](/static/readmeimg/visitor/visitor-order-email.png)</details>

---

## Code Testing

I used CI's linter (https://pep8ci.herokuapp.com/) to test all the python. In some cases there are "line too long" warnings but lines cannot alawys be split up easily.
- Example: content=f'Webhook received: event["type"]} | SUCCESS: Verified order already in database',

## Lighthouse Testing

The main pages used were tested using Google Dev Tools Lightouse

### Desktop Platform Testing

<details><summary>Home Page</summary>

![Home](/static/readmeimg/performance/desktop-home-perf.png)</details>

<details><summary>Store Page</summary>

![Store](/static/readmeimg/performance/desktop-store-perf.png)</details>

<details><summary>Product Page</summary>

![Product](/static/readmeimg/performance/desktop-product-perf.png)</details>

<details><summary>Cart</summary>

![Cart](/static/readmeimg/performance/desktop-cart-perf.png)</details>

<details><summary>Checkout</summary>

![Checkout](/static/readmeimg/performance/desktop-till-perf.png)</details>

### Mobile Platform Testing

<details><summary>Home Page</summary>

![Home](/static/readmeimg/performance/mobile-home-perf.png)</details>

<details><summary>Store Page</summary>

![Store](/static/readmeimg/performance/mobile-store-perf.png)</details>

<details><summary>Product Page</summary>

![Product](/static/readmeimg/performance/mobile-product-perf.png)</details>

<details><summary>Cart</summary>

![Cart](/static/readmeimg/performance/mobile-cart-perf.png)</details>

<details><summary>Checkout</summary>

![Checkout](/static/readmeimg/performance/mobile-till-perf.png)</details>


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
- [Heroku](https://codeanywhere.com/): PaaS deployment site
- [Google Fonts](https://fonts.google.com/): to import fonts.
- [Font Awesome](https://fontawesome.com/): to import icons.
- [Lucidchart](https://www.drawio.com/): for the mockups and ERM.
- [GIMP](https://www.gimp.org/): to create the logo and readme screens image
- [Issues](https://github.com/brianach/fmcistore/issues): agile project management 

&nbsp;

---

# Deployment

## Deploy site using Heroku
  
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
  - Add AWS config variables if used
  - Add Stripe Payments variabls if used
  
- ### Create environment variables for your app


  - If not already present, create a .gitignore file and add env.py to it ( before final deployment add any other files and folders you want to exclude from the deployed app)

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

- The site is based on a modified version of [Code Institute's PP5](https://github.com/Code-Institute-Solutions/Boutique-Ado)
- Deployment procedure modified from [SJeCollins](https://github.com/SJECollins/ci-pp4-pet-rx/blob/main/README.md) excellent readme and also his test procedure document

&nbsp;

---

## Media

- The logo is FMCI's current logo
- Social media and google map location icons are from [Font Awesome](https://fontawesome.com)
- Fonts are from [Google Fonts](https://fonts.google.com)
- Product images are stock images with FMCI logo appeded using GIMP [GIMP](https://www.gimp.org/)
  

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

