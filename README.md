# 🧾 HTML zu JasperReport Konverter

## 🎯 Projektziel

Dieses Projekt bietet eine Sammlung von Jupyter-Notebooks und Python-Funktionen, um HTML5-Code (z.B. aus Annotierungs-Tools) in eine Form zu überführen, die mit JasperReport kompatibel ist. Dabei werden bestimmte CSS-Angaben konvertiert oder angepasst – z.B. `bottom` zu `top`, oder zusätzliche `offsets` berücksichtigt.

Die Umsetzung erfolgt mit **einfachen Python-Funktionen**, die HTML-Code parsen und manipulieren. Die Bedienung erfolgt über **Jupyter-Notebooks**, die für jeden Anwendungsfall separat und übersichtlich aufgebaut sind.

## 📋 Funktionen

Das Projekt bietet folgende Hauptfunktionen:

1. **Umrechnung von `bottom` zu `top`**: Konvertiert bottom-positionierte Elemente zu top-positionierten Elementen
2. **Anwendung von Offsets**: Fügt Offset-Werte zu Positionsangaben hinzu
3. **Batch-Konvertierung**: Verarbeitet mehrere HTML-Dateien in einem Durchgang
4. **Extraktion von Positionsdaten**: Extrahiert und analysiert Positionsinformationen aus HTML-Elementen
5. **Konvertierung zu JasperReport-XML**: Wandelt HTML-Elemente in JasperReport-XML-Snippets um

## 📂 Projektstruktur

```
html_to_jasper/
├── data/
│   ├── original/      # HTML-Originaldateien
│   └── output/        # Konvertierte HTML-Dateien
├── notebooks/
│   ├── 01_convert_bottom_to_top.ipynb
│   ├── 02_apply_offset.ipynb
│   ├── 03_batch_convert_folder.ipynb
│   ├── 04_extract_positions.ipynb
│   └── 05_html_to_jasper_snippets.ipynb
├── shared/
│   ├── constants.py   # Seitengröße, Ränder etc.
│   └── html_utils.py  # Wiederverwendbare Funktionen
└── README.md
```

## 🔧 Installation und Voraussetzungen

### Voraussetzungen

- Python 3.6 oder höher
- Jupyter Notebook oder JupyterLab
- Grundkenntnisse in Python und HTML

### Installation

1. Klone das Repository:
   ```bash
   git clone https://github.com/username/html_to_jasper.git
   cd html_to_jasper
   ```

2. Installiere die benötigten Pakete:
   ```bash
   pip install beautifulsoup4 ipywidgets pandas
   ```

3. Starte Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## 📒 Notebooks

### 01_convert_bottom_to_top.ipynb

In diesem Notebook wird die Positionierung von HTML-Elementen, die per `bottom` definiert sind, in `top`-Positionen umgerechnet.

**Bedienung:**
1. HTML-Code eingeben oder Datei auswählen
2. Offset-Werte für X und Y optional einstellen
3. Umrechnung per Button starten
4. Ausgabe wird angezeigt und in `data/output/` gespeichert

### 02_apply_offset.ipynb

Dieses Notebook ermöglicht die Anwendung von Offset-Korrekturen für `left` und `top` Werte in HTML-Elementen.

**Bedienung:**
1. HTML-Code eingeben oder Datei auswählen
2. Offset-Werte für X und Y einstellen
3. Umrechnung per Button starten
4. Ausgabe wird angezeigt und in `data/output/` gespeichert

### 03_batch_convert_folder.ipynb

Mit diesem Notebook können alle HTML-Dateien in einem Ordner automatisch verarbeitet werden.

**Bedienung:**
1. Quell- und Zielordner auswählen
2. Konvertierungsfunktion auswählen (Bottom zu Top oder Offset anwenden)
3. Parameter für die gewählte Funktion einstellen
4. Batch-Verarbeitung per Button starten
5. Ergebnisse werden im Zielordner gespeichert

### 04_extract_positions.ipynb

Dieses Notebook extrahiert Positionsinformationen (top/left) aus HTML-Elementen und stellt sie tabellarisch dar.

**Bedienung:**
1. HTML-Code eingeben oder Datei auswählen
2. Extraktion per Button starten
3. Positionsdaten werden als Tabelle angezeigt
4. Optional: Daten als CSV exportieren

### 05_html_to_jasper_snippets.ipynb

Dieses Notebook konvertiert HTML-Elemente in JasperReport-XML-Bausteine, die in JasperReport-Vorlagen eingefügt werden können.

**Bedienung:**
1. HTML-Code eingeben oder Datei auswählen
2. Konvertierungsoptionen einstellen (Skalierungsfaktoren, Header/Footer, etc.)
3. Konvertierung per Button starten
4. JasperReport-XML wird angezeigt und kann kopiert werden
5. Optional: XML in Datei speichern

## 🧩 Shared Modules

### constants.py

Enthält alle technischen Konstanten für die HTML- und JasperReport-Konvertierung:

- HTML-Dimensionen und Ränder
- JasperReport-Dimensionen und Ränder
- Skalierungsfaktoren für die Konvertierung

### html_utils.py

Enthält wiederverwendbare Funktionen für die HTML-Verarbeitung:

- HTML-Parsing und CSS-Extraktion
- Konvertierung von bottom zu top
- Anwendung von Offsets
- Extraktion von Positionsdaten
- Dateioperationen (Laden/Speichern)
- Batch-Verarbeitung

## 💡 Tipps zur Verwendung

- Stelle sicher, dass dein HTML-Code gültig ist und die erforderlichen CSS-Eigenschaften enthält
- Für die Konvertierung von `bottom` zu `top` sollten die Elemente mit `bottom` Positionierung versehen sein
- Die Skalierungsfaktoren können angepasst werden, um die Größenverhältnisse zwischen HTML und JasperReport zu optimieren
- Nutze die Batch-Verarbeitung für die effiziente Konvertierung mehrerer Dateien
- Exportiere Positionsdaten als CSV für weitere Analysen oder Dokumentation

## 📞 Fehlerbehebung

Bei Problemen mit den Notebooks:

1. Stelle sicher, dass alle benötigten Bibliotheken installiert sind:
   ```python
   !pip install beautifulsoup4 ipywidgets pandas
   ```

2. Überprüfe die Pfade zu den Dateien und Ordnern
3. Prüfe, ob der HTML-Code gültig ist und die erwarteten CSS-Eigenschaften enthält
4. Bei Fehlern in der Konvertierung, überprüfe die Konstanten in `shared/constants.py`