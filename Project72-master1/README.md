έχω προσθέσει 2η ζώνη στο xml.j2 <zone2>
στο jspars διαβάζει 2 xlsm ένα για κάθε ζώνη z1 z2. Αυτό το έκανα με το να προσθέσω ένα ακόμα argument στις μεθόδους parse
Ενώ δουλεύει σωστά για τα opaque ( δηλ. μου προσθέτει στο json το opaque_parameter1 ... και το opaque_parameterz2  και στο xml

 στο def ...etc μου κάνει update το out.json αλλά μου αντικαθιστά την τιμή parameter6z1 με την parameter6z2 αντί να τις κρατήσει και τις 2. Τις 2 αυτές παραμέτρους μου τις κάνει σωστά parse  από τα excel γιατί τις κάνω print
