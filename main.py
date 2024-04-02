import json
import csv
import os


def json_to_csv(json_file, csv_file):
    # Open the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Open CSV file in write mode
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write header using keys from the first dictionary in the JSON
        writer.writerow(data[0].keys())

        # Write data rows
        for row in data:
            writer.writerow(row.values())


# Take input JSON file path using os.path.join
json_file = input("Enter path to JSON file: ")
csv_file = os.path.splitext(json_file)[0] + '.csv'  # Change extension to CSV

json_to_csv(json_file, csv_file)
print(f"Conversion completed. CSV file saved as: {csv_file}")
