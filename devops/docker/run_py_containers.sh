# run.sh will launch python docker containers in one go

# Ubuntu 14 
docker run -itdp 14276:22 u14_py276
docker run -itdp 1435:22 u14_py35
docker run -itdp 1434:22 u14_py34
docker run -itdp 14269:22 u14_py269

# Ubuntu 12 
docker run -itdp 12273:22 u12_py273

# Centos 7
docker run -itdp 7275:22 c7_py275

# Centos 6 
docker run -itdp 6266:22 c6_py266






