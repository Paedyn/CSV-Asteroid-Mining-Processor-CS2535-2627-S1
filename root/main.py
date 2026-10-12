import csv
data=[]

with open("input_asteroid_data.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("output_asteroid_data.csv", "w", newline="") as output_file:
        writer=csv.writer(output_file)

        fieldnames = [
            "asteroid_id",
            "ore_units",
            "crystal_units",
            "gas_units",
            "total_units",
            "cargo_value"
        ]

        for row in reader:
            asteroid_id = row["asteroid_id"]
            ore = int(row["ore_units"])
            crystal = int(row["crystal_units"])
            gas = int(row["gas_units"])

            total_units = ore + crystal + gas
            cargo_value = (ore * 2) + (crystal * 5) + (gas * 3)
            writer.writerow([
                asteroid_id,
                ore,
                crystal,
                gas,
                cargo_value
            ])
print()
# total_units = ore_units + crystal_units + gas_units
#
# cargo_value = (ore_units × 2) + (crystal_units × 5) + (gas_units × 3)
