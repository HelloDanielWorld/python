import csv

def save_to_csv(file_path, data):
     with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['KEY', 'VALUE'])
        writer.writeheader()
        for key, value in data.items():
            writer.writerow({'KEY': key, 'VALUE': value})


def load_from_csv(file_path, key):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['KEY'] == key:
                return row['VALUE']
            
