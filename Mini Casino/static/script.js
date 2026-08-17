let knopfRaten = document.querySelector("#knopf_raten");
let knopfRoulette = document.querySelector("#knopf_roulette");
let knopfMuenzwurf = document.querySelector("#knopf_muenzwurf");

let ergebnisRaten = document.querySelector("#ergebnis_raten");
let ergebnisRoulette = document.querySelector("#ergebnis_roulette");
let ergebnisMuenzwurf = document.querySelector("#ergebnis_muenzwurf");

const INTERNET_ADRESSE = "http://127.0.0.1:5000";

if (knopfRaten) {
    knopfRaten.addEventListener("click", function() {
        let wert = document.querySelector("#tipp_raten").value;
        fetch(`${INTERNET_ADRESSE}/zahlenraten?tipp=${wert}`)
            .then(res => res.json())
            .then(data => {
                ergebnisRaten.innerText = data.ergebnis;
            });
    });
}

if (knopfRoulette) {
    knopfRoulette.addEventListener("click", function() {
        let zahl = document.querySelector("#tipp_roulette_zahl").value;
        let farbe = document.querySelector("#tipp_roulette_farbe").value;
        fetch(`${INTERNET_ADRESSE}/roulette?zahl=${zahl}&farbe=${farbe}`)
            .then(res => res.json())
            .then(data => {
                ergebnisRoulette.innerText = data.ergebnis;
            });
    });
}

if (knopfMuenzwurf) {
    knopfMuenzwurf.addEventListener("click", function() {
        let tipp = document.querySelector("#tipp_muenzwurf").value;
        fetch(`${INTERNET_ADRESSE}/muenzwurf?tipp=${tipp}`)
            .then(res => res.json())
            .then(data => {
                ergebnisMuenzwurf.innerText = data.ergebnis;
            });
    });
}

let knopfBlackjackStart = document.querySelector("#knopf_bj_start");
let knopfBlackjackZiehen = document.querySelector("#knopf_bj_ziehen");
let knopfBlackjackStopp = document.querySelector("#knopf_bj_stopp");

let kartenSpieler = document.querySelector("#bj_spieler_karten");
let punkteSpieler = document.querySelector("#bj_spieler_punkte");
let kartenGegner = document.querySelector("#bj_gegner_karten");
let punkteGegner = document.querySelector("#bj_gegner_punkte");
let ergebnisBlackjack = document.querySelector("#ergebnis_blackjack");

if (knopfBlackjackStart) {
    knopfBlackjackStart.addEventListener("click", function() {
        fetch(`${INTERNET_ADRESSE}/blackjack/start`)
            .then(res => res.json())
            .then(data => {
                kartenSpieler.innerText = "Deine Karten: " + data.spieler_karten.join(", ");
                punkteSpieler.innerText = "Deine Punkte: " + data.spieler_punkte;
                kartenGegner.innerText = "Computer-Karten: " + data.computer_karten.join(", ");
                punkteGegner.innerText = "Computer-Punkte: " + data.computer_punkte;
                ergebnisBlackjack.innerText = "Spiel gestartet! Du bist am Zug.";
                
                knopfBlackjackZiehen.disabled = false;
                knopfBlackjackStopp.disabled = false;
            });
    });
}

if (knopfBlackjackZiehen) {
    knopfBlackjackZiehen.addEventListener("click", function() {
        fetch(`${INTERNET_ADRESSE}/blackjack/ziehen`)
            .then(res => res.json())
            .then(data => {
                kartenSpieler.innerText = "Deine Karten: " + data.spieler_karten.join(", ");
                punkteSpieler.innerText = "Deine Punkte: " + data.spieler_punkte;
                if (data.computer_karten) {
                    kartenGegner.innerText = "Computer-Karten: " + data.computer_karten.join(", ");
                    punkteGegner.innerText = "Computer-Punkte: " + data.computer_punkte;
                }
                
                ergebnisBlackjack.innerText = data.ergebnis || "Karte gezogen!";
                
                if (data.status === "bust" || data.status === "win") {
                    knopfBlackjackZiehen.disabled = true;
                    knopfBlackjackStopp.disabled = true;
                }
            });
    });
}

if (knopfBlackjackStopp) {
    knopfBlackjackStopp.addEventListener("click", function() {
        fetch(`${INTERNET_ADRESSE}/blackjack/stopp`)
            .then(res => res.json())
            .then(data => {
                kartenGegner.innerText = "Computer-Karten: " + data.computer_karten.join(", ");
                punkteGegner.innerText = "Computer-Punkte: " + data.computer_punkte;
                ergebnisBlackjack.innerText = data.ergebnis;
                
                knopfBlackjackZiehen.disabled = true;
                knopfBlackjackStopp.disabled = true;
            });
    });
}
