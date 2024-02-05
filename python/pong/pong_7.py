# Hier bauen wir ein das die Spieler nichtmehr oben/unten das Fenster verlassen koennen

import pygame
pygame.init()
clock = pygame.time.Clock()

SpielerABild = pygame.image.load("spieler_a.png")
SpielerBBild = pygame.image.load("spieler_b.png")
KugelBild    = pygame.image.load("kugel.png")
Hintergrund  = pygame.image.load("hintergrund.png")

FensterBreite  = 640
FensterHoehe   = 480
FPS            = 60
SpielerAbstand = 50

SpielerABildRect = SpielerABild.get_rect()
SpielerBreite  = SpielerABildRect.width
SpielerHoehe   = SpielerABildRect.height
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
SchriftGroesse    = 48

font = pygame.font.SysFont(None, SchriftGroesse)

window = pygame.display.set_mode((FensterBreite, FensterHoehe))
pygame.display.set_caption('Pong')
while True:
    SpielerAX = SpielerAbstand
    SpielerBX = FensterBreite - SpielerAbstand - SpielerBreite
    SpielerA  = pygame.Rect(SpielerAX, SpielerAY, SpielerBreite, SpielerHoehe)
    SpielerB  = pygame.Rect(SpielerBX, SpielerBY, SpielerBreite, SpielerHoehe)

    HintergrundPosition = pygame.Rect(0,0,FensterBreite, FensterHoehe)
    window.blit(Hintergrund, HintergrundPosition)
    window.blit(SpielerABild, SpielerA)
    window.blit(SpielerBBild, SpielerB)

    KugelPosition = pygame.Rect(BallX - BallRadius, BallY - BallRadius, BallRadius * 2, BallRadius * 2)
    window.blit(KugelBild, KugelPosition)

    SpielerAText = font.render(str(SpielerAPunkte), True, pygame.Color('white'))
    window.blit(SpielerAText, (PunkteRandAbstand, PunkteRandAbstand))
    SpielerBText = font.render(str(SpielerBPunkte), True, pygame.Color('white'))
    window.blit(SpielerBText, (FensterBreite - PunkteRandAbstand - 16, PunkteRandAbstand))

    pygame.display.flip()
    clock.tick(FPS)


    BallX += BallXGeschwindigkeit
    BallY += BallYGeschwindigkeit

    if (BallX > SpielerBX - BallRadius) and (BallX < SpielerBX + SpielerBreite + BallRadius):
        if (BallY > SpielerBY - BallRadius) and (BallY < SpielerBY + SpielerHoehe + BallRadius):
            if (BallXGeschwindigkeit > 0):
                BallXGeschwindigkeit *= BallAbprallFaktor

    if (BallX > SpielerAX - BallRadius) and (BallX < SpielerAX + SpielerBreite + BallRadius):
        if (BallY > SpielerAY - BallRadius) and (BallY < SpielerAY + SpielerHoehe + BallRadius):
            if (BallXGeschwindigkeit < 0):
                BallXGeschwindigkeit *= BallAbprallFaktor

    if (BallY < BallRadius):
        BallYGeschwindigkeit *= BallAbprallFaktor
    if (BallY > FensterHoehe - BallRadius):
        BallYGeschwindigkeit *= BallAbprallFaktor

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

    # Zuerst schauen wir ob SpielerA oben das Fenster verlassen hat und bewegen ihn dann an den oberen Rand
    if SpielerAY < 0:
        SpielerAY = 0
    # Und jetzt das gleiche fuer den unteren Rand
    if SpielerAY > FensterHoehe - SpielerHoehe:
        SpielerAY = FensterHoehe - SpielerHoehe

    # Und nochmal das gleiche fuer SpielerB
    if SpielerBY < 0:
        SpielerBY = 0
    if SpielerBY > FensterHoehe - SpielerHoehe:
        SpielerBY = FensterHoehe - SpielerHoehe

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

