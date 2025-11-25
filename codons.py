def create_codon_dict(file_path):
    codon_dict = {}  # נבנה כאן את המילון: codon -> amino acid name

    # פותחים את הקובץ לקריאה
    with open(file_path, 'r') as file:
        for line in file:
            # מסירים רווחים מיותרים בתחילת וסוף השורה, וגם \n
            line = line.strip()

            # מדלגים על שורות ריקות או שורות הערה
            if not line or line.startswith('#'):
                continue

            # מפרקים את השורה למילים
            parts = line.split()

            # הטור הראשון הוא הקודון (כמו "AUG")
            codon = parts[0]

            # שאר המילים – שם החומצה האמינית, יכול להיות מילה אחת או יותר
            amino_acid = " ".join(parts[1:])

            # מכניסים למילון
            codon_dict[codon] = amino_acid

    return codon_dict
