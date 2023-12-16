import pygame,random
from ships import Enemy, Bullet, SpaceShip
from pygame.locals import USEREVENT
import sys

pygame.init()
screen=pygame.display.set_mode((850,640))
running=True
pygame.display.set_caption("Space Invader Game")
pygame.time.set_timer(USEREVENT+1,6000)

black=(0,0,0)
background=pygame.image.load('background.jpg')
score=0
game_over=False
level=1
bullets=20
lives=4

ss=SpaceShip(393,570,'spaceship.png')
all_sprites=pygame.sprite.Group()
all_sprites.add(ss) 
ss_moving=False


enemy_group=pygame.sprite.Group()
ship_bullet_group=pygame.sprite.Group()
enemy_bullet_group=pygame.sprite.Group()
for e in range(3*level):
    col=random.randrange(18,800,32)
    row=random.randrange(134,350,16)
    enemy=Enemy(col,row,"aircraft.png",5)
    enemy_group.add(enemy)

for u in range(2*level):
    col=random.randrange(18,800,32)
    row=random.randrange(34,118,16)
    enemy=Enemy(col,row,"ufo.png",2)
    enemy_group.add(enemy)

clock=pygame.time.Clock()
def check_collision(bullet,enemies):
    return pygame.sprite.spritecollide(bullet,enemies,True)

def GameOver():
    game_over_font=pygame.font.Font(None,72)
    game_over_text=game_over_font.render("Game Over",True,(255,0,0))
    screen.blit(game_over_text,(300,300))
    enemy_group.empty()
    ship_bullet_group.empty()
    all_sprites.empty()
    enemy_bullet_group.empty()
    pygame.display.flip()
    global running
    running=False
    pygame.time.delay(3000)
    

while running:
    screen.blit(background,(0,0))
    live_x=0
    for live in range(lives-1):
        live_img=pygame.image.load('littlespaceship.png').convert_alpha()
        live_x+=20
        live_y=600
        screen.blit(live_img,(live_x,live_y))



    for event in pygame.event.get():
        print(event)
        if  event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
            if event.key==pygame.K_a and 5<ss.rect.x:
                ss.rect.x-=20
            elif event.key==pygame.K_d and ss.rect.x<780:
                print(ss.rect.x)
                ss.rect.x+=20
            elif event.key==pygame.K_SPACE:
                if bullets==0:
                    GameOver()
                bullets-=1
                ship_bullet=Bullet(ss.rect.x+23,ss.rect.y,"s")
                ship_bullet_group.add(ship_bullet)
        elif event.type==USEREVENT+1:
            print("6 saniye oldu")
            enemy_bullet_group.empty()
            for b in range(level*5):
                col=random.randrange(20,795,64)
                row=random.randint(0,20)
                enemy_bullet=Bullet(col,row,"e")
                enemy_bullet_group.add(enemy_bullet)
            
    bullet_font=pygame.font.Font(None,25)
    bullet_text=bullet_font.render(f"Bullets:{bullets}",True,(0,0,0))
    screen.blit(bullet_text,(750,620))
    score_font=pygame.font.Font(None,36)
    score_text=score_font.render(f"Score:{score}",True,(0,0,0))
    screen.blit(score_text,(10,10))
    for ship_bullet in ship_bullet_group:
        if check_collision(ship_bullet,enemy_group):
            print("çarptı")
            ship_bullet_group.remove(ship_bullet)
            score+=1
            bullets+=3
            if enemy_group.__len__()==0:
                level_font=pygame.font.Font(None,46)
                level_text=level_font.render(f"LEVEL {level} COMPLETED",True,(0,0,0))
                screen.blit(level_text,(300,300))
                pygame.display.flip()
                print("düşmanlar öldü")
                level+=1
                enemy_group.empty()
                ship_bullet_group.empty()
                all_sprites.empty()
                enemy_bullet_group.empty()
                pygame.time.delay(2000)
                ss=SpaceShip(393,570,'spaceship.png')
                all_sprites=pygame.sprite.Group()
                all_sprites.add(ss) 
                ss_moving=False
                
                for e in range(3*level):
                    col=random.randrange(18,800,32)
                    row=random.randrange(134,350,16)
                    enemy=Enemy(col,row,"aircraft.png",5)
                    enemy_group.add(enemy)

                for u in range(2*level):
                    col=random.randrange(18,800,32)
                    row=random.randrange(34,118,16)
                    enemy=Enemy(col,row,"ufo.png",2)
                    enemy_group.add(enemy)
                
    enemy_group.update()
    ship_bullet_group.update()
    for enemy_bullet in enemy_bullet_group:
        if pygame.sprite.spritecollide(ss,enemy_bullet_group,True):
            enemy_bullet_group.remove(enemy_bullet)
            lives-=1
            pygame.display.flip()
            enemy_group.empty()
            ship_bullet_group.empty()
            all_sprites.empty()
            enemy_bullet_group.empty()
            pygame.time.delay(2000)
            for e in range(3*level):
                    col=random.randrange(18,800,32)
                    row=random.randrange(134,350,16)
                    enemy=Enemy(col,row,"aircraft.png",5)
                    enemy_group.add(enemy)

            for u in range(2*level):
                col=random.randrange(18,800,32)
                row=random.randrange(34,118,16)
                enemy=Enemy(col,row,"ufo.png",2)
                enemy_group.add(enemy)
            ss=SpaceShip(393,570,'spaceship.png')
            all_sprites=pygame.sprite.Group()
            all_sprites.add(ss) 
            ss_moving=False
            if lives==0:
                GameOver()
            break

    ship_bullet_group.draw(screen)
    enemy_group.draw(screen)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen)
    all_sprites.update()
    all_sprites.draw(screen)
    clock.tick(60)
    pygame.display.flip()        

pygame.quit()