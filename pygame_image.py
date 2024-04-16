import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)                #練習7-1
    koukaton_img = pg.image.load("fig/3.png")                     #練習2
    koukaton_img = pg.transform.flip(koukaton_img,True,False)
    koukaton_rct = koukaton_img.get_rect()           #練習8-1(こうかとんのRectを抽出)
    koukaton_rct.center = 300,200                    #練習8-2(中心座標の設定)
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()


        x=0
        y=0

        if key_lst[pg.K_UP]:
            y=1
        elif key_lst[pg.K_DOWN]:
            y=-1
        elif key_lst[pg.K_LEFT]:
            x=-1
        elif key_lst[pg.K_RIGHT]:
            x=3
        
        koukaton_rct.move_ip(x-1,y)

        
        

        x = tmr % 3200    
        screen.blit(bg_img, [-x, 0])                #練習6
        screen.blit(bg_img2,[-x+1600,0])            #練習7-1
        screen.blit(bg_img, [-x+3200, 0])           #練習7-2
        screen.blit(bg_img2,[-x+4800,0])            #練習7-2
        screen.blit(koukaton_img, koukaton_rct)       #練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200)   #練習6




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()