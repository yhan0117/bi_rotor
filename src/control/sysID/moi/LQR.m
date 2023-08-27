A = [0 1 0
     0 0 1
     0 0 0];
B = [0 0 0.5356]';

C = [0 1 0
     0 0 1];

con = ctrb(A,B);
uncon = length(A) - rank(con);

obs = obsv(A,C);
unobs = length(A) - rank(obs);

Q = diag([0.1 5 0.01]);
R = 0.001;
G = lqr(A,B,Q,R)

save('LQR.mat','G')
