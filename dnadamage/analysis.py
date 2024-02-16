import os
from skimage import io, filters, measure, morphology, feature
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import csv

# Function to read and preprocess the image
def preprocess_image(image_path):
    image = io.imread(image_path, as_gray=True)
    # Use an adaptive threshold to account for variable lighting conditions
    image_blurred = filters.gaussian(image, sigma=1.0)
    thresh = filters.threshold_local(image_blurred, block_size=51, method='gaussian')
    binary = image_blurred > thresh
    return binary.astype(np.uint8)  # Convert to an unsigned byte image

# Function to enhance spots and possibly tails
def highlight_spread_tails(binary_image):
    # Apply morphological closing to connect components of potential tails
    selem = morphology.disk(2)
    closed = morphology.closing(binary_image, selem)
    return closed

# Function to detect and classify spots with additional differentiation of tail lengths
def detect_and_classify_spots(binary_image):
    label_img = measure.label(binary_image)
    regions = measure.regionprops(label_img)

    # Initialize counters
    round_spots = 0
    short_spread_tail_spots = 0
    long_spread_tail_spots = 0

    # Placeholder thresholds for classification
    tail_length_threshold = 100  # This value should be determined based on your image analysis

    for region in regions:
        # Use area, eccentricity, and solidity to distinguish spots
        if region.area < 50:  # Ignore small artifacts
            continue
        if region.eccentricity < 0.6 and region.solidity > 0.9:
            round_spots += 1
        elif region.eccentricity >= 0.8:
            if region.major_axis_length < tail_length_threshold:
                short_spread_tail_spots += 1
            else:
                long_spread_tail_spots += 1

    return round_spots, short_spread_tail_spots, long_spread_tail_spots

# Function to analyze the images and return results
def analyze_images(image_paths):
    results = {}
    for path in image_paths:
        binary_image = preprocess_image(path)
        tail_highlighted_image = highlight_spread_tails(binary_image)
        # Update to handle three return values
        round_spots, short_spread_tail_spots, long_spread_tail_spots = detect_and_classify_spots(tail_highlighted_image)
        total_spots = round_spots + short_spread_tail_spots + long_spread_tail_spots
        results[path] = {
            'round_spots': round_spots,
            'short_spread_tail_spots': short_spread_tail_spots,  # Added this line
            'long_spread_tail_spots': long_spread_tail_spots,    # Added this line
            'percentage_round': (round_spots / total_spots * 100) if total_spots > 0 else 0,
            'percentage_short_spread_tail': (short_spread_tail_spots / total_spots * 100) if total_spots > 0 else 0,  # Updated this line
            'percentage_long_spread_tail': (long_spread_tail_spots / total_spots * 100) if total_spots > 0 else 0     # Updated this line
        }
    return results
