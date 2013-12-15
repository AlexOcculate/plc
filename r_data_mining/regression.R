

toyota <- read.csv("/Users/mattstringer/research/plc/r_data_mining/ToyotaCorolla.csv")

v1=rep(1,length(toyota$FuelType))
v2=rep(0,length(toyota$FuelType))

toyota$FuelType1=ifelse(toyota$FuelType=="CNG",v1,v2)
toyota$FuelType2=ifelse(toyota$FuelType=="Diesel",v1,v2)