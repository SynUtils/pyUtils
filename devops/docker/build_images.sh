# Build Images

# Build core
docker build -t u14_core -f u14_core .
echo "u14_core image has built-----------------------------"

docker build -t u12_core -f u12_core .
echo "u12_core image has built-----------------------------"

docker build -t c6_core -f c6_core .
echo "c6_core image has built-----------------------------"

docker build -t c7_core -f c7_core .
echo "c7_core image has built-----------------------------"

echo "Hurray! Done with core images-----------------------------"

# Ubuntu 14 Python
docker build -t u14_py276 -f u14_py276 .
docker build -t u14_py35 -f u14_py35 .
docker build -t u14_py34 -f u14_py34 .
docker build -t u14_py269 -f u14_py269 .
echo "Hurray! Done with ubuntu14 Python images-----------------------------"

# Ubuntu 14 PHP
docker build -t u14_php5514 -f u14_php5514 .
echo "Hurray! Done with ubuntu14 PHP images-----------------------------"


# Ubuntu 12 
docker build -t u12_py273 -f u12_py273 .
echo "Hurray! Done with ubuntu12 Python images-----------------------------"


# Centos 7 Python
docker build -t c7_py275 -f c7_py275 .
echo "Hurray! Done with Centos7 Python images-----------------------------"

# Centos 7 PHP
docker build -t c7_php5514 -f c7_php5514 .
echo "Hurray! Done with Centos7 PHP images-----------------------------"

# Centos 6 Python
docker build -t c6_py266 -f c6_py266 .
echo "Hurray! Done with Centos6 Python images-----------------------------"
