
%% Actividad: Algoritmos evolutivos
%
%   [+] Autor: David Carrascal <david.carrascal@uah.es> 
%
%   [+] Fecha: 26 Oct 2021
clc
close all
clear variables


%% Abrimos el fichero
load("Practica_Sist_Tec_Teleco.mat")

%% Variables globales
r_base = 0.350; % km


%% Pintamos los puntos, clientes y el radio medio
figure(1)
hold on;

% Pintamos las posiciones posibles de estaciones base
plot(bt(:,1),bt(:,2), '*');

% Pintamos las posiciones de los clientes
plot(xp(:,1), xp(:,2), 'o');

% Pintamos de prueba el radio  de cobertura en la primera psoción permitida
circle(bt(13,1),bt(13,2), r_base)

hold off;
set(gcf,'Position',[100 100 1000 700]);
title("Superfice del despliegue",'interpreter','latex','fontsize',16)
legend("Posiciones posibles para BS", "Clientes en t_{0}", 'fontsize',11)
grid minor
xlabel("y (Km)")
ylabel("x (Km)")
xlim([0 2])
ylim([0 2])

%% Iniciamos la codificación de nuestro Coral :)
% 
% Vamos a utilizar la codificación binaria, nuestro coral estará modelado
% por un vector de 100 digitos binarios. De los cuales solo podremos
% establecer 30 digitos a 1.

% Nuestro espacio de busqueda no tiene por que coincidir con nuestro tamaño
% de coral. 

% Sancho nos comenta que la reproducción asexual no suele funcionar bien en
% el algoritmo :c que de momento no la hagamos 

% Vars del algoritmo %

% Definimos la longitud de nuestra parcela del coral
N = 100;
M = 100;

% Definimos el grado de libre/ocupado
rho_zero = 0.2;

% Ratio de broadcast spawners
Fb = 0.8;

% Intentos de asentarse las larvas en el coral
K = 20;

% Ratio de fragmentación (Reproducción asexual)
Fa = 0.1;

% Ratio de depredación
Fd = Fa;






