library(lattice)
library(nutshell)
data(births2006.smpl)

births2006.smpl[1:5,]

# What does dim do?
dim(births2006.smpl)

# find number of births by days of the week
births.dow=table(births2006.smpl$DOB_WK)
births.dow


barchart(births.dow,ylab="Day of Week",col="black")

dob.dm.tbl=table(WK=births2006.smpl$DOB_WK, MM=births2006.smpl$DMETH_REC) 

dob.dm.tbl

dob.dm.tbl=dob.dm.tbl[,-2] 
dob.dm.tbl


trellis.device()
barchart(dob.dm.tbl,ylab="Day of Week") 
barchart(dob.dm.tbl,horizontal=FALSE,groups=FALSE, xlab="Day of Week",col="black")

# birth weights for the number of number offsprings
histogram(~DBWT|DPLURAL,data=births2006.smpl,layout=c(1,5), col="black")
histogram(~DBWT|DMETH_REC,data=births2006.smpl,layout=c(1,3), col="black")

histogram(~DBWT|DPLURAL,data=births2006.smpl,layout=c(1,5), col="black")

# same as above, but as a density plot
densityplot(~DBWT|DPLURAL,data=births2006.smpl,layout=c(1,5), col="black")
