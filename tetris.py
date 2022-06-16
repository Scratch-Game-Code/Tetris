#!/usr/bin/env python2

import collections 
import itertools
import os
import platform
import pygame
import random
import sys
import time

from lib.tetri_shapes import *
from lib.game_screen import GameScreen

if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'

os.environ['SDL_VIDEO_WINDOW_POS'] = '300, 30'

class Tetri(object):

    def __init__(self, level):
        self.level = level
        self.gameover = False
        self.block_types = {'L':[create_L, 4], 
                            'J':[create_J, 4],
                            'Z':[create_Z, 4],              
                            'S':[create_S, 4], 
                            'I':[create_I, 4], 
                            'T':[create_T, 4], 
                            'O':[create_O, 1]} 
                            
        self.levels = {1:0.1, 2:0.08, 3:0.06, 4:0.04, 5:0.02, 6:0.001}

        self.shifts =  {'L':{0:[[0, 40], [-40, 0], [0, -40], [40, -80]],  
                             1:[[40, 40], [0, 80], [-40, 40], [-80, 0]], 
                             2:[[40, -40], [80, 0], [40, 40], [0, 80]], 
                             3:[[-80, 0], [-40, -40], [0, 0], [40, 40]]},  
                        'J':{0:[[-40, 0], [0, 40], [40, 0], [80, -40]], 
                             1:[[0, 80], [40, 40], [0, 0], [-40, -40]],
                             2:[[80, -40], [40, -80], [0, -40], [-40, 0]],
                             3:[[-40, -40], [-80, 0], [-40, 40], [0, 80]]},
                        'Z':{0:[[0, 80], [-40, 40], [0, 0], [-40, -40]],
                             1:[[80, -40], [40, 0], [0, -40], [-40, 0]],
                             2:[[-40, -40], [0, 0], [-40, 40], [0, 80]],
                             3:[[-40, 0], [0, -40], [40, 0], [80, -40]]},
                        'S':{0:[[0, 40], [-40, 0], [80, 40], [40, 0]],  
                             1:[[0, 0], [-40, 40], [0, -80], [-40, -40]],
                             2:[[40, 0], [80, 40], [-40, 0], [0, 40]],
                             3:[[-40, -40], [0, -80], [-40, 40], [0, 0]]},
                        'I':{0:[[40, 120], [0, 80], [-40, 40], [-80, 0]],
                             1:[[80, -120], [40, -80], [0, -40], [-40, 0]],
                             2:[[-80, 0], [-40, 40], [0, 80], [40, 120]],
                             3:[[-40, 0], [0, -40], [40, -80], [80, -120]]},
                        'T':{0:[[0, 80], [-40, 40], [-80, 0], [0, 0]],
                             1:[[80, 0], [40, 40], [0, 80], [0, 0]],
                             2:[[0, -80], [40, -40], [80, 0], [0, 0]],
                             3:[[-80, 0], [-40, -40], [0, -80], [0, 0]]},
                        'O':{0:[[0, 0], [0, 0], [0, 0], [0, 0]]}
                 }
                       
        self.speed = [0, 10]
        self.level = self.levels[self.level] 
        
    def new_block(self, block):
        self.block = block 
        position_range = range(self.block_types[self.block][1])
        self.positions = itertools.cycle(position_range)
        self.cur_pos = next(self.positions)
        create_block = self.block_types[self.block][0]
        self.blocks = create_block()

    def rotate_block(self, board):
        shift_amnt = self.shifts[self.block]
        idx = 0
        save_block_pos = collections.OrderedDict()
        for surface in self.blocks:
            save_block_pos[surface] = self.blocks[surface].copy()
        for blk in self.blocks:
            self.blocks[blk][0] += shift_amnt[self.cur_pos][idx][0]
            self.blocks[blk][1] += shift_amnt[self.cur_pos][idx][1]
            idx += 1
        if not (self.clear_on_left(board) and 
                self.clear_on_right(board) and 
                self.clear_on_bottom(board) and
                all(self.blocks[i].bottom <= 740 for i in self.blocks)):
            self.blocks = save_block_pos         
        else:
            self.cur_pos = next(self.positions)

    def vertical_clearance(self, cur_brd):
        for node in cur_brd:
            for blk in node:
                if any(self.blocks[v].bottom + self.speed[1] > node[blk].top 
                       for v in self.blocks):
                    self.speed[1] = 10 
                    return
        return

    def lateral_clearance(self, cur_brd):
        if not self.clear_on_right(cur_brd) and self.speed[0] > 0: 
            self.speed[0] -= 40                
        elif not self.clear_on_left(cur_brd) and self.speed[0] < 0:
            self.speed[0] += 40 
        if (self.speed[0] < 0 and 
            any(self.blocks[i].left == 40 for i in self.blocks)):
            self.speed[0] += 40
        elif (self.speed[0] > 0 and 
            any(self.blocks[i].right == 520 for i in self.blocks)):
            self.speed[0] -= 40  
        return
        
    def shift_right(self):
        shift = max(self.blocks[i].right for i in self.blocks)
        adj_brd = shift - 520
        for i in self.blocks:
            self.blocks[i].right -= adj_brd
        
    def shift_left(self):
        shift = min(self.blocks[i].left for i in self.blocks)
        adj_brd = 40 - shift
        for i in self.blocks:
            self.blocks[i].left += adj_brd
    
    def overflow_check(self, board):
        for node in board:
            for blk in node:
                if any(self.blocks[v].left == node[blk].left and 
                       self.blocks[v].bottom == node[blk].top 
                       for v in self.blocks):
                    for b in self.blocks:
                        if self.blocks[b].top <= 20:
                            self.gameover = True
                    self.speed = [0, 0]

    def clear_on_left(self, board): 
        for node in board:
            for blk in node:                
                if any(self.blocks[i].left == node[blk].right and
                       self.blocks[i].top > node[blk].top and 
                       self.blocks[i].top < node[blk].bottom or
                       self.blocks[i].left == node[blk].right and
                       self.blocks[i].bottom > node[blk].top and
                       self.blocks[i].bottom < node[blk].bottom 
                       for i in self.blocks):
                    return False
        return True					               

    def clear_on_right(self, board):
        for node in board:
            for blk in node:
                if any(self.blocks[i].right == node[blk].left and
                       self.blocks[i].top > node[blk].top and 
                       self.blocks[i].top < node[blk].bottom or
                       self.blocks[i].right == node[blk].left and
                       self.blocks[i].bottom > node[blk].top and
                       self.blocks[i].bottom < node[blk].bottom 
                       for i in self.blocks):
                    return False
        return True

    def clear_on_bottom(self, board):
        for node in board:
            for blk in node:
                if any(self.blocks[i].right == node[blk].right and
                       self.blocks[i].top > node[blk].top and
                       self.blocks[i].top < node[blk].bottom or
                       self.blocks[i].right == node[blk].right and
                       self.blocks[i].bottom > node[blk].top and
                       self.blocks[i].bottom < node[blk].bottom   
                       for i in self.blocks):
                    return False
        return True
        

