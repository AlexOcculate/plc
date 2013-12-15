
library(lattice)

oj <- read.csv("/Users/mattstringer/research/plc/r_data_mining/oj.csv")
oj$store <- factor(oj$store)
oj[1:2,]


t1=tapply(oj$logmove,oj$brand,FUN=mean,na.rm=TRUE)

t2=tapply(oj$logmove,INDEX=list(oj$brand,oj$week),FUN=mean,na.rm=TRUE)

plot(t2[1,],type= "l",xlab="week",ylab="dominicks",ylim=c(7,12))
plot(t2[2,],type= "l",xlab="week",ylab="miniute_maid",ylim=c(7,12))
plot(t2[3,],type= "l",xlab="week",ylab="miniute_maid",ylim=c(7,12))


logmove=c(t2[1,],t2[2,],t2[3,])
week1=c(40:160)
week=c(week1,week1,week1)
brand1=rep(1,121)
brand2=rep(2,121)
brand3=rep(3,121)
brand=c(brand1,brand2,brand3)



xyplot(logmove~week|factor(brand),type= "l",layout=c(1,3)

boxplot(logmove~brand,data=oj)
histogram(~logmove|brand,data=oj,layout=c(1,3))
densityplot(~logmove|brand,data=oj,layout=c(1,3),plot.points=FALSE)


oj1=oj[oj$store == 5,]
xyplot(logmove~week|brand,data=oj1,type="l",layout=c(1,3),col="black")