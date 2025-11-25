def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            # מפרקים את השורה לארבעה חלקים
            codon, amino_acid, single_letter, full_name = line.split()
            # מוסיפים למילון: קודון → קיצור של אות אחת
            codon_dict[codon] = single_letter
    return codon_dict
