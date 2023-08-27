close all
g = 9.806;
hold on
grid on 
plot(CW1(:,4), CW1(:,2)*g, ":")
plot(CW2(:,4), CW2(:,2)*g, ":")

avgx = [CW1(:,4); CW2(:,4)];
avgy = g*[CW1(:,2); CW2(:,2)];
[p, S] = polyfit(avgx,avgy,2);
R2 =  1 - S.normr^2 / norm(avgy-mean(avgy))^2;

t = linspace(0, 18000, 500);
plot(t, polyval(p,t), "LineWidth", 1);

title(sprintf('Thrust vs Motor Speed \n Propeller 1, Clockwise, $R^{2}$ = %0.3f', R2), 'Interpreter', 'Latex');
xlabel('motor speed [rpm]', 'Interpreter', 'Latex')
ylabel('thrust [N]', 'Interpreter', 'Latex')
legend("Trial 1", "Trial 2", "Best fit polynomial of order 2", 'Location','northwest')
ylim([0 9])

set(gcf,'Position',[800 600 600 420])
exportgraphics(gcf, "CW.jpg")
%%
clf
hold on
grid on
plot(CCW1(:,4), CCW1(:,2)*g, ":")
plot(CCW2(:,4), CCW2(:,2)*g, ":")
avgx = [CW1(:,4); CW2(:,4); CCW1(:,4); CCW2(:,4)];
avgy = g*[CW1(:,2); CW2(:,2); CCW1(:,2); CCW2(:,2)];
[p, S] = polyfit(avgx,avgy,2);
R2 =  1 - S.normr^2 / norm(avgy-mean(avgy))^2;

t = linspace(0, 18000, 500);
plot(t, polyval(p,t), "LineWidth", 1);

title(sprintf('Thrust vs Motor Speed \n Propeller 2, Counter-Clockwise, $R^{2}$ = %0.3f', R2), 'Interpreter', 'Latex');
xlabel('motor speed [rpm]', 'Interpreter', 'Latex')
ylabel('thrust [N]', 'Interpreter', 'Latex')
legend("Trial 1", "Trial 2", "Best fit polynomial of order 2", 'Location','northwest')
ylim([0 9])

set(gcf,'Position',[800 600 600 420])
exportgraphics(gcf, "CCW.jpg")
%%
clf
hold on
grid on
plot(CW1(:,4), CW1(:,3), ":")
plot(CW2(:,4), CW2(:,3), ":")
avgx = [CW1(:,4); CW2(:,4)];
avgy = [CW1(:,3); CW2(:,3)];
[p, S] = polyfit(avgx,avgy,2)
R2 =  1 - S.normr^2 / norm(avgy-mean(avgy))^2;

t = linspace(0, 18000, 500);
plot(t, polyval(p,t), "LineWidth", 1);

title(sprintf('Torque vs Motor Speed \n Propeller 1, Clockwise, $R^{2}$ = %0.3f', R2), 'Interpreter', 'Latex');
xlabel('motor speed [rpm]', 'Interpreter', 'Latex')
ylabel('torque [Nm]', 'Interpreter', 'Latex')
legend("Trial 1", "Trial 2", "Best fit polynomial of order 2", 'Location','northeast')

set(gcf,'Position',[800 600 600 420])
exportgraphics(gcf, "CWTorque.jpg")

%%
% clf
hold on
grid on
plot(CCW1(:,4), CCW1(:,3), ":")
plot(CCW2(:,4), CCW2(:,3), ":")
avgx = [CCW1(:,4); CCW2(:,4)];
avgy = [CCW1(:,3); CCW2(:,3)];
[p, S] = polyfit(avgx,avgy,2)
R2 =  1 - S.normr^2 / norm(avgy-mean(avgy))^2;

t = linspace(0, 18000, 500);
plot(t, polyval(p,t), "LineWidth", 1);

title(sprintf('Torque vs Motor Speed \n Propeller 2, Counter-Clockwise, $R^{2}$ = %0.3f', R2), 'Interpreter', 'Latex');
xlabel('motor speed [rpm]', 'Interpreter', 'Latex')
ylabel('torque [Nm]', 'Interpreter', 'Latex')
legend("Trial 1", "Trial 2", "Best fit polynomial of order 2", 'Location','northwest')

set(gcf,'Position',[800 600 600 420])
exportgraphics(gcf, "CCWTorque.jpg")
