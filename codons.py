def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            
            # שינוי קריטי: פיצול לפי פסיק
            # ברוב הקבצים המדעיים הפורמט הוא Codon,Letter (למשל AAA,K)
            parts = clean_line.split(',')
            
            if len(parts) == 2:
                # אנו משתמשים ב-strip() גם על החלקים עצמם
                # כדי להימנע ממצב של ' K' (עם רווח) במקום 'K'
                codon = parts[0].strip()
                amino_acid = parts[1].strip()
                
                codon_dict[codon] = amino_acid
                
    return codon_dict





"""
def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            # מפרקים את השורה לארבעה חלקים
            codon, amino_acid, single_letter, full_name = line.split()
            # מוסיפים למילון: קודון → קיצור של אות אחת
            codon_dict[codon] = single_letter
    return codon_dict
"""
