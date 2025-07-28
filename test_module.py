import unittest
import medical_data_visualizer

class MedicalDataVisualizerTestCase(unittest.TestCase):
    def test_cat_plot(self):
        fig = medical_data_visualizer.draw_cat_plot()
        self.assertIsNotNone(fig, "Expected cat plot figure to be returned.")

    def test_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map()
        self.assertEqual(len(fig.axes[0].images), 1, "Expected one heatmap image on the axis.")

if __name__ == '__main__':
    unittest.main()
