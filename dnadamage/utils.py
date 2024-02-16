import csv
import os

def save_results_to_csv(results, directory_path):
    # Ensure the directory exists; if not, create it
    if not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)

    # Define the CSV file path
    csv_file_path = os.path.join(directory_path, 'analysis_results.csv')
    
    # Adjusted field names for the CSV
    fieldnames = ['Image Name', 'Round Spots', 'Short Spread Tail Spots', 'Long Spread Tail Spots', 'Percentage Round', 'Percentage Short Spread Tail', 'Percentage Long Spread Tail']

    # Write to CSV
    with open(csv_file_path, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()
        
        # Write the results for each image
        for image_path, data in results.items():
            image_name = os.path.basename(image_path)
            writer.writerow({
                'Image Name': image_name,
                'Round Spots': data['round_spots'],
                'Short Spread Tail Spots': data['short_spread_tail_spots'],
                'Long Spread Tail Spots': data['long_spread_tail_spots'],
                'Percentage Round': f"{data['percentage_round']:.2f}",
                'Percentage Short Spread Tail': f"{data['percentage_short_spread_tail']:.2f}",
                'Percentage Long Spread Tail': f"{data['percentage_long_spread_tail']:.2f}"
            })

