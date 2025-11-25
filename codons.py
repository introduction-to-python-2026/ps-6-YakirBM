def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            
            # ניקוי מרכאות למקרה שהקובץ נראה כמו "AAA","K"
            clean_line = clean_line.replace('"', '').replace("'", "")
            
            # זיהוי אוטומטי של המפריד (פסיק או רווח/טאב)
            if ',' in clean_line:
                parts = clean_line.split(',')
            else:
                parts = clean_line.split() # ברירת מחדל: רווחים או טאבים
            
            if len(parts) >= 2:
                key = parts[0].strip()
                val = parts[1].strip()
                
                # הגנה: קודון חייב להיות באורך 3 אותיות (למשל AAA)
                # זה מונע קריאה של כותרות כמו 'Codon' או שורות זבל
                if len(key) == 3:
                    codon_dict[key] = val
                    
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
