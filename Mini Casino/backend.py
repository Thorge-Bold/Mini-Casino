from flask import Flask, jsonify, request
from flask_cors import CORS
import random

mini_casino = Flask(__name__)
CORS(mini_casino)

blackjack_zustand = {
    "spieler_karten": [],
    "computer_karten": [],
    "spieler_punkte": 0,
    "computer_punkte": 0,
    "spiel_aktiv": False
}

KARTEN_DECK = [
    {"name": "2", "wert": 2},
    {"name": "3", "wert": 3},
    {"name": "4", "wert": 4},
    {"name": "5", "wert": 5},
    {"name": "6", "wert": 6},
    {"name": "7", "wert": 7},
    {"name": "8", "wert": 8},
    {"name": "9", "wert": 9},
    {"name": "10", "wert": 10},
    {"name": "Bube", "wert": 10},
    {"name": "Dame", "wert": 10},
    {"name": "König", "wert": 10},
    {"name": "Ass", "wert": 11}
]

def punkte_berechnen(karten):
    return sum(karte["wert"] for card in karten)

@mini_casino.route("/zahlenraten", methods=["GET"])
def raten():
    ziel = random.randint(1, 10)
    tipp = int(request.args.get("tipp", 0))
    if tipp == ziel:
        return jsonify({"ergebnis": f"Gewonnen! Die richtige Zahl war {ziel}."})
    else:
        return jsonify({"ergebnis": f"Leider falsch. Die richtige Zahl war {ziel}."})

@mini_casino.route("/roulette", methods=["GET"])
def roulette():
    tipp_zahl = request.args.get("zahl")
    tipp_farbe = request.args.get("farbe")
    gewinn_zahl = random.randint(1, 10)
    gewinn_farbe = random.choice(["rot", "schwarz"])
    zahl_getroffen = (tipp_zahl and int(tipp_zahl) == gewinn_zahl)
    farbe_getroffen = (tipp_farbe and tipp_farbe.lower() == gewinn_farbe)
    if zahl_getroffen and farbe_getroffen:
        msg = f"Hauptgewinn! Zahl {gewinn_zahl} ({gewinn_farbe}) getroffen!"
    elif farbe_getroffen:
        msg = f"Farbe richtig! Es war die {gewinn_zahl} ({gewinn_farbe})."
    elif zahl_getroffen:
        msg = f"Zahl richtig! Es war die {gewinn_zahl} ({gewinn_farbe})."
    else:
        msg = f"Verloren. Es war die {gewinn_zahl} ({gewinn_farbe})."
    return jsonify({"ergebnis": msg})

@mini_casino.route("/muenzwurf", methods=["GET"])
def muenzwurf():
    tipp = request.args.get("tipp")
    ergebnis_wurf = random.choice(["Kopf", "Zahl"])
    if tipp and tipp.lower() == ergebnis_wurf.lower():
        return jsonify({"ergebnis": f"Gewonnen! Die Münze zeigt {ergebnis_wurf}."})
    else:
        return jsonify({"ergebnis": f"Leider verloren! Die Münze zeigte {ergebnis_wurf}."})

@mini_casino.route("/blackjack/start", methods=["GET"])
def blackjack_start():
    blackjack_zustand["spieler_karten"] = [random.choice(KARTEN_DECK)]
    blackjack_zustand["computer_karten"] = [random.choice(KARTEN_DECK)]
    blackjack_zustand["spieler_punkte"] = sum(k["wert"] for k in blackjack_zustand["spieler_karten"])
    blackjack_zustand["computer_punkte"] = sum(k["wert"] for k in blackjack_zustand["computer_karten"])
    blackjack_zustand["spiel_aktiv"] = True
    return jsonify({
        "spieler_karten": [c["name"] for c in blackjack_zustand["spieler_karten"]],
        "computer_karten": [c["name"] for c in blackjack_zustand["computer_karten"]],
        "spieler_punkte": blackjack_zustand["spieler_punkte"],
        "computer_punkte": blackjack_zustand["computer_punkte"],
        "status": "running"
    })

