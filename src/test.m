run = 0;
alpha = 0.25;
betha = 0.75;
ngens = 0:1:999;

data_table = readtable(strcat("results/alpha_",num2str(alpha*100),".0_betha_",num2str(100*betha),".0/hist_run_",num2str(run),".csv"), 'NumHeaderLines',1);

% Vamos a ordenar la tabla
data_table_ordered = sortrows(data_table);

% Pasamos a matriz
data = data_table_ordered{:,:};
    
% Pintamos la figura
data_ponits = data(:, [2 3 4]);
h=figure();
set(gcf,'Position',[100 100 900 700]);
plot(ngens, data_ponits(:,1)); hold on;
plot(ngens, data_ponits(:,2)); hold on;
plot(ngens, data_ponits(:,3)); hold off;
grid on
title("Alpha: " + num2str(alpha*100) + " - Betha: " + num2str(100*betha) +" - Run: " +num2str(run));
xlabel("Nº generaciones")
legend("Worse case", "Avg", "Best case")

% set(h,'Units','Inches');
% pos = get(h,'Position');
% set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])
% strPath = strcat('ieee123/fig/powerBalance_d', num2str(delta));
% print(h,strPath,'-dpdf','-r0')