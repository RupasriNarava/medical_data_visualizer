# This file is used to run your functions and test them visually
from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Run the categorical plot function and save image
cat_plot_fig = draw_cat_plot()
cat_plot_fig.savefig("catplot.png")

# Run the heatmap function and save image
heat_map_fig = draw_heat_map()
heat_map_fig.savefig("heatmap.png")
