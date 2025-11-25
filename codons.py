def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            codon, amino_acid, single_letter, full_name = line.split()
            codon_dict[codon] = single_letter
    return codon_dict
