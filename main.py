from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Ejecutar la función de gráfico categórico y guardar el resultado
cat_fig = draw_cat_plot()
cat_fig.savefig("catplot.png")

# Ejecutar la función del heatmap y guardar el resultado
heat_fig = draw_heat_map()
heat_fig.savefig("heatmap.png")