def row_check(board):
    row_count = collections.Counter()
    for node in board:
        surface = list(node.keys())[0]
        row_count[node[surface][1]] += 1
    complete_row = [i for i in row_count if row_count[i] == 12]      
    return complete_row
    
def set_down_speed(blocks):
    position_blk = list(blocks.keys())[0]
    diff = blocks[position_blk].bottom % 10
    for block in blocks:
        blocks[block].bottom -= diff
    return        
           
def main():
    cur_brd = list()
    cur_bag = list()
    tetri_types = ['L', 'J', 'Z', 'S', 'I', 'T', 'O']
    tetri_bags = list(itertools.permutations(tetri_types))
    game = GameScreen()
    while True:
        level = int(game.level)
        tetri = Tetri(level)
        if not cur_bag:
            cur_bag = list(random.choice(tetri_bags))
        cur_block = cur_bag.pop(0)
        tetri.new_block(cur_block)
        while all(tetri.blocks[i].bottom < 740 for i in tetri.blocks):
            time.sleep(tetri.level)
            game.update_block(tetri.blocks, cur_brd)
            tetri.overflow_check(cur_brd)
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and
                    event.key == pygame.K_DOWN):
                    set_down_speed(tetri.blocks)
                    tetri.level /= 2
                elif (event.type == pygame.KEYUP and
                    event.key == pygame.K_DOWN):
                    tetri.level *= 2
                elif (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_LSHIFT):
                    tetri.rotate_block(cur_brd)
                    if any(tetri.blocks[i].right > 520 for i in tetri.blocks):
                        tetri.shift_right()
                    if any(tetri.blocks[i].left < 40 for i in tetri.blocks):
                        tetri.shift_left()
                elif (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_RIGHT and 
                    all(tetri.blocks[i].right < 520 for i in tetri.blocks) and
                    tetri.clear_on_right(cur_brd)):
                    tetri.speed[0] = 40
                elif (event.type == pygame.KEYUP and
                    event.key == pygame.K_RIGHT):
                    tetri.speed[0] = 0
                elif (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_LEFT and 
                    all(tetri.blocks[i].left > 40 for i in tetri.blocks) and
                    tetri.clear_on_left(cur_brd)):
                    tetri.speed[0] = -40
                elif (event.type == pygame.KEYUP and
                    event.key == pygame.K_LEFT):
                    tetri.speed[0] = 0
                elif ((event.type == pygame.KEYDOWN and 
                       event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT):
                    game.font_file.close()
                    sys.exit()
            if tetri.speed[1]:
                tetri.lateral_clearance(cur_brd)
                if tetri.speed[1] == 10:
                    tetri.vertical_clearance(cur_brd)
                for i in tetri.blocks:
                    tetri.blocks[i].move_ip(tetri.speed)
            else:
                break
        cur_brd.extend([{blk:tetri.blocks[blk]} for blk in tetri.blocks])
        rows = row_check(cur_brd)        
        if rows:
            cur_brd = game.complete_line(rows, cur_brd)
        if tetri.gameover:
            game.over


if __name__ == '__main__':
    main()
