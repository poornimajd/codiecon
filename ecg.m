clc;close all;clear all;
a=arduino('com6','uno')
b=zeros(1,1000);
for i=1:1000
  b(i) =readVoltage(a,'A2')*1023/5
end
j=1:1000;
plot(j,b)
csvwrite('ecg_arduino_values_new1.csv',b);