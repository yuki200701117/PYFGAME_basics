import pygame #載入PYGAME

pygame.init() #啟動
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH)) #產生畫布
pygame.display.set_caption("My first game!")


BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN   = (0, 255, 255)
MEG    = (255, 0, 255)
GRAY   = (236, 223, 238)

displayscreen.fill(GRAY) #填滿畫布背景
#pygame.draw.line(畫布名稱, color, start, end, thickness)
pygame.draw.line(displayscreen, RED, (0, WINDOW_HEIGHT//2), (WINDOW_WIDTH, WINDOW_HEIGHT//2), 5)
pygame.draw.line(displayscreen, RED, (WINDOW_WIDTH//2, 0), (WINDOW_WIDTH//2, WINDOW_HEIGHT), 5)

#pygame.draw.cirlce(畫布名稱，顏色，中心點,半徑, thickness) thickness=0(填滿), 1,2...10線條寬度
pygame.draw.circle(displayscreen, CYAN, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(displayscreen, CYAN, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 180, 6)


#pygame.draw.rect(畫布名稱，顏色, topleft-x, topleft-y, width, height)
pygame.draw.rect(displayscreen, BLUE, (0, 0, WINDOW_WIDTH, 100), 0)

running = True
while running:
    for event in pygame.event.get(): #抓取畫布上的所有事件
        #print(event)
        if event.type == pygame.QUIT:#事件的type==QUIT(按下結束建)
            running = False
            
        pygame.display.update() #畫布更新

pygame.quit() #結束