# Jetzt fuegen wir den Ball hinzu welche von den Spielern und den Raendern abprallt

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

# Zuerst ein paar neue Konstanten
BallXStartGeschwindigkeit = 2
BallYStartGeschwindigkeit = 1.2
BallRadius                = 8
BallAbprallFaktor         = -1.1

# Und auch noch ein paar Variabeln
BallX = FensterBreite/2
BallY = FensterHoehe/2
BallXGeschwindigkeit = BallXStartGeschwindigkeit
BallYGeschwindigkeit = BallYStartGeschwindigkeit

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
    # Jetzt muessen wir noch den Ball Malen
    BallPosition = (BallX, BallY)
    pygame.draw.circle(window, ROT, BallPosition, BallRadius)

    pygame.display.flip()
    clock.tick(FPS)

    # Damit sich der Ball bewegt muessen wir die Position jedes mal ein klein wenig veraendern
    BallX += BallXGeschwindigkeit
    BallY += BallYGeschwindigkeit

    # Zuerst schauen wir ob der Ball sich auf der X-Achse innerhalb des rechten Spielers befindet
    if (BallX > SpielerBX) and (BallX < SpielerBX + SpielerBreite):
        # Und jetzt auf der Y-Achse
        if (BallY > SpielerBY) and (BallY < SpielerBY + SpielerHoehe):
            # Wenn der Ball auf beiden Achsen innerhalb des Spielers ist
            # beruehren sich die beiden und der Ball soll abprallen.
            BallXGeschwindigkeit *= BallAbprallFaktor

    # Und jetzt das gleiche fuer den linken Spieler
    if (BallX > SpielerAX) and (BallX < SpielerAX + SpielerBreite):
        if (BallY > SpielerAY) and (BallY < SpielerAY + SpielerHoehe):
            BallXGeschwindigkeit *= BallAbprallFaktor

    # Jetzt schauen wir ob der Ball unten den Rand beruehrt
    if (BallY < 0):
        BallYGeschwindigkeit *= BallAbprallFaktor
    # Und das gleiche fuer den Rand unten
    if (BallY > FensterHoehe):
        BallYGeschwindigkeit *= BallAbprallFaktor

    # Wenn der Ball den linken Rand beruehrt hat der rechte Spieler ein Tor gemacht.
    # Punkte zaehlen wir spaeter, zuerst bewegen wir den Ball nur in die Mitte zurueck.
    if (BallX < 0) or (BallX > FensterBreite):
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

