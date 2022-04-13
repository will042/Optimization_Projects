A = 2;
B = 1;


delta = 0.0001;
delta_z = 1;

x1 = A;
i = 0;

x2 = @(x1) 1/(A+x1)-B

z = @(x1,x2) norm([x1, x2], 1)

data.x1 = [x1];
data.x2 = [x2(x1)];
data.delta_z = [0];
data.z = [z(x1, x2(x1))];


z_current = z(x1, x2(x1));

z_plus = z(x1+delta, x2(x1+delta));

z_minus = z(x1-delta, x2(x1-delta));

if z_plus < z_minus
    delta = delta;
else
    delta = -delta;
end



while delta_z >= 0 && i<10000000

    z_current = z(x1, x2(x1));

    z_plus = z(x1+delta, x2(x1+delta));

    x1 = x1+delta;

    delta_z = z_current-z_plus;
    
    data.z = [data.z, z_current];
    data.x1 = [data.x1, x1];
    data.x2 = [data.x2, x2(x1)];
    data.delta_z = [data.delta_z, delta_z];

    i = i+1;
    
end

fprintf('x1:%d\n x2:%d\n',x1, x2(x1))

syms f(x1, x2)
f = (A+x1)*(B+x2)==1;
z = norm([x1,x2],1);


fig1 = figure(1);
fig1.PaperPosition = [0, 0, 6, 4];
clf
hold on;
scatter(data.x1(1),data.x2(1))
scatter(data.x1(end-1),data.x2(end-1))
fimplicit(f)
fimplicit(z==data.z(end))
fimplicit(z==data.z(ceil(numel(data.z)/2)))
fimplicit(z==data.z(1))
hold off;
grid on;
xlabel('x1');
ylabel('x2');
legend('Start Point','End Point','(A+x1)*(B+x2)==1','Objective Function', 'Location', 'northeastoutside')
% axis equal
% print(fig1, '-dsvg', 'fig1.svg')

fig2 = figure(2);
% fig2.PaperPosition = [0, 0, 4, 3];
plot(0:i,data.x1,0:i,data.x2,0:i,data.z,0:i,data.delta_z)
legend('x1','x2','z','deltaz'); grid on; xlabel('Iterations')
% print(fig2, '-dsvg', 'fig2.svg')
