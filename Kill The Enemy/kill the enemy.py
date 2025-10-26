import pgzrun
import random

WIDTH = 1000
HEIGHT = 563
TITLE = "Kill The Enemy"

igris = Actor("igris (2)")
igris.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
beru = Actor("beru (2)")
beru.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
score = 0
gameover = False
time_left = 10
shadows_collected = 0
enemy_hits = 0

def draw():
    screen.clear()
    screen.blit("solo", (0, 0))
    
    if gameover:
        screen.draw.filled_rect(Rect(200, 150, 600, 300), (0, 0, 0, 180))  
        screen.draw.text("GAME OVER", center=(WIDTH/2, 200), fontsize=80, color="blue")
        screen.draw.text(f"Final Score: {score}", center=(WIDTH/2, 280), fontsize=50, color="white")
        screen.draw.text("Press R to Restart", center=(WIDTH/2, 350), fontsize=30, color="green")
        screen.draw.text("Press Q to Quit", center=(WIDTH/2, 400), fontsize=30, color="red")

    else:
        igris.draw()
        beru.draw()
        
        screen.draw.text(f"Score: {score}", (20, 20), fontsize=40, color="red")
        screen.draw.text(f"Time: {time_left}s", (WIDTH-150, 20), fontsize=40, color="green")
        screen.draw.text(f"Iron Hit: {shadows_collected}", (20, 70), fontsize=30, color="orange")
        screen.draw.text(f"beru Hit: {enemy_hits}", (20, 110), fontsize=30, color="purple")

def update():
    global gameover
    
    if not gameover:
    
        igris.x += 2
        beru.y += random.randint(-1, 1)
        
        beru.x += 4
        beru.y += random.randint(-2, 2)
        
      
        if igris.x > WIDTH: igris.x = 0
        if igris.x < 0: igris.x = WIDTH
        if igris.y > HEIGHT: igris.y = 0
        if igris.y < 0: igris.y = HEIGHT
        
        if beru.x > WIDTH: beru.x = 0
        if beru.x < 0: beru.x = WIDTH
        if beru.y > HEIGHT: beru.y = 0
        if beru.y < 0: beru.y = HEIGHT

def on_mouse_down(pos):
    global score, shadows_collected, enemy_hits
    
    if not gameover:
        if igris.collidepoint(pos):
            igris.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
            score += 2
            shadows_collected += 1
            sounds.gun.play()  
            
        elif beru.collidepoint(pos):
            beru.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
            score -= 3
            enemy_hits += 1
            sounds.gun.play()  


def update_time():
    global time_left, gameover
    if not gameover:
        time_left -= 1
        if time_left <= 0:
            gameover = True

def reset_game():
    global score, gameover, time_left, shadows_collected, enemy_hits
    score = 0
    gameover = False
    time_left = 10
    shadows_collected = 0
    enemy_hits = 0
    igris.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
    beru.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))

def on_key_down(key):
    if key == keys.R:
        reset_game()
    if key == keys.Q:
        quit()


clock.schedule_interval(update_time, 1.0)

pgzrun.go()