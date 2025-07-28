import unittest
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Disable GUI backend for testing

import medical_data_visualizer

class MedicalDataVisualizerTestCase(unittest.TestCase):
    def test_cat_plot(self):
        fig = medical_data_visualizer.draw_cat_plot()
        self.assertEqual(fig.axes[0].get_title(), 'cardio = 0')
        self.assertEqual(fig.axes[1].get_title(), 'cardio = 1')

    def test_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map()
        self.assertEqual(len(fig.axes[0].images), 1)

if __name__ == "__main__":
    unittest.main()
