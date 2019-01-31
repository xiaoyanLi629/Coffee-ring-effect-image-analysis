Data <- read.csv("/Users/xiaoyanli/Desktop/Image_analysis_8_7_2018/Report folder/CaCl2_MgCl2_NaCl_image analysis_results/total_properties_095_6.csv")
X = Data[, 6]
X1 = X[1:5]
X2 = X[6:10]
X3 = X[11:15]
par(mfrow = c(2, 2))
par(mar = c(7, 7, 3, 3))
boxplot(X1, X2, X3, names=c("high","medium","low"), xlab="Sample group", ylab="Average area of particles", cex.lab=1, cex.axis=1, cex.main=2, cex.sub=11)
title(sub = 'Subfigure 1')

Data <- read.csv("/Users/xiaoyanli/Desktop/Image_analysis_8_7_2018/Report folder/CaCl2_MgCl2_NaHCO3 image analysis/total_properties_089_11.csv")
X = Data[, 4]
X1 = X[1:5]
X2 = X[6:10]
X3 = X[11:15]
boxplot(X1, X2, X3, names=c("high","medium","low"), xlab=expression('Sample group'), ylab="Number of particles", cex.lab=1, cex.axis=1, cex.main=1, cex.sub=1)
title(sub = 'Subfigure 2')

Data <- read.csv("/users/xiaoyanli/Desktop/Image_analysis_8_7_2018/Report folder/Na2SO4_CaSO4_MgSO4 image analysis/total_properties_0.86_4.csv")
X = Data[, 7]
X1 = X[1:5]
X2 = X[6:10]
X3 = X[11:15]
boxplot(X1, X2, X3, names=c("high","medium","low"), xlab=expression('Sample group'), ylab="Total area of particles", cex.lab=1, cex.axis=1, cex.main=1, cex.sub=1)
title(sub = 'Subfigure 3')

Data <- read.csv("/users/xiaoyanli/Desktop/Image_analysis_8_7_2018/Report folder/NaHCO3_CaSO4_MgSO4 image analysis/total_properties_0.93_6.csv")
X = Data[, 4]
X1 = X[1:5]
X2 = X[6:10]
X3 = X[11:15]
boxplot(X1, X2, X3, names=c("high","medium","low"), xlab=expression('Sample group'), ylab="Number of particles", cex.lab=1, cex.axis=1, cex.main=1, cex.sub=1)
title(sub = 'Subfigure 4')

#mtext("Boxplot for four experiments", outer = TRUE, side = 3, cex = 1.2, line = 1)
#mtext("Title for Two Plots", outer = TRUE, cex = 1.5)


