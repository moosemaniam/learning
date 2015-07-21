#
# @file nonUniformQuant.m
# @brief
# @author VikasMK
# @version 1.0
# @date 2015-07-16


x = 0:0.01:1;
#power law
p=0.75;
cpower = x.^p;
##ulaw
u=50;
culaw=log10(1+u.*x)/log10(1+u);
##Alaw
#A = 10;
#
#cAlaw= A*x/(1+log(A .* x[0:(1/A)]))
##cAlaw[end:] = (1 + log(A * x))/(1+log(A))
subplot(3,1,1);
plot(x,cpower);

subplot(3,1,2);
plot(x,culaw);
