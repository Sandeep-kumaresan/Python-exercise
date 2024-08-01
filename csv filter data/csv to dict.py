import csv

# File paths
master_file_path = 'master.csv'
product_file_path = 'product.csv'
output_file_path = 'output.csv'


# Read the master product CSV into a dictionary
def read_master_product(file_path):
    master_dict = {}
    with open(file_path, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            master_dict[row['id']] = row
    return master_dict


# Read the product CSV to get the list of IDs
def read_product(file_path):
    product_ids = []
    with open(file_path, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            product_ids.append(row['id'])
    return product_ids


# Write the records to the output CSV
def write_output(file_path, records, fieldnames):
    with open(file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)


# Main function to orchestrate the process
def main():
    master_dict = read_master_product(master_file_path)
    product_ids = read_product(product_file_path)

    # Get the fieldnames from the master dictionary (assuming all records have the same fields)
    fieldnames = list(master_dict.values())[0].keys()

    # Fetch the corresponding records from the master dictionary
    records_to_write = [master_dict[prod_id] for prod_id in product_ids if prod_id in master_dict]

    # Write the fetched records to output CSV
    write_output(output_file_path, records_to_write, fieldnames)
    print(f"Output written to {output_file_path}")


if __name__ == "__main__":
    main()
