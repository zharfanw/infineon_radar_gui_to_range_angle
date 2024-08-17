close all
clear all
clc

% % make a rectangular grid of r and theta,
% % then define x and y in the usual way 
% rr = 0:1:20;
% thth = (0:.05:1)*2*pi;
% [r th] = meshgrid(rr,thth);
% x = r.*cos(th);
% y = r.*sin(th);
% z = 1 + x.^2 - y.^2;
% surf(x,y,z)
% view(2)
% 
% % set(c_bfm,'LineStyle','none');
% hold on
% plot([zeros(1,13); 90*cosd(0:30:360)], [zeros(1,13); 90*sind(0:30:360)],'k')
% plot(90*((0:0.33:1)'*cosd(0:10:360))', 90*((0:0.33:1)'*sind(0:10:360))','k')
% colorbar
% set(colorbar,'FontSize',16)
% axis equal
% set(gca, 'Box','off', 'XColor','none', 'YColor','none',  'Color','none')
% hold off
% 
% xt = 105*cosd(0:30:330);
% yt = 105*sind(0:30:330);
% tlbls = sprintfc('%3d°', (0:30:330));
% text(xt, yt, tlbls)

% Definisikan jari-jari dan sudut
r = linspace(0, 2, 20);
theta = linspace(0, 2*pi, 91);

% Buat matriks jari-jari dan sudut
[R, THETA] = meshgrid(r, theta);

% Hitung koordinat kartesian
x = R .* cos(THETA);
y = R .* sin(THETA);

% Definisikan fungsi z
z = R .* sin(2*THETA);

% Buat plot polar mesh
surf(x, y, z,'EdgeColor', 'none');
xlabel('x');
ylabel('y');
zlabel('z');
title('Plot Polar Mesh');
view(2)

% Tambahkan label untuk radius dan sudut
text(1.5, 0, 2, 'Radius', 'FontSize', 12);
text(0, 1.5, 2, 'Sudut', 'FontSize', 12);