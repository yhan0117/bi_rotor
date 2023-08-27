clear;clc;close all
T = readmatrix("P0.5(2).csv");
L = size(T,1);

for i = 1:L
    T(i,3) = (T(i,2) - T(1,2))/1000; 
end
for i = 1:L-1
    DT(i) = T(i+1,3) - T(i,3); 
end
Ts = mean(DT);
plot(T(:,3), T(:,1))
Y = fft(T(:,1));
P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = 1/Ts*(0:(L/2))/L;
plot(f,P1) 

[mag, i] = max(P1);
FF = f(i);
TT = 1/FF;

save('Period.mat','TT')