# python_game
利用pygame module自己創造的小遊戲

1. **參考資料**
    1. Pygame Page: http://pygame.org
    2. documentation: https://pygame.org/docs/ref/
    
    5. ~~XXXX忘記了~~ <br><br><br>
-------


**_2. What is Pygame_**:
  * Pygame提供Display, Sound, Image, Text, Event幫助製作遊戲
  * Pyagme可以做出2-D小遊戲
  * Pygame偵測使用者適用keyboard, joystick, mouse控制遊戲
  * Pygame提供許多內建的game object來製作遊戲<br><br>

**_3.Pygame Basic_**:
 | Code | Description |
 |:-----:|:----------:|
 | _1.py_ | Create my game surface, game loop and draw.|
 | _2.py_ | Blit text, font, sound and image object.   |
 | _3.py_ | Getting user keyboard amd collision dection.|
    
    
 **_4. Code snippet_**
 
 ```python
 #Creat game display
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("feed the angry bird!")


 
 ```
 ```python
 #Blite image object and setting its rec.
player_image = pygame.image.load("angry_bird.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2
displayscreen.blit(player_image, player_rect)

```

**_5. Game Assets_**<br>
[Icon Archive:] (https://iconarchive.com/) 網站提供很多遊戲角色下載<br>
[Leshy SFMaker:] (https://www.leshylabs.com/apps/sfMaker/ )網站可以下載遊戲特效，也可以簡單自己製作音效

   

<img src="https://github.com/yuki200701117/PYFGAME_basics/blob/main/%E6%93%B7%E5%8F%96.PNG"  width="400" height"300" alt="2.py程式截圖"
