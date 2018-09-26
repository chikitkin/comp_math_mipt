n = 30;
x = linspace(0,1,n);
y = rand(1,n);

p = polyfit(x,y,n-1);

xx = linspace(0,1,1000);
hold on;
plot(x, y, 'ro');
plot(xx, polyval(p,xx))