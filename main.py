import pygame, random


#initializing pygame
pygame.init()
clock=pygame.time.Clock()

#Screen setup
screen_width=1000
screen_height=630
screen=pygame.display.set_mode((screen_width,screen_height))


'''1-top platform
2-player
3-ground
4-water
5-tree
6-flower
7-enemy
8-final boss
9-home
10-coins
'''

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 1, 6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 7, 1, 0, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 2, 5, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 6, 1, 1, 1, 3, 1, 1, 0, 10, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 3, 3, 0, 0, 0, 5, 0, 0, 0, 0, 1, 10, 0, 0, 0, 0, 5, 0, 9, 0, 0],
    [3, 3, 3, 3, 1, 1, 0, 6, 0, 0, 7, 6, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 6, 7, 5, 6, 5, 7, 0, 0, 1, 0, 0, 0, 0, 6, 5, 7, 3, 3, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 3, 3, 3, 0, 0, 6, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 0, 0, 0, 6, 1, 3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 6, 0, 1, 1, 1, 3, 3, 1, 1, 0, 5, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 10, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 1, 1, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 1, 1, 3, 3, 3, 3, 3, 3, 3, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3],
]

#images

bg=pygame.image.load("assets/1.png") 
player_Left_Images=[]
player_Right_Images=[]

player_Left_Images.append(pygame.image.load("assets/player/Left/1.png"))
player_Left_Images.append(pygame.image.load("assets/player/Left/2.png"))
player_Left_Images.append(pygame.image.load("assets/player/Left/3.png"))
player_Left_Images.append(pygame.image.load("assets/player/Left/4.png"))
player_Left_Images.append(pygame.image.load("assets/player/Left/5.png"))
player_Left_Images.append(pygame.image.load("assets/player/Left/6.png"))
player_Left_Images.append(pygame.image.load("assets/player/Left/7.png"))
player_Left_Images.append(pygame.image.load("assets/player/Left/8.png"))
player_Left_Images.append(pygame.image.load("assets/player/Left/9.png"))

player_Right_Images.append(pygame.image.load("assets/player/Right/1.png"))
player_Right_Images.append(pygame.image.load("assets/player/Right/2.png"))
player_Right_Images.append(pygame.image.load("assets/player/Right/3.png"))
player_Right_Images.append(pygame.image.load("assets/player/Right/4.png"))
player_Right_Images.append(pygame.image.load("assets/player/Right/5.png"))
player_Right_Images.append(pygame.image.load("assets/player/Right/6.png"))
player_Right_Images.append(pygame.image.load("assets/player/Right/7.png"))
player_Right_Images.append(pygame.image.load("assets/player/Right/8.png"))
player_Right_Images.append(pygame.image.load("assets/player/Right/9.png"))

boss_img_arr=[]

boss_img_arr.append(pygame.image.load("assets/boss/mace1.png"))
boss_img_arr.append(pygame.image.load("assets/boss/mace2.png"))

platform_img=pygame.image.load("assets/platform.png") 
ground_img=pygame.image.load("assets/ground.png") 
water_img=pygame.image.load("assets/water.png") 
tree_img=pygame.image.load("assets/tree2.png") 
enemy_img=pygame.image.load("assets/enemy.png") 
over_img=pygame.image.load("assets/gameover.png") 
bullet_img=pygame.image.load("assets/bullet.png") 
castle_img=pygame.image.load("assets/castle.png") 
win_img=pygame.image.load("assets/win.png") 
coin_img=pygame.image.load("assets/coin.png") 
score_coin_img=pygame.image.load("assets/coin2.png") 
lives_img=pygame.image.load("assets/heart.png") 
reset_img=pygame.image.load("assets/reset.png") 

flower_img1=pygame.image.load("assets/flower1.png")
flower_img2=pygame.image.load("assets/flower2.png")
flower_img3=pygame.image.load("assets/flower3.png") 
flower_list=[flower_img1,flower_img2,flower_img3]

#group containing all sprites
playerGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
platformGroup = pygame.sprite.Group()
waterGroup=pygame.sprite.Group()
bulletGroup=pygame.sprite.Group()
bossGroup=pygame.sprite.Group()
castleGroup=pygame.sprite.Group()
inactiveGroup=pygame.sprite.Group()
coinGroup=pygame.sprite.Group()
worldGroup=pygame.sprite.Group()
# Sprite class

class Sprite(pygame.sprite.Sprite):
    rect=0
    img=0
    def __init__(self,x,y, height, width,img,color):
        super().__init__()
  
        self.image =img  
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    
    
