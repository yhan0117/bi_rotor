%%
%measured
load("Period.mat")

clear;
clc;
T = 1.8;
w = 2*pi/T;
P = w^2;

kp = 0.5*180/pi;

%
km = 0.0000040990;
O = 300;
L = 25/100;

syms moi

moi1 = double(vpa(solve(P == kp*2*km*O*L/moi)));

%calc
m = 28/1000;
J = 168607.35 / 10^9;
J = J + 2*m*(L/2)^2;
J = J*1.1;
save('MOI.mat','J', 'km', 'O', 'L')
