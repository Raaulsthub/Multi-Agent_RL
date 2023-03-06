import pygame
import numpy as np
import pandas as pd
import gym

RENDER_WIDTH = 800
RENDER_HEIGHT = 800
RADIUS = 20

class Shooter:
    def __init__(self, radius, color, team, hp, x, y):
        self.radius = radius
        self.color = color
        self.team = team
        self.hp = hp
        self.x = x
        self.y = y
        

class multiAgentFPS(gym.Env):
    def __init__(self):
        self.action_space = gym.spaces.MultiBinary(6) # for now, only forward
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(4,))

        # render
        self.screen = pygame.display.set_mode((800, 800))

        # initial state

        # players, initial positions
        self.players = []
        # team zero
        self.players.append(Shooter(RADIUS, (255, 0, 0), 0, 2, 50, RENDER_HEIGHT - 50))
        self.players.append(Shooter(RADIUS, (0, 255, 0), 0, 2, 100, RENDER_HEIGHT - 50))
        self.players.append(Shooter(RADIUS, (0, 0, 255), 0, 2, 150, RENDER_HEIGHT - 50))
        # team one
        self.players.append(Shooter(RADIUS, (255, 255, 0), 1, 2, RENDER_WIDTH - 50, 50))
        self.players.append(Shooter(RADIUS, (255, 0, 255), 1, 2, RENDER_WIDTH - 100, 50))
        self.players.append(Shooter(RADIUS, (0, 255, 255), 1, 2, RENDER_WIDTH - 150, 50))

        # environment objects
        self.objects = []
        self.objects.append(pygame.Rect(RENDER_WIDTH - 275, 100, 200, 30)) # upper right rect
        self.objects.append(pygame.Rect(75, RENDER_HEIGHT - 130, 200, 30)) # lower left
        self.objects.append(pygame.Rect(250, 375, 300, 50)) # central rect
        self.objects.append(pygame.Rect(150, 150, 100, 100)) # upper left square
        self.objects.append(pygame.Rect(RENDER_WIDTH - 250, RENDER_HEIGHT - 250, 100, 100)) # lower right square
 

    def reset(self):
        # team1 initial positions
        self.players[0].x = 50
        self.players[0].y = RENDER_HEIGHT - 50
        self.players[1].x = 100
        self.players[1].y = RENDER_HEIGHT - 50
        self.players[2].x = 150
        self.players[2].y = RENDER_HEIGHT - 50
        # team2 initial positions
        self.players[3].x = RENDER_WIDTH - 50
        self.players[3].y = 50
        self.players[4].x = RENDER_WIDTH - 100
        self.players[4].y = 50
        self.players[5].x = RENDER_WIDTH - 150
        self.players[5].y = 50
        pass

    def step(self, action):
        i = 0
        for j in action:
            print(j)
            if j == True:
                self.players[i].y -= 1
            i += 0

        reward = 0
        done = False
        next_state = None
        return next_state, reward, done, {}
    
    def render(self, mode='human'):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        self.screen.fill((150, 150, 150))

        for i in self.players:
            pygame.draw.circle(self.screen, i.color, (i.x, i.y), i.radius)   
        for i in self.objects:
            pygame.draw.rect(self.screen, (0, 0, 0), i)

        pygame.display.flip()
        return True

    def close(self):
        pygame.quit()
        

def main():
    env = multiAgentFPS()
    closed = False
    while ~closed:
        closed = env.render()
    env.close()

if __name__ == '__main__':
    main()