#player class
class Player(pygame.sprite.Sprite):    
    
    def __init__(self,x,y,imgL,imgR):
        super().__init__()
        self.Ani_Index=0
        self.Left_Ani=imgL
        self.Right_Ani=imgR
        self.image =imgL[0]  
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def move(self,dx,dy):
        if self.rect.x+dx<0 or self.rect.x+dx>1000:
            dx=0
        self.rect.x+=dx
        self.rect.y+=dy
        self.animate()
        
    def animate(self):  
        if(dy==0):    
            if dx!=0: 
                self.Ani_Index+=1
            if self.Ani_Index>=len(self.Left_Ani):
               self.Ani_Index=0
        
        if dx>0:
            self.image=self.Left_Ani[self.Ani_Index]
        elif dx<0:
            self.image=self.Right_Ani[self.Ani_Index]

        
#Platform class
class Platform(Sprite):
    xpos=0
    
    def __init__(self,x,y, height, width,img,color):
        super().__init__(x,y, height, width,img,color)
        self.xpos=x
    def move(self,dx):
        self.rect.x=self.xpos - dx        

class Bullet(Platform):   
    def shoot(self):
            self.rect.x+=35 
            
    def move(self,dx):
        pass
        
#Platform class
class Enemy(Platform):
    direction=-2
    count=0
    def walk(self):
        self.xpos+=self.direction
        self.rect.x+=self.direction
        self.count+=1
        if(self.count<90):
            self.direction=-2
        elif(self.count<180):
            self.direction=2
        else:
            self.count=0
            self.direction=-2

class Boss(pygame.sprite.Sprite):
    
    def __init__(self,x,y,imgArr):
        super().__init__()
        self.Ani_Index=0
        self.Ani=imgArr
        self.image =imgArr[0]  
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.velY=-5
        self.xpos=x
    def fly(self):
        if self.rect.y+self.velY<0 or self.rect.y+self.velY>350:
            self.velY*=-1
        self.rect.y+=self.velY
        self.animate()
    
    def move(self,dx):
        self.rect.x=self.xpos - dx          
        
    def animate(self):  
        self.Ani_Index+=0.2
        if self.Ani_Index>=len(self.Ani):
              self.Ani_Index=0
        self.image=self.Ani[int(self.Ani_Index)]
        
class InactiveSprites(pygame.sprite.Sprite):
    xpos=0
    def __init__(self,x,y,img):
        super().__init__()
  
        self.image =img  
        self.rect = self.image.get_rect()
        self.rect.midbottom=[x+70/2,y+70]
        self.xpos=self.rect.x
        
    def move(self,dx):
        self.rect.x=self.xpos-dx
       
player=0
boss=0    
def createGameWorld():
    tile_height=70
    tile_width=70
    global player
    global boss
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==2:
                player=Player(j*tile_width,i*tile_height,player_Left_Images,player_Right_Images)
                playerGroup.add(player)
            elif grid[i][j]==1:
                platform=Platform(j*tile_width,i*tile_height,20,20,platform_img,(200,130,0))
                platformGroup.add(platform)
                worldGroup.add(platform)
            elif grid[i][j]==3:
                platform=Platform(j*tile_width,i*tile_height,20,20,ground_img,(200,130,0))
                platformGroup.add(platform)
                worldGroup.add(platform)
            elif grid[i][j]==4:
                water=Platform(j*tile_width,i*tile_height,20,20,water_img,(200,130,0))
                waterGroup.add(water)
                worldGroup.add(water)
            elif grid[i][j]==5:
                tree=InactiveSprites(j*tile_width,i*tile_height,tree_img)
                inactiveGroup.add(tree)
                worldGroup.add(tree)
            elif grid[i][j]==6:
                choice=random.randint(0, 2)
                flower=InactiveSprites(j*tile_width,i*tile_height,flower_list[choice])
                inactiveGroup.add(flower)
                worldGroup.add(flower)
            elif grid[i][j]==7:
                enemy=Enemy(j*tile_width,i*tile_height,20,20,enemy_img,(200,130,0))
                enemyGroup.add(enemy)
                worldGroup.add(enemy)
            elif grid[i][j]==8:
                boss=Boss(j*tile_width,i*tile_height,boss_img_arr)
                bossGroup.add(boss)
                worldGroup.add(boss)
            elif grid[i][j]==9:
                castle=Platform(j*tile_width-100,i*tile_height-150,20,20,castle_img,(200,130,0))
                castleGroup.add(castle)
                worldGroup.add(castle)
            elif grid[i][j]==10:
                coin=Platform(j*tile_width,i*tile_height,20,20,coin_img,(200,130,0))
                coinGroup.add(coin)
                worldGroup.add(coin)

