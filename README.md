## 📘 Einführung in das Projekt: HTML5 nach JasperReports mit Python in Google Colab

Willkommen zum Projekt!  
In diesem Projekt entwickeln wir Python-Funktionen, die HTML5-Code in die Sprache von JasperReports überführen. Ziel ist es, Webinhalte automatisiert in strukturierte Report-Layouts zu konvertieren.

### 🔧 Voraussetzungen

- Ein Google-Konto
- Grundkenntnisse in Python
- HTML5-Basiswissen
- Grundverständnis von JasperReports (optional, hilfreich)

---

## ▶️ Google Colab öffnen und starten

1. Öffne [Google Colab](https://colab.research.google.com).
2. Klicke auf „Datei öffnen“ > „GitHub“ und gib das Projekt-Repository oder den Dateipfad ein.
3. Alternativ kannst du eine `.ipynb`-Datei von deinem lokalen Rechner hochladen.
4. Nach dem Öffnen kannst du den Code sofort ausführen oder anpassen.

---

## 🚀 Projektziel

Wir erstellen ein Python-Modul, das folgende Aufgaben erfüllt:

1. **Konstanten setzen**  
   - HTML-Seitengröße definieren (z. B. `width`, `height`, `margins`)
   - JasperReports-Parameter definieren (z. B. `pageWidth`, `pageHeight`)

2. **HTML-Code übergeben & speichern**  
   - Eingabe von HTML als String oder Datei
   - Speicherung zur Weiterverarbeitung

3. **Code-Sektionen erkennen & strukturieren**  
   - Z. B. `div`, `table`, `img`, `p`, `span` usw.
   - Klassifizierung für spätere Konvertierung

4. **Verarbeitung & Ausgabe**  
   - Konvertierung in JasperReports XML-Syntax
   - Export in `.jrxml` oder Vorschau als strukturierter Text

---

## 📂 Struktur & Module

- `HTML5_to_JasperReports_Converter.ipynb` – Hauptnotebook mit allen Funktionen zur Konvertierung
- `OLD_HTML_to_Jesperreports_COnverter.ipynb` – Alte Version des Konverters (Referenz)
- `html_converter.py` - Python-Modul mit der Implementierung der Konvertierungsfunktionen

---

## 🔄 Verwendung der `orginal_Html_string` Funktion

Die `orginal_Html_string` Funktion ermöglicht es dir, deinen eigenen HTML-Code für die Konvertierung zu verwenden.

### Wie man die Funktion verwendet:

1. **Im Jupyter Notebook:**
   ```python
   # Importiere die benötigten Module
   from html_converter import convert_bottom_to_top, save_html_with_timestamp, save_original_html
   
   # Definiere deinen HTML-String
   mein_html = """<!DOCTYPE html>
   <html>
   <head>
       <meta charset="utf-8" />
   </head>
   <body>
       <!-- Dein HTML-Code hier -->
       <div style="position: absolute; left: 100px; bottom: 200px;">Beispieltext</div>
   </body>
   </html>"""
   
   # Verwende die orginal_Html_string Funktion
   # Diese Funktion nimmt deinen HTML-String entgegen und gibt ihn zurück
   # Beispiel aus dem Notebook:
   html_code = mein_html  # In deinem Code: html_code = orginal_Html_string(mein_html)
   
   # Jetzt kannst du mit dem HTML-Code weiterarbeiten
   # z.B. Konvertierung von bottom zu top Koordinaten
   converted_html = convert_bottom_to_top(html_code)
   
   # Speichere das Ergebnis
   save_html_with_timestamp(converted_html)
   ```

2. **Parameter der `orginal_Html_string` Funktion:**
   - `html_string`: Der HTML-Code als String, der für die Konvertierung verwendet werden soll

3. **Rückgabewert:**
   - Die Funktion gibt den übergebenen HTML-String zurück, der dann für die weitere Verarbeitung verwendet werden kann

### Tipps:
- Stelle sicher, dass dein HTML-Code gültig ist und die erforderlichen CSS-Eigenschaften enthält
- Für die Konvertierung von `bottom` zu `top` Koordinaten sollten die Elemente mit `bottom` Positionierung versehen sein
- Du kannst auch HTML aus einer Datei laden:
  ```python
  from html_converter import load_html_from_file
  
  # Lade HTML aus einer Datei
  html_code = load_html_from_file("pfad/zu/deiner/datei.html")
  ```

---

## 💡 Hinweis

Die Transformation von HTML nach JasperReports ist kein 1:1-Mapping. Daher verwenden wir spezielle Operationen, die auf häufige Strukturen abgestimmt sind (Tabellen, Textblöcke, Styles).

---

## 📞 Bei Problemen

Bitte stelle sicher, dass alle benötigten Bibliotheken in Colab installiert sind, z. B. mit:
```python
!pip install beautifulsoup4 lxml
