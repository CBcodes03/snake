import pygame
import time
import random

#initialize game attributes
pygame.init()
window_width=500
window_height=500
window=pygame.display.set_mode((window_width,window_height))
snake_block_size=20
snake_speed=10
snake_list=[]
snake_length=1
snake_x=round((window_width / 2)/20)*20
snake_y=round((window_width / 2)/20)*20
snake_x_change=0
snake_y_change=0
#score setting
font_style=pygame.font.SysFont("helvetica",30,0,1)
font_style2=pygame.font.SysFont("helvetica",50,1,1)
#display score
def display_score(score):
    scoretext=font_style.render("Score:"+str(score),1,"black")
    window.blit(scoretext,[0,0])
#gameover
def display_game_over():
    game_over_text=font_style2.render("Game Over!",1,"Black")
    window.blit(game_over_text,(150,225))
    pygame.display.flip()

#setting up food
food_size=20
food_x=round(random.randrange(0,window_width-food_size)/20.0)*20.0
food_y=round(random.randrange(0,window_width-food_size)/20.0)*20.0
#draw snake
def draw_snake(snake_block_size,snake_list):
    for block in snake_list:
        pygame.draw.rect(window,"darkgreen",[block[0],block[1],snake_block_size,snake_block_size])

#game loop
run=True
while run:
    pygame.display.set_caption("Snake Game!")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    snake_x+=snake_x_change
    snake_y+=snake_y_change

    #check if snake eats food....

    if snake_x == food_x and snake_y == food_y:
        food_on_snake=True
        while food_on_snake:
            food_x = round(random.randrange(food_size,window_width-2*food_size)/snake_block_size)*snake_block_size
            food_y = round(random.randrange(food_size,window_height-2*food_size)/snake_block_size)*snake_block_size
            for block in snake_list:
                if block[0] == food_x and block[1] == food_y:
                    food_on_snake = True
                else:
                    food_on_snake = False
        snake_length+=1
    #nake list update
    snake_head=[]
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    #boundaries
    if snake_x<0 or snake_x>=window_width or snake_y < 0 or snake_y >= window_width:
        display_game_over()
        time.sleep(2)
        run = False
    #self coulision
    for block in snake_list[:-1]:
        if block == snake_head:
            display_game_over()
            time.sleep(2)
            run = False
    #user inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and snake_x_change != snake_block_size:
        snake_x_change=-snake_block_size
        snake_y_change=0
    elif keys[pygame.K_d] and snake_x_change != -snake_block_size:
        snake_x_change=snake_block_size
        snake_y_change=0
    elif keys[pygame.K_w] and snake_y_change != snake_block_size:
        snake_x_change=0
        snake_y_change=-snake_block_size
    elif keys[pygame.K_s] and snake_y_change != -snake_block_size:
        snake_x_change=0
        snake_y_change=snake_block_size
    elif keys[pygame.K_q]:
        pygame.quit()



    clock = pygame.time.Clock()
    clock.tick(snake_speed)
#    pygame.time.delay(50)

    window.fill("white")
    pygame.draw.rect(window,"red",[food_x,food_y,food_size,food_size])
    draw_snake(snake_block_size,snake_list)
    display_score(snake_length-1)
    pygame.display.flip()
pygame.quit()
