# 🎰 Interaktives Web-Casino

Ein Full-Stack Abschlussprojekt welches innerhalb des 2 Wöchigen Orientierungskurses beim DCI entstanden ist. 
Vorkenntnisse: Keine / Zeitaufwand: 3 std/vormittags und 2 bis 3 Stunden Abends bis das Wissen angeeignet war.

Das Projekt demonstriert die asynchrone Kommunikation zwischen einem Python-Backend und einem modernen JavaScript-Frontend.

## 🚀 Key Features & Technische Highlights

- **Fullstack-Architektur:** Saubere Trennung zwischen serverseitiger Programmierlogik (Backend) und dynamischer Benutzeroberfläche (Frontend).
- **Sichere Backend-Berechnungen:** Alle Spielergebnisse, Zufallszahlen und gezogenen Karten werden manipulationssicher auf dem Server berechnet und per API bereitgestellt.
- **Asynchrone Benutzeroberfläche (UX):** Verwendung von JavaScripts `fetch()`, um Spieldaten in Echtzeit abzufragen und darzustellen, ohne dass die Webseite neu geladen werden muss.

---

## 🎮 Integrierte Spiele

### 🃏 Mini-Blackjack
- **Logik:** Der Spieler zieht Karten (Werte 1–10) aus einem serverseitigen Zufalls-Stapel gegen den Computer.
- **Regeln:** Wer die höhere Punktzahl hat, gewinnt. Erreicht ein Spieler oder der Computer mehr als 21 Punkte ("Bust" ab 22), ist das Spiel sofort verloren.

### 🔴 Mini-Roulette
- **Logik:** Tippen auf Zahlen von 1 bis 10 sowie auf die Farben Rot oder Schwarz.
- **Backend-Fokus:** Die Gewinnzahl und Gewinnfarbe werden im Python-Backend über einen Zufallsgenerator ermittelt und mit dem Tipp des Spielers abgeglichen.

### 🪙 Münzwurf & 🔢 Zahlenrätsel
- Klassische Logikspiele zur Demonstration von Benutzereingabe-Validierungen und schnellen Status-Rückmeldungen vom Server.

---

## 🛠️ Verwendete Technologien

- **Backend:** Python 3, Flask (Micro-Framework)
- **Frontend:** HTML5, CSS3 (Responsive Design), JavaScript (ES6, Fetch API)
- **Schnittstelle:** REST-API (JSON-Datenaustausch)

---

