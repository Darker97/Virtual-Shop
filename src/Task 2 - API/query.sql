SELECT * FROM Shop.Products;
select Products_Name, Rating, Body, Customers.Name from Shop.Comments join Shop.Customers on Comments.Customers_ID = Customers.ID;
Query3
Query4
Query5
select Name, Price, count(Transactions.Type) as charge from Products join Transactions on Products.Name = Transactions.Products_Name where Transactions.Type = "bought" group by Name order by charge desc;
select Name, sum(Rating) as Score from Products join Comments on Products.Name = Comments.Products_Name group by Name order by Score desc;
select bought.Name, (chargeBought - chargeDelivered) as charge from ( select Name, count(Transactions.Type) as chargeBought from Products join Transactions on Products.Name = Transactions.Products_Name where Transactions.Type = "bought" group by Name ) as bought join ( select Name, count(Transactions.Type) as chargeDelivered from Products join Transactions on Products.Name = Transactions.Products_Name where Transactions.Type = "delivered" group by Name ) as delivered on bought.Name = delivered.Name; 
select Name, count(Rating) as charge from Products join Comments on Products.Name = Comments.Products_Name group by Name order by charge desc;
select Name, count(Comments.ID) as charge from Customers join Comments on Customers.ID = Comments.Customers_ID group by Name order by charge desc;
create view bought as select Name, Price, count(Transactions.Type) as charge from Products join Transactions on Products.Name = Transactions.Products_Name where Transactions.Type = "bought" group by Name order by charge desc; select Name, (Price * charge) as Revenue from bought order by Revenue desc; drop view bought;
create view bought as select Name, Price, count(Transactions.Type) as charge from Products join Transactions on Products.Name = Transactions.Products_Name where Transactions.Type = "bought" group by Name order by charge desc; select sum(Price * charge) as Revenue from bought order by Revenue desc; drop view bought;