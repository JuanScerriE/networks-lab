import argparse
import csv

def process_csv(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            data = [(float(row[1]), int(row[5])) for row in [row for row in reader][1:]]
        

        packet_count = len(data)
        total_size = 8192 * packet_count
        start_time = min((time for time, _ in data))
        end_time = max((time for time, _ in data))
        diff_time = end_time - start_time

        print(
f"""General Info ->
Packet Count: {packet_count}
Total Size (in Bytes): {total_size}
Start Time (in Seconds): {start_time}
End Time (in Seconds): {end_time}
Difference (in Seconds): {diff_time}

Conversions ->
Total Size (in MibiBytes): {(total_size) / (1024 ** 2)}""")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument('file', metavar='FILE', help='Path to the CSV file')

    args = parser.parse_args()
    process_csv(args.file)

if __name__ == "__main__":
    main()
