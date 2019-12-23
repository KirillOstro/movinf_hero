import pygame
import os

pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

all_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


creature_image = load_image('creature.png')
creature_image = pygame.transform.scale(creature_image, (30, 30))
creature = pygame.sprite.Sprite(all_sprites)
creature.image = creature_image
creature.rect = creature.image.get_rect()
creature.rect.topleft = 0, 0
delta = 10

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_DOWN]:
            creature.rect.top += delta
        if keys[pygame.K_UP]:
            creature.rect.top -= delta
        if keys[pygame.K_LEFT]:
            creature.rect.left -= delta
        if keys[pygame.K_RIGHT]:
            creature.rect.left += delta
    screen.fill(pygame.Color('white'))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

