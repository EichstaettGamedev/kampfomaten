# Hier bauen wir ersetzen wir die Rechtecke/Kreise durch Bilder, damit das Spiel was schicker ausschaut

import pygame
pygame.init()
clock = pygame.time.Clock()

# Zuerst laden wir alle Bilder die wir brauchen
# WICHTIG! Die Bilder fuer die beiden Spieler muessen gleich gross sein
SpielerABild = pygame.image.load("spieler_a.png")
SpielerBBild = pygame.image.load("spieler_b.png")
KugelBild    = pygame.image.load("kugel.png")
Hintergrund  = pygame.image.load("hintergrund.png")

FensterBreite  = 640
FensterHoehe   = 480
FPS            = 60
SpielerAbstand = 50
# Hier fragen wir ab wie gross das Bild fuer SpielerA ist und nehmen diese als Breite/Hoehe fuer die Spieler
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
SchriftGroesse    = 24

font = pygame.font.SysFont(None, SchriftGroesse)

window = pygame.display.set_mode((FensterBreite, FensterHoehe))
while True:
    SpielerAX = SpielerAbstand
    SpielerBX = FensterBreite - SpielerAbstand - SpielerBreite
    SpielerA  = pygame.Rect(SpielerAX, SpielerAY, SpielerBreite, SpielerHoehe)
    SpielerB  = pygame.Rect(SpielerBX, SpielerBY, SpielerBreite, SpielerHoehe)

    HintergrundPosition = pygame.Rect(0,0,FensterBreite, FensterHoehe)
    window.blit(Hintergrund, HintergrundPosition)
    # Anstelle von draw.rect muessen wir jetzt die blit Methode verwenden.
    # Blit ist kurz fuer Bit blit was das Zeichnen von einen Bild in ein anderes bedeutet
    window.blit(SpielerABild, SpielerA)
    window.blit(SpielerBBild, SpielerB)

    # Auch die Kugel muessen wir per blit zeichnen
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

