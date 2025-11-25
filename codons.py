def create_codon_dict(file_path):
    # 1. יצירת מילון ריק שיכיל את התוצאות
    codon_dict = {}
    
    # 2. פתיחת הקובץ לקריאה
    # השימוש ב-'with' מבטיח שהקובץ ייסגר אוטומטית בסיום
    with open(file_path, 'r') as file:
        
        # 3. מעבר על הקובץ שורה אחר שורה
        for line in file:
            # ניקוי רווחים מיותרים וירידות שורה משני הצדדים
            clean_line = line.strip()
            
            # דילוג על שורות ריקות (אם ישנן)
            if not clean_line:
                continue
            
            # 4. פיצול השורה לרכיבים (קודון וחומצה אמינית)
            # הפקודה split ללא פרמטרים מפצלת לפי רווחים או טאבים
            parts = clean_line.split()
            
            # בדיקה שיש לנו בדיוק שני חלקים כדי למנוע שגיאות
            if len(parts) == 2:
                codon = parts[0]
                amino_acid = parts[1]
                
                # 5. הוספה למילון: המפתח הוא הקודון, הערך הוא החומצה
                codon_dict[codon] = amino_acid
                
    # 6. החזרת המילון המוכן
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
