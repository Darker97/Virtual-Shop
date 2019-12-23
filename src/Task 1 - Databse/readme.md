# TableCreater
The Tablecreater connects to the Mysql Database and executes the Querys, in our case, the create for the tables.

The Query.sql file holds all querys to be executed, one query per line. All lines will be executed.

The Setup.config holds the data to connect to the DB, in the following schema:
```
{
    URL
    Port
    Username
    Password
    Table
}
```