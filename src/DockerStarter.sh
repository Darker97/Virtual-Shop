git pull

cd Task\ 1\ -\ Databse
cd TableCreate
docker build -t tablescreater:0.1 .

echo "------------------------------------------------------------------------------"



cd ../../
cd Task\ 2\ -\ API
docker build -t apiservice:0.1 .
echo "------------------------------------------------------------------------------"


cd ../
cd Task\ 2.1\ -\ Authentication\ Service/
docker build -t securityservice:0.1 .
echo "------------------------------------------------------------------------------"


cd ../
cd Task\ 3\ -\ Customer/
docker build -t helpercustomer:0.1 .
echo "------------------------------------------------------------------------------"


cd ../
cd Task\ 4\ -\ Deliverer/
docker build -t helperdeliverer:0.1 .
echo "------------------------------------------------------------------------------"


cd ../
cd Task\ 5\ -\ Employer/
docker build -t helperemployer:0.1 .
echo "------------------------------------------------------------------------------"


cd ../
cd Task\ 7\ -\ Standart\ Seite/
docker build -t standartwebpage:0.1 .
echo "------------------------------------------------------------------------------"


cd ../
cd Task\ 9\ -\ Website\ Managment/
docker build -t adminwebpage:0.1 .
echo "------------------------------------------------------------------------------"
echo "Finished"


cd ../
cd Task\ 99\ -\ Docker/
docker-compose up