clear;clc;clf
load("motor.mat")

avgx = [CW1(:,4); CW2(:,4)];
avgy = [CW1(:,2); CW2(:,2)];
p = polyfit(avgx, avgy, 2)
t = linspace(0, 18000, 1000);
% hold on
% plot(CW1(:,4), CW1(:,2))
plot(t, polyval(p, t))

avgx = [CCW1(:,4); CCW2(:,4)];
avgy = [CCW1(:,2); CCW2(:,2)];

p = polyfit(avgx, avgy, 2)
% t = linspace(0, 18000, 1000);
hold on
% plot(CCW1(:,4), CCW1(:,2))
plot(t, polyval(p, t))

%%