@mini_casino.route("/blackjack/ziehen", methods=["GET"])
def blackjack_ziehen():
    if not blackjack_zustand["spiel_aktiv"]:
        return jsonify({"ergebnis": "Starte zuerst ein neues Spiel!", "status": "inactive"})
    
    neue_karte_spieler = random.choice(KARTEN_DECK)
    blackjack_zustand["spieler_karten"].append(neue_karte_spieler)
    blackjack_zustand["spieler_punkte"] = sum(k["wert"] for k in blackjack_zustand["spieler_karten"])
    
    if blackjack_zustand["spieler_punkte"] > 21:
        blackjack_zustand["spiel_aktiv"] = False
        return jsonify({
            "spieler_karten": [c["name"] for c in blackjack_zustand["spieler_karten"]],
            "spieler_punkte": blackjack_zustand["spieler_punkte"],
            "ergebnis": f"Verloren! Mit {blackjack_zustand['spieler_punkte']} Punkten überkauft.",
            "status": "bust"
        })
        
    gegner_nachricht = "Der Computer hält seine Punkte."
    if blackjack_zustand["computer_punkte"] < 17:
        neue_karte_computer = random.choice(KARTEN_DECK)
        blackjack_zustand["computer_karten"].append(neue_karte_computer)
        blackjack_zustand["computer_punkte"] = sum(k["wert"] for k in blackjack_zustand["computer_karten"])
        gegner_nachricht = f"Der Computer zieht eine Karte ({neue_karte_computer['name']})."
        
        if blackjack_zustand["computer_punkte"] > 21:
            blackjack_zustand["spiel_aktiv"] = False
            return jsonify({
                "spieler_karten": [c["name"] for c in blackjack_zustand["spieler_karten"]],
                "spieler_punkte": blackjack_zustand["spieler_punkte"],
                "computer_karten": [c["name"] for c in blackjack_zustand["computer_karten"]],
                "computer_punkte": blackjack_zustand["computer_punkte"],
                "ergebnis": f"Gewonnen! Der Computer hat sich mit {blackjack_zustand['computer_punkte']} Punkten überkauft.",
                "status": "win"
            })
            
    return jsonify({
        "spieler_karten": [c["name"] for c in blackjack_zustand["spieler_karten"]],
        "spieler_punkte": blackjack_zustand["spieler_punkte"],
        "computer_karten": [c["name"] for c in blackjack_zustand["computer_karten"]],
        "computer_punkte": blackjack_zustand["computer_punkte"],
        "ergebnis": f"Du ziehst {neue_karte_spieler['name']}. {gegner_nachricht}",
        "status": "running"
    })

@mini_casino.route("/blackjack/stopp", methods=["GET"])
def blackjack_stopp():
    if not blackjack_zustand["spiel_aktiv"]:
        return jsonify({"ergebnis": "Kein aktives Spiel!", "status": "inactive"})
    
    while blackjack_zustand["computer_punkte"] < 17:
        neue_karte = random.choice(KARTEN_DECK)
        blackjack_zustand["computer_karten"].append(neue_karte)
        blackjack_zustand["computer_punkte"] = sum(k["wert"] for k in blackjack_zustand["computer_karten"])
        
        if blackjack_zustand["computer_punkte"] > 21:
            blackjack_zustand["spiel_aktiv"] = False
            return jsonify({
                "computer_karten": [c["name"] for c in blackjack_zustand["computer_karten"]],
                "computer_punkte": blackjack_zustand["computer_punkte"],
                "ergebnis": f"Gewonnen! Der Computer hat sich mit {blackjack_zustand['computer_punkte']} Punkten überkauft.",
                "status": "win"
            })
            
    blackjack_zustand["spiel_aktiv"] = False
    p_score = blackjack_zustand["spieler_punkte"]
    c_score = blackjack_zustand["computer_punkte"]
    
    if p_score > c_score:
        msg = f"Gewonnen! Du hast {p_score} Punkte, der Computer hat {c_score}."
    elif c_score > p_score:
        msg = f"Verloren! Der Computer gewinnt mit {c_score} gegen deine {p_score} Punkte."
    else:
        msg = f"Unentschieden! Beide haben {p_score} Punkte."
        
    return jsonify({
        "computer_karten": [c["name"] for c in blackjack_zustand["computer_karten"]],
        "computer_punkte": c_score,
        "ergebnis": msg,
        "status": "ended"
    })

if __name__ == "__main__":
    mini_casino.run()
