import unittest
import numpy as np
import os
from skimage import io
from dnadamage.analysis import preprocess_image, detect_and_classify_spots

class TestAnalysisFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This method will be run once before all tests
        # Define the path to your test images directory
        cls.image_directory = "/home/drdx/IBE - MY GROUP/image analytics"
        cls.test_image_path = os.path.join(cls.image_directory, "test_image.jpg")  # Adjust with an actual test image name

    def test_preprocess_image_exists(self):
        # Check if the test image exists to ensure tests are valid
        self.assertTrue(os.path.exists(self.test_image_path), "Test image does not exist.")

    def test_preprocess_image(self):
        # Load a test image, preprocess it, and check basic properties
        image = io.imread(self.test_image_path, as_gray=True)
        binary_image = preprocess_image(self.test_image_path)
        self.assertIsInstance(binary_image, np.ndarray, "Preprocessed image is not an ndarray.")
        self.assertEqual(image.shape, binary_image.shape, "Preprocessed image shape does not match original.")
        self.assertTrue((binary_image == 0).all() or (binary_image == 1).all(), "Preprocessed image is not binary.")

    def test_detect_and_classify_spots(self):
        # This test might be more complex as it involves analyzing the output of detect_and_classify_spots
        # Ideally, you would have a test image with known quantities of spots and their classifications
        # Since creating a synthetic image or ensuring a specific outcome requires knowing the image contents,
        # this pseudo-test will outline the structure but won't execute real assertions

        # Example structure:
        # synthetic_image = np.zeros((100, 100), dtype=np.uint8)
        # round_spots, short_spread_tail_spots, long_spread_tail_spots = detect_and_classify_spots(synthetic_image)
        # self.assertEqual(round_spots, expected_round_spots, "Detected round spots do not match expected.")
        # self.assertEqual(short_spread_tail_spots, expected_short_spread_tail_spots, "Detected short spread tail spots do not match expected.")
        # self.assertEqual(long_spread_tail_spots, expected_long_spread_tail_spots, "Detected long spread tail spots do not match expected.")
        pass

    # Additional tests can be added as necessary

if __name__ == '__main__':
    unittest.main()