createGameWorld()    
        
#fonts
score_font=pygame.font.Font('freesansbold.ttf', 25)
over_font=pygame.font.Font('freesansbold.ttf', 25)
        
dx=0
dy=0
gravity=1
camera=0
gameState="play"
canJump=False
score=0
lives=3

while True:    
    screen.fill((37,49,52))
    screen.blit(bg,[0-camera/3,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx=-5
            if event.key == pygame.K_RIGHT:
                dx=5
            if event.key == pygame.K_UP and canJump:
                dy=-18
                canJump=False
            if event.key == pygame.K_SPACE:
                bullet=Bullet(player.rect.x,player.rect.y+30,10,10,bullet_img,(0,0,0))
                bulletGroup.add(bullet)
                worldGroup.add(bullet)
            if event.key == pygame.K_r:
               if gameState=="over":
                    player.rect.x=20
                    player.rect.y=20               
                    gameState="play"      
               if gameState=="end":     
                    camera=0
                    lives=3
                    score=0
                    for p in  worldGroup:
                        p.kill()
                    for p in  playerGroup:
                        p.kill()
                    createGameWorld()  
                    gameState="play"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx=0
            if event.key == pygame.K_RIGHT:
                dx=0
    
    if gameState=="play":
        
        dy+=gravity
    
    
        #check for collision of player with platforms if the player move by dx or dy
        for p in platformGroup:
            p=p.rect
            plr=player.rect
            #check for collision in x direction
            if p.colliderect(plr.x + dx, plr.y, plr.width, plr.height):
                dx = 0
            #check for collision in y direction
            if p.colliderect(plr.x, plr.y + dy, plr.width, plr.height):
                #check if below the ground i.e. jumping
                if dy < 0:
                    dy = p.bottom - plr.top
                    
                elif dy > 0: #check if above the ground i.e. falling
                    dy = p.top - plr.bottom
                    canJump=True
                    
    
        
        #moving game world according to player position     
        if camera<4025:   
            if player.rect.x+dx>200 or (camera>0 and dx<0) :
               camera+=dx 
               player.rect.x-=dx
               for p in  worldGroup:
                   p.move(camera)
    
        
        #making player,bullet and the enemy move
        player.move(dx,dy)
        for enemy in enemyGroup:
            enemy.walk()
        for bullet in bulletGroup:
            bullet.shoot()
        boss.fly()   
            
        pygame.sprite.groupcollide(bulletGroup,enemyGroup,True,True)
        pygame.sprite.groupcollide(bulletGroup,bossGroup,True,True)
        coin_collected=pygame.sprite.groupcollide(playerGroup,coinGroup,False,True)
        if coin_collected:
            score+=10
        
        bullet_kill=pygame.sprite.groupcollide(bulletGroup,platformGroup,True,False) 
        player_kill= pygame.sprite.spritecollideany(player,enemyGroup)
        player_kill_boss= pygame.sprite.spritecollideany(player,bossGroup)
        
        if  player_kill or player_kill_boss or player.rect.y>640:
            lives=lives-1
            if(lives==0):
                gameState="end"
            else:    
                gameState="over"
        
        win = pygame.sprite.spritecollideany(player,castleGroup)
        if win:
            player.rect.x=840
            player.rect.y=365
            gameState="win"
            
        
    inactiveGroup.draw(screen)
    waterGroup.draw(screen)
    platformGroup.draw(screen)
    enemyGroup.draw(screen)
    bulletGroup.draw(screen)
    castleGroup.draw(screen)
    bossGroup.draw(screen)
    coinGroup.draw(screen)
    playerGroup.draw(screen)
    
    score_text=score_font.render("x "+str(score), False, (140,140,200))   
    screen.blit(score_text,[110+camera/1000,45]) 
    screen.blit(score_coin_img,[50+camera/1000,25])
    
    lives_text=score_font.render("x "+str(lives), False, (140,140,200))  
    screen.blit(lives_text,[910+camera/1000,45]) 
    screen.blit(lives_img,[850+camera/1000,25])
        
    if gameState=="over":
        player.move(0,1000)
        screen.blit(reset_img,[350+camera/1000,190])
        lives_text=score_font.render(str(lives), False, (205,205,0))
        screen.blit(lives_text,[480+camera/1000,305]) 
    if gameState=="win":
        screen.blit(win_img,[350+camera/1000,190])
        
    if gameState=="end":
        player.move(0,1000)
        screen.blit(over_img,[350+camera/1000,190])
        
    pygame.display.update()
    clock.tick(30)