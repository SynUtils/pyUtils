# Build Images

# Build core
docker build -t u14_core -f u14_core .
docker build -t u12_core -f u12_core .
docker build -t c6_core -f c6_core .
docker build -t c7_core -f c7_core .


# Ubuntu 14 
docker build -t u14_py276 -f u14_py276 .
docker build -t u14_py35 -f u14_py35 .
docker build -t u14_py34 -f u14_py34 .
docker build -t u14_py269 -f u14_py269 .

# Ubuntu 12 
docker build -t u12_py273 -f u12_py273 .

# Centos 7
docker build -t c7_py275 -f c7_py275 .

# Centos 6 
docker build -t c6_py266 -f c6_py266 .