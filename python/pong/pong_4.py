# Hier fangen wir an die Anzahl der Tore zu zaehlen und zeichen diese in die Ecken Links und Rechts oben

import pygame
pygame.init()
clock = pygame.time.Clock()

FensterBreite  = 640
FensterHoehe   = 480
FPS            = 60
SpielerAbstand = 50
SpielerBreite  = 20
SpielerHoehe   = 100
SpielerGeschwindigkeit = 4

SpielerAY = FensterHoehe/2 - SpielerHoehe/2
SpielerBY = FensterHoehe/2 - SpielerHoehe/2

BallXStartGeschwindigkeit = 2
BallYStartGeschwindigkeit = 1.2
BallRadius                = 8
BallAbprallFaktor         = -1.1

BallX = FensterBreite/2
BallY = FensterHoehe/2
BallXGeschwindigkeit = BallXStartGeschwindigkeit
BallYGeschwindigkeit = BallYStartGeschwindigkeit

# Wir brauchen 2 neue Variablen fuer die Punkte der Spieler
SpielerAPunkte = 0
SpielerBPunkte = 0

# Und noch ein paar Konstanten
PunkteRandAbstand = 16
SchriftGroesse    = 24

# Damit wir die Punktezahlen zeichen koennen muessen wir zuerst einen Font laden
font = pygame.font.SysFont(None, SchriftGroesse)

window = pygame.display.set_mode((FensterBreite, FensterHoehe))
while True:
    SpielerAX = SpielerAbstand
    SpielerBX = FensterBreite - SpielerAbstand - SpielerBreite
    SpielerA  = pygame.Rect(SpielerAX, SpielerAY, SpielerBreite, SpielerHoehe)
    SpielerB  = pygame.Rect(SpielerBX, SpielerBY, SpielerBreite, SpielerHoehe)

    window.fill(pygame.Color('black'))
    pygame.draw.rect(window, pygame.Color( 'blue'), SpielerA)
    pygame.draw.rect(window, pygame.Color('green'), SpielerB)

    BallPosition = (BallX, BallY)
    pygame.draw.circle(window, pygame.Color('red'), BallPosition, BallRadius)

    # Um Text zu zeichnen muessen wir zuerst den Text in ein Bild umwandeln, dies nennt man rendern.
    SpielerAText = font.render(str(SpielerAPunkte), True, pygame.Color('white'))
    # Jetzt koennen wir das Bild vom Text auf den Bildschirm mittels der blit methode zeichnen.
    window.blit(SpielerAText, (PunkteRandAbstand, PunkteRandAbstand))
    # Und nochmal das gleiche fuer SpielerB
    SpielerBText = font.render(str(SpielerBPunkte), True, pygame.Color('white'))
    window.blit(SpielerBText, (FensterBreite - PunkteRandAbstand - 16, PunkteRandAbstand))

    pygame.display.flip()
    clock.tick(FPS)


    BallX += BallXGeschwindigkeit
    BallY += BallYGeschwindigkeit

    if (BallX > SpielerBX) and (BallX < SpielerBX + SpielerBreite):
        if (BallY > SpielerBY) and (BallY < SpielerBY + SpielerHoehe):
            BallXGeschwindigkeit *= BallAbprallFaktor

    if (BallX > SpielerAX) and (BallX < SpielerAX + SpielerBreite):
        if (BallY > SpielerAY) and (BallY < SpielerAY + SpielerHoehe):
            BallXGeschwindigkeit *= BallAbprallFaktor

    if (BallY < 0):
        BallYGeschwindigkeit *= BallAbprallFaktor
    if (BallY > FensterHoehe):
        BallYGeschwindigkeit *= BallAbprallFaktor

    if (BallX < 0) or (BallX > FensterBreite):
        # Hier muessen wir schauen ob der Ball Links oder Rechts aus dem Bildschirm flog
        if (BallX < 0):
            # Wenn der Ball links rausfliegt bedeutet das der rechte Spieler kriegt einen Punkt
            SpielerBPunkte += 1
        else:
            # Und links umgekehrt
            SpielerAPunkte += 1
        BallX = FensterBreite/2
        BallY = FensterHoehe/2
        BallXGeschwindigkeit = BallXStartGeschwindigkeit
        BallYGeschwindigkeit = BallYStartGeschwindigkeit

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        SpielerAY -= SpielerGeschwindigkeit
    if keys[pygame.K_s]:
        SpielerAY += SpielerGeschwindigkeit
    if keys[pygame.K_UP]:
        SpielerBY -= SpielerGeschwindigkeit
    if keys[pygame.K_DOWN]:
        SpielerBY += SpielerGeschwindigkeit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

