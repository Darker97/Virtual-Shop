# Assignment 3 - Project Idea

## Group:

| Team        | ID           | 
| :------------- |:-------------:|
| Christian Baltzer|19970210-T453|
| Carolin Brückmann|19980317-T306|


## The Problem
For our Project Idea, we want to solve the chaos Problem of a shop. 
Most shops rely on paperwork to keep track of their storage. This method is slow and vulnerable to mistakes. 

## The Solution

We want to enhance the situation by introducing our storage managment system. This system includes a database in which all products of the shop are listed, aswell as all transactions the shop did with it's clients and suppliers.
The Shop will also have a Webservice, in which the customers can see what is available, and the shop owners can see all information they need to manage their Shop.
The webservice gets its Data from a rest API. This API Client is also analyzing the data on its own. 

## Main users
The main users will be customers, the employees and the managment of the shop. Everyone has their own Website, where they can see usefull information.

For instance, the managment has no insight in the products itself but in the business figures, like amount of sold items or amount of ordered items.

## Main features 
The main feature of our System, is the simplicity it brings. There is no need for manuell accounting to keep track of anymore or for long searches in the storehouse. With our System, the shop owner and his employees get an overview over the shops storage and the shops activities.


<!--Main features of the application are being able to sign in if you are an employee. If you are an employee you should be able to access data on other employees, the products, the suppliers and the different stores. It should be possible to analyse the data. For example who is the employee of the month? Which store sold the most products last week? And which product is the bestseller? Which supplier was the most reliable in the past? And how frequent buy customers at our stores? 
If you are a customer it should be possible to get information on availability of certain products as well as more detailed information on certain products. This could include prices, location and charateristics e.g. color. 
-->

## Technical Details
We are planing to build the System in a Kubernetes Kluster. The system is therefore easily scalabel and redundant. 
The parts themself will work inside of Docker Containers.

### The Structure
Our System will have multiple parts:

#### The main Database
Our main DB is there to hold all the data. It will be based on MySQL.

#### The Rest API and the Analyzer
Between the Website and the DB, we will have an Analyzer with a REST API. This one will analyze the given Data and give out the Results.

#### The Website
The Website is grabbing its Informations from the API and will then present them to the User. 
There will be multiple sites, one for each User group.

#### "The Randomizers" - our virtual People
To bring the whole System to life we need Interaction. Sadly we can't use a real shop or real employes, which is why we use little Python scripts, that will randomly insert data into the DB. There will also be randomizers that represent customers which buy products. 

