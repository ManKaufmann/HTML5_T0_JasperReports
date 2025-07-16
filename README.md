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

---

## 💡 Hinweis

Die Transformation von HTML nach JasperReports ist kein 1:1-Mapping. Daher verwenden wir spezielle Operationen, die auf häufige Strukturen abgestimmt sind (Tabellen, Textblöcke, Styles).

---

## 📞 Bei Problemen

Bitte stelle sicher, dass alle benötigten Bibliotheken in Colab installiert sind, z. B. mit:
```python
!pip install beautifulsoup4 lxml
