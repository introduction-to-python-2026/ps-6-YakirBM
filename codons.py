def create_codon_dict(file_path):
    codon_dict = {}
    
    with open(file_path, 'r') as file:
        rows = file.readlines() # בהתאם להוראות במחברת (שלב 1)
        
        for row in rows:
            # שלב 2: ניקוי רווחים ופיצול לפי TAB
            parts = row.strip().split('\t')
            
            # אנו זקוקים לפחות ל-3 עמודות כדי להגיע לאות K
            # (המחברת הראתה שיש 4 עמודות)
            if len(parts) >= 3:
                codon = parts[0]       # AAA
                amino_acid = parts[2]  # K (שים לב! זה אינדקס 2 ולא 1)
                
                codon_dict[codon] = amino_acid
                
    return codon_dict

"""
def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            codon, amino_acid, single_letter, full_name = line.split()
            codon_dict[codon] = single_letter
    return codon_dict
""""
