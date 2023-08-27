function xDot = dynamics(t,x,thetaDes,dist, K)
    
    %desired x
    xDes = thetaDes*[t 1 0];

    %Initialize xDot a column vector
    xDot = zeros(3,1);

    %system's gain/constant
    k = K(1);

    %controller's gain/constants
    kp = K(2);
    kd = K(3); 
    ki = K(4);

    %pid control law
    u = kp*(xDes(2) - x(2)) + kd*(xDes(3) - x(3)) + ki*(xDes(1) - x(1)) + dist*t^5;
    
    %system dynamics
    xDot(1) = x(2);
    xDot(2) = x(3);
    xDot(3) = k*u;
end