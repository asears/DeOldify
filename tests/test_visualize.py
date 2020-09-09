import pytest
from deoldify import visualize


class VisualizeTest(unittest.TestCase):
    def test_plot_transformed_image_from_url():
        ModelImageVisualizer.plot_transformed_image_from_url()

    def test_plot_transformed_image():
        ModelImageVisualizer.plot_transformed_image()

    def test_get_transformed_image():
        ModelImageVisualizer.get_transformed_image()

    def test_VideoColorizer_colorize_from_url():
        VideoColorizer.colorize_from_url()

    def test_VideoColorizer_colorize_from_file_name():
        VideoColorizer.colorize_from_file_name()

    def test_get_video_colorizer():
        get_video_colorizer()

    def test_get_stable_video_colorizer():
        get_stable_video_colorizer

    def test_get_image_colorizer():
        get_image_colorizer()

    def test_get_stable_image_colorizer():
        get_stable_image_colorizer()

    def test_get_artistic_image_colorizer():
        get_artistic_image_colorizer

    def test_show_image_in_notebook():
        show_image_in_notebook()

    def test_show_video_in_notebook():
        show_video_in_notebook()
