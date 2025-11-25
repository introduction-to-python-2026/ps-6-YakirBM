def create_codon_dict(file_path):
    codon_dict = {}

    with open(file_path, 'r') as file:
        for line in file:
            # מסירים רווחים מיותרים ו־\n
            line = line.strip()

            # מדלגים על שורות ריקות ושורות הערה
            if not line or line.startswith('#'):
                continue

            # מפצלים את השורה לחלקים
            parts = line.split()

            # נוודא שיש לפחות שני חלקים: קודון + ערך
            if len(parts) < 2:
                continue  # או אפשר להרים שגיאה, אבל למטלה זה מיותר

            codon = parts[0]        # לדוגמה "AAA"
            amino_one_letter = parts[1]  # לדוגמה "K"

            codon_dict[codon] = amino_one_letter

    return codon_dict
