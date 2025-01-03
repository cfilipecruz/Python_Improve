import re
from collections import defaultdict
from datetime import datetime

def extract_data(file_path):
    """Extracts relevant data from the text file."""
    wound_treatment_keywords = [
        "feridas", "ulceras", "pensos", "ferida", "tratamento de úlcera", "penso de úlcera",
        "vigiar penso", "ferida cirúrgica", "líquido de drenagem"
    ]
    muscular_treatment_keywords = [
        "exercícios musculares", "exercitação musculoarticular", "espasticidade", "equilíbrio corporal",
        "alongamento", "técnica de posicionamento", "cinesiterapia"
    ]

    results = defaultdict(lambda: {
        "Vezes intervido": 0,
        "Tratamento de feridas": 0,
        "Habilitação muscular": 0
    })
    not_registered_correctly = []

    current_name = None
    current_date = None
    processed_dates = set()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # Match date and name pattern
            match = re.match(r"^\s*(\d{4}/\d{2}/\d{2})\s+\d{4}/\d{2}/\d{2}\s+\d+\s+(.*)$", line)
            if match:
                # Save the current date and name
                current_date = match.group(1)
                current_name = match.group(2).strip()
                key = (current_name, current_date)

                # Increment intervention count only if this person/date combo hasn't been processed
                if key not in processed_dates:
                    results[current_name]["Vezes intervido"] += 1
                    processed_dates.add(key)
                continue

            # Count keywords in the current section, ensuring unique counts per person/date
            if current_name and current_date:
                key = (current_name, current_date)

                if key in processed_dates:
                    if any(keyword in line.lower() for keyword in wound_treatment_keywords):
                        results[current_name]["Tratamento de feridas"] += 1
                        processed_dates.remove(key)  # Prevent double counting for the same date

                    if any(keyword in line.lower() for keyword in muscular_treatment_keywords):
                        results[current_name]["Habilitação muscular"] += 1
                        processed_dates.remove(key)  # Prevent double counting for the same date

    # Move incorrectly registered names to a separate list
    valid_results = {}
    for name, data in results.items():
        if data["Tratamento de feridas"] > 0 or data["Habilitação muscular"] > 0:
            valid_results[name] = data
        else:
            not_registered_correctly.append(name)

    return valid_results, not_registered_correctly

def save_to_file(results, not_registered_correctly, output_path):
    """Saves the processed data to a file."""
    total_interventions = 0
    total_wound_treatments = 0
    total_muscular_habilitations = 0

    with open(output_path, "w", encoding="utf-8") as file:
        # Write valid entries
        for name, data in results.items():
            total_interventions += data["Vezes intervido"]
            total_wound_treatments += data["Tratamento de feridas"]
            total_muscular_habilitations += data["Habilitação muscular"]

            file.write(f"Nome: {name}\n")
            file.write(f"  Vezes intervido: {data['Vezes intervido']}\n")
            file.write(f"  Tratamento de feridas: {data['Tratamento de feridas']}\n")
            file.write(f"  Habilitação muscular: {data['Habilitação muscular']}\n")
            file.write("\n\n")

        # Write incorrectly registered names
        file.write("Pessoas mal registadas ou sem tratamento:\n")
        for name in not_registered_correctly:
            file.write(f"{name}\n")

        # Write totals
        file.write("\nTotais:\n")
        file.write(f"Total de intervenções: {total_interventions}\n")
        file.write(f"Total de tratamentos de feridas: {total_wound_treatments}\n")
        file.write(f"Total de habilitações musculares: {total_muscular_habilitations}\n")

def main():
    """Main function to process the input file and save results."""
    input_file_path = "C:\\Users\\marqu\\Desktop\\TXT\\Input.txt"  # Path to input file
    output_file_path = "C:\\Users\\marqu\\Desktop\\TXT\\Output.txt"  # Path to output file

    results, not_registered_correctly = extract_data(input_file_path)
    save_to_file(results, not_registered_correctly, output_file_path)

    print("Processing complete. Results saved to Output.txt.")

if __name__ == "__main__":
    main()