# Hier polieren wir das Spiel ein wenig indem wir folgendes einbauen:
# - Mit der Escape Taste kann man das Spiel beenden
# - Der Ball prallt schon ab sobald der Rand/Spieler beruehrt wird, und nicht erst wenn der Mittelpunkt diesen Beruehrt
# - Wir verhindern, dass der Ball in dem Spieler stecken bleiben kann

import pygame
pygame.init()
clock = pygame.time.Clock()

WEISS   = (255,255,255)
SCHWARZ = (  0,  0,  0)
ROT     = (255,  0,  0)
GRUEN   = (  0,255,  0)
BLAU    = (  0,  0,255)

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

SpielerAPunkte = 0
SpielerBPunkte = 0

PunkteRandAbstand = 16
SchriftGroesse    = 24

font = pygame.font.SysFont(None, SchriftGroesse)

window = pygame.display.set_mode([FensterBreite, FensterHoehe])
running = True
while running:
    SpielerAX = SpielerAbstand
    SpielerBX = FensterBreite - SpielerAbstand - SpielerBreite
    SpielerA  = pygame.Rect(SpielerAX, SpielerAY, SpielerBreite, SpielerHoehe)
    SpielerB  = pygame.Rect(SpielerBX, SpielerBY, SpielerBreite, SpielerHoehe)

    window.fill(SCHWARZ)
    pygame.draw.rect(window,  BLAU, SpielerA)
    pygame.draw.rect(window, GRUEN, SpielerB)

    BallPosition = (BallX, BallY)
    pygame.draw.circle(window, ROT, BallPosition, BallRadius)

    SpielerAText = font.render(str(SpielerAPunkte), True, WEISS)
    window.blit(SpielerAText, (PunkteRandAbstand, PunkteRandAbstand))
    SpielerBText = font.render(str(SpielerBPunkte), True, WEISS)
    window.blit(SpielerBText, (FensterBreite - PunkteRandAbstand - 16, PunkteRandAbstand))

    pygame.display.flip()
    clock.tick(FPS)


    BallX += BallXGeschwindigkeit
    BallY += BallYGeschwindigkeit

    if (BallX > SpielerBX - BallRadius) and (BallX < SpielerBX + SpielerBreite + BallRadius):
        if (BallY > SpielerBY - BallRadius) and (BallY < SpielerBY + SpielerHoehe + BallRadius):
            # Der Ball soll nur vom rechten Spieler abprallen wenn er sich nach Rechts bewegt
            # Dadurch verhindern wir auf einfache weise das der Ball stecken bleibt
            if (BallXGeschwindigkeit > 0):
                BallXGeschwindigkeit *= BallAbprallFaktor

    if (BallX > SpielerAX - BallRadius) and (BallX < SpielerAX + SpielerBreite + BallRadius):
        if (BallY > SpielerAY - BallRadius) and (BallY < SpielerAY + SpielerHoehe + BallRadius):
            # Hier das gleiche nur umgekehrt
            if (BallXGeschwindigkeit < 0):
                BallXGeschwindigkeit *= BallAbprallFaktor

    if (BallY < BallRadius):
        BallYGeschwindigkeit *= BallAbprallFaktor
    if (BallY > FensterHoehe - BallRadius):
        BallYGeschwindigkeit *= BallAbprallFaktor

    # Hier muessen wir noch den BallRadius hinzufuegen damit Punkte erst vergeben werden wenn der Ball
    # den Bildschirm komplett verlassen hat
    if (BallX < -BallRadius) or (BallX > FensterBreite + BallRadius):
        if (BallX < BallRadius):
            SpielerBPunkte += 1
        else:
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
            running = False

