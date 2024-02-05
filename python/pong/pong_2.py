# Jetzt erweitern wir das Programm um 2 Spieler welche wir mit W/S und Pfeil Oben/Unten bewegen koennen

import pygame
pygame.init()
# Damit das Spiel auf allen Computern gleich schnell laeuft brauchen wir eine Uhr
clock = pygame.time.Clock()

FensterBreite  = 640
FensterHoehe   = 480
# Zuerst ein paar Konstanten damit die folgenden Formeln klarer werden
FPS            = 60
SpielerAbstand = 50
SpielerBreite  = 20
SpielerHoehe   = 100
SpielerGeschwindigkeit = 4

# Hier speichern wir die Position der beiden Spieler, zu beginn befinden sich beide in der Mitte des Fensters
SpielerAY = FensterHoehe/2 - SpielerHoehe/2
SpielerBY = FensterHoehe/2 - SpielerHoehe/2

window = pygame.display.set_mode((FensterBreite, FensterHoehe))
pygame.display.set_caption('Pong')
while True:
    # Anstelle des Kreises zeichnen wir jetzt 2 Rechtecke, das ist beim Linken Spieler einfach
    SpielerAX = SpielerAbstand

    # Der zweite Spieler ist leider was komplizierter.
    # Wir fangen am rechten Rand an (FensterBreite).
    # Bewegen uns um den Abstand zum Rand nach Links (SpielerAbstand).
    # Und bewegen uns um die Breite des Spielers nach Links (SpielerBreite).
    SpielerBX = FensterBreite - SpielerAbstand - SpielerBreite

    # Jetzt erstellen wir die Rechtecke fuer die beiden Spieler
    SpielerA  = pygame.Rect(SpielerAX, SpielerAY, SpielerBreite, SpielerHoehe)
    SpielerB  = pygame.Rect(SpielerBX, SpielerBY, SpielerBreite, SpielerHoehe)
    # Und zeichen nun den Bildschirm
    window.fill(pygame.Color('black'))
    pygame.draw.rect(window, pygame.Color( 'blue'), SpielerA)
    pygame.draw.rect(window, pygame.Color('green'), SpielerB)

    pygame.display.flip()
    # Hier limitieren wir das Spiel auf 60 Bilder die Sekunde, ansonsten wird das Spiel viel zu schnell sein
    clock.tick(FPS)

    # Nachdem wir alles gezeichnet haben fragen wir pygame nach allen Tasten welche gerade gedrueckt sind
    keys = pygame.key.get_pressed()
    # Wenn W gedrueckt ist soll sich der linke Spieler nach oben bewegen
    if keys[pygame.K_w]:
        SpielerAY -= SpielerGeschwindigkeit
    # Bei S nach unten
    if keys[pygame.K_s]:
        SpielerAY += SpielerGeschwindigkeit
    # Und hier das gleiche fuer den rechten Spieler, zuerst nach Oben
    if keys[pygame.K_UP]:
        SpielerBY -= SpielerGeschwindigkeit
    # Und dann nach unten
    if keys[pygame.K_DOWN]:
        SpielerBY += SpielerGeschwindigkeit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

