# Zuerst einmal schauen wir nur das wir ein Fenster oeffnen und einen Kreis in die Mitte zeichen

# Um pygame benutzen zu koennen muessen wir es zuallererst importieren, falls pygame nicht gefunden wird kannst du es per `pip install pygame` installieren
import pygame
# Jetzt muss es noch initialisiert werden
pygame.init()

# Und noch ein paar Konstanten damit die Formeln verstaendlicher sind
FensterBreite  = 640
FensterHoehe   = 480

# Hier oeffnen wir ein neues Fenster welches 640x480 Pixel gross ist
window = pygame.display.set_mode([FensterBreite, FensterHoehe])

# Dies ist unsere Hauptschleife in der wir konstant das Fenster neu zeichnen und schauen welche Tasten der Spieler drueckt
while True:
    # Zuerst malen wir den Hintergrund
    window.fill(pygame.Color('black'))
    # Dann einen Kreis in die Mitte des Fensters
    pygame.draw.circle(window, pygame.Color('blue'), (FensterBreite/2, FensterHoehe/2), 50)
    # Zum Schluss muessen wir noch flip aufrufen damit wir etwas sehen
    pygame.display.flip()

    # Hier gehen wir in einer Schleife alle Eingaben/Ereignisse ab
    for event in pygame.event.get():
        # Hier pruefen wir die Art des Ereignisses, QUIT bedeutet das der Nutzer das Spiel beenden moechte (z.B. durch Alt-F4 oder klick aufs X oben rechts)
        if event.type == pygame.QUIT:
            # Mit der exit funktion koennen wir das Programm nun sofort beenden
            exit()


# Uebungsaufgaben
# 1. Veraendere das Programm, so dass der Hintergrund Weiss und nicht Schwarz ist
# 2. Male 2 zusaetzliche Kreise, einen oben Links und einen unten Rechts
# 3. Definiere eine neue Farbe, Purpur und benutze diese fuer einen Kreis

# Loesungen fuer die Aufgaben sind weiter unten































# Loesungen fuer die Uebungsaufgaben:
# 1. Hier musst du in Zeile 31 beim window.fill Befehl SCHWARZ durch WEISS ersetzen
#
# 2. Hierfuer musst du vor dem .flip() folgende Zeilen hinzufuegen:
#    pygame.draw.circle(window, BLAU, (                FensterBreite/4,                FensterHoehe/4), 50)
#    pygame.draw.circle(window, BLAU, (FensterBreite - FensterBreite/4, FensterHoehe - FensterHoehe/4), 50)
#
# 3. Zuerst definieren wir Purpur durch folgende Zeile welche z.B. nach der definition von BLAU kommt
#    PURPUR = (255,  0,255)
#    Danach dann bei einem pygame.draw.circle Befehl BLAU durch PURPUR ersetzen