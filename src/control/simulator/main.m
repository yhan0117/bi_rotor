clc;clear;close all
%kd, ki, kp
load("MOI.mat")
% load("LQR.mat")


Kp = 0.6;
Kd = 0.22; %0.22281692032865351726852652442282 is critically damped when kp = 0.5
Ki = 0.05;
kp = Kp*180/pi; 
kd = Kd*180/pi; 
ki = Ki*180/pi; 

k = 2*km*O*L/J;

% ki = G(1);
% kp = G(2);
% kd = G(3);

%states - [integralTheta theta thetaDot] %theta in degrees

gains = [k kp kd ki];
tspan = [0 10];
thetaDes = 0; %degrees
initialState = [0 30 0]; 
dist = 0;

[t,x] = ode45(@(t,x)dynamics(t,x,thetaDes,dist, gains), tspan, initialState); 
figure()
hold on
grid on

title("Simulation Results of Using PID Controller on the Bi-rotor Device", Interpreter="latex")
xlabel("time [s]", Interpreter="latex")
ylabel("angle [$^\circ$]", Interpreter="latex")
plot(t,x(:,2))
ylim([-25 45])
set(gcf,'Position',[800 600 600 420])
exportgraphics(gcf, "PID.jpg")
% 
% wn = sqrt(k*kp)
% zeta = k*kd/wn/2

