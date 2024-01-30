# Hier bauen wir ein, dass die Spieler nichtmehr oben/unten das Fenster verlassen koennen

import pygame
pygame.init()
clock = pygame.time.Clock()

WEISS   = (255,255,255)
SCHWARZ = (  0,  0,  0)
ROT     = (255,  0,  0)
GRUEN   = (  0,255,  0)
BLAU    = (  0,  0,255)

SpielerABild = pygame.image.load("spieler_a.png")
SpielerBBild = pygame.image.load("spieler_b.png")
KugelBild    = pygame.image.load("kugel.png")
Hintergrund  = pygame.image.load("hintergrund.png")

# Zuerst muessen wir die Sound Effekte aehnlich wie die Bilder laden
TorSound     = pygame.mixer.Sound("tor.wav")
HitSound     = pygame.mixer.Sound("hit.wav")
RandHitSound = pygame.mixer.Sound("borderHit.wav")

# Musik muss ein wenig anders geladen werden,
Musik        = pygame.mixer.music.load("bgm.mp3")
# Hiermit spielen wir sie ab, -1 bedeutet das die Musik in einer Endlosschleife wiederholt wird
pygame.mixer.music.play(-1)

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
SchriftGroesse    = 24

font = pygame.font.SysFont(None, SchriftGroesse)

window = pygame.display.set_mode([FensterBreite, FensterHoehe])
running = True
while running:
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
            if (BallXGeschwindigkeit > 0):
                pygame.mixer.Sound.play(HitSound)
                BallXGeschwindigkeit *= BallAbprallFaktor

    if (BallX > SpielerAX - BallRadius) and (BallX < SpielerAX + SpielerBreite + BallRadius):
        if (BallY > SpielerAY - BallRadius) and (BallY < SpielerAY + SpielerHoehe + BallRadius):
            if (BallXGeschwindigkeit < 0):
                pygame.mixer.Sound.play(HitSound)
                BallXGeschwindigkeit *= BallAbprallFaktor

    if (BallY < BallRadius):
        # Wenn der obere Rand beruehrt wird wollen wir den Effekt abspielen
        pygame.mixer.Sound.play(RandHitSound)
        BallYGeschwindigkeit *= BallAbprallFaktor
    if (BallY > FensterHoehe - BallRadius):
        # Beim unteren ebenso
        pygame.mixer.Sound.play(RandHitSound)
        BallYGeschwindigkeit *= BallAbprallFaktor

    if (BallX < -BallRadius) or (BallX > FensterBreite + BallRadius):
        # Wenn der Ball vom Spieler abprallt nehmen wir einen anderen, ein wenig fetzigeren Effekt
        pygame.mixer.Sound.play(TorSound)
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

    if SpielerAY < 0:
        SpielerAY = 0
    if SpielerAY > FensterHoehe - SpielerHoehe:
        SpielerAY = FensterHoehe - SpielerHoehe

    if SpielerBY < 0:
        SpielerBY = 0
    if SpielerBY > FensterHoehe - SpielerHoehe:
        SpielerBY = FensterHoehe - SpielerHoehe

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

