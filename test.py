from save_to_csv import load_from_csv

key_retrieve = "key1"

file_path = r"C:\pythonCSV\python\data.csv"



value = load_from_csv(file_path, key_retrieve)
print(value)