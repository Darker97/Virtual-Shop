#### Security Service
The Security Service has multiple tasks to solve. On the one hand it will provide all necessary functions to make sure that the user only gets the information he is allowed to, and will check all the given requests to the API for standart attacks, such as an SQL injection. The Security Service is seperated in two parts, the authentication Service and the parts in the API.

##### Injection Attacks
A known thread for a database is an SQL Injection. This means that the user is able to insert code into the given query and to collect more data than he is allowed to. If an SQL injection is possible, the attacker can get access to all data that is stored in the database or, in the worst case scenario can even alter it.
To counter this attack, our security function should scan every incoming request and check it for commands. This won't counter all SQL Attacks, but should get rid of the most obvious ones.

##### WhoAmI and WhoAreYou?
To make sure only the right Person can access the right data, we wil implement a small password checker. 

The system will get a hashed password and username from the webpage and then check the password with the database. If the information check our, the API will send a cookie with a tooken back, which will then be stored in the cache of the browser. 

The cookie itself contains information like user and timestamp which will then be signed by our private key and encrypted by our public key. 

If the user is now accessing data, he sends the coockie to the API with the request, which then gets checked with the database. The Authentication Service will then check the signature and the stored data. 

We will also implement a permission system so we can track what a person can do and what not. For Employes we will create specific rules, which can do more or less things. (For Example, Technician, Sales Person)

In the case that the given data is wrong at any point of the function, the API will answer with an Error and an Error Code. The client will then react to the given answer. 