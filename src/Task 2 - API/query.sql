SELECT * FROM Shop.Products;
Query2
Query3
Query4
Query5
select Name, Price, count(Transactions.Type) as charge from Products join Transactions on Products.Name = Transactions.Products_Name where Transactions.Type = "bought" group by Name order by charge desc;