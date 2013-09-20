#!/usr/bin/env python

import pygame
import sys
import os
import time
import random
import itertools
import collections 


def create_L_left():
    blocks = collections.OrderedDict() 
    coords = [240, 0]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/blue_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 40]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/blue_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[1] += 40
    return blocks
    
def create_L_right():
    blocks = collections.OrderedDict()
    coords = [280, 0]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/yellow_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] -= 40
    coords = [240, 40]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/yellow_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[1] += 40
    return blocks

def create_S_left():
    blocks = collections.OrderedDict()
    coords = [240, 0]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/red_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 40]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/red_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40 
    return blocks

def create_S_right():
    blocks = collections.OrderedDict()
    coords = [240, 0]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/purple_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [200, 40]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/purple_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    return blocks

def create_Long():
    blocks = collections.OrderedDict()
    coords = [200, 0]
    for i in xrange(4):
        block = pygame.image.load(os.getcwd() + '/images/green_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    return blocks

def create_T():
    blocks = collections.OrderedDict()
    coords = [240, 0]
    for i in xrange(3):
        block = pygame.image.load(os.getcwd() + '/images/pink_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 40]
    block = pygame.image.load(os.getcwd() + '/images/pink_block.png')
    block.convert_alpha()
    block_rect = block.get_rect()
    block_rect.topleft = coords
    blocks[block] = block_rect
    return blocks

def create_Box():
    blocks = collections.OrderedDict()
    coords = [240, 0]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/aqua_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [240, 40]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/aqua_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    return blocks

class GameScreen(object):
    
    def __init__(self):
        pygame.init()
        size = width, height = 760, 760
        self.screen = pygame.display.set_mode((size))
        self.bg = pygame.image.load(os.getcwd() + '/images/background.png')
        self.bg.convert_alpha()
        self.brd = pygame.image.load(os.getcwd() + '/images/board.png')
        self.brd.convert_alpha()
        self.clear_block = pygame.image.load(os.getcwd() + 
                                             '/images/clear_block.png')
        self.clear_block.convert_alpha()
        self.gameover = pygame.image.load(os.getcwd() + 
                                          '/images/game_over.png')
        self.gameover.convert_alpha()
        self.stats = pygame.image.load(os.getcwd() + '/images/score_board.png')
        self.stats.convert_alpha()
        self.font_file = open(os.getcwd() + '/font/DS-DIGIB.TTF', 'r')
        self.font = pygame.font.Font(self.font_file, 24)
        self.score = '00000'
        self.lines = '00000'
        self.level = '001'
        score_text = self.font.render('Score: %s' % 
                                       self.score, True, (0, 255, 0))
        lines_text = self.font.render('Lines: %s' % 
                                       self.lines, True, (0, 255, 0))
        level_text = self.font.render('Level: %s' % 
                                       self.level, True, (0, 255, 0))
        self.screen.blit(self.brd, (40, 20)) 
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.stats, (540, 20)) 
        self.screen.blit(score_text, (555, 35)) 
        self.screen.blit(lines_text, (555, 95)) 
        self.screen.blit(level_text, (555, 155)) 
        pygame.display.flip()
        
    def update_block(self, blocks, board):
        self.screen.blit(self.brd, (40, 20))
        for blk in blocks:
            self.screen.blit(blk, blocks[blk])
        self.update_board(board)
        self.screen.blit(self.bg, (0, 0))
        self.update_score([])
    
    def update_board(self, board):
        for node in board:
            surface = node.keys()[0]
            self.screen.blit(surface, node[surface])
        
    def update_score(self, line_amnt):
        self.lines = str(int(self.lines) + len(line_amnt))
        self.lines = ('0' * (5 - len(self.lines))) + self.lines
        lines_text = self.font.render('Lines: %s' % 
                                      self.lines, True, (0, 255, 0)) 
        self.score = str(int(self.score) + (len(line_amnt) * 50))
        self.score = ('0' * (5 - len(self.score))) + self.score
        score_text = self.font.render('Score: %s' % 
                                      self.score, True, (0, 255, 0))      
        level_text = self.font.render('Level: %s' %
                                       self.level, True, (0, 255, 0))
        self.screen.blit(self.stats, (540, 20))
        self.screen.blit(score_text, (555, 35))
        self.screen.blit(lines_text, (555, 95))
        self.screen.blit(level_text, (555, 155))
        pygame.display.flip()        
  
    def complete_line(self, line_amnt, board, speed):
        self.update_score(line_amnt)
        break_speed = [0, speed]  # drop speed is affecting max level 
        new_brd = list()
        for node in board:
            surface = node.keys()[0]
            if any(node[surface][1] == i for i in line_amnt):
                self.screen.blit(self.clear_block, node[surface][:2])
            else:
                new_brd.append(node)
        board = new_brd
        pygame.display.flip()
        time.sleep(0.1)

        displaced = list()
        for node in board:
            surface = node.keys()[0]
            if node[surface][1] < max(line_amnt):
                displaced.append(node[surface])
        while all(blk.bottom < 740 for blk in displaced):
            for blk in displaced:            
                blk.move_ip(break_speed) 
            for node in board:
                surface = node.keys()[0]
                self.screen.blit(surface, node[surface])
            for node in board:
                surface = node.keys()[0]
                if any(blk.left == node[surface].left and
                       blk.bottom == node[surface].top and
                       node[surface] not in displaced for blk in displaced): 
                    return board
            pygame.display.flip()
        return board

class Tetris(object):

    def __init__(self, level):
        self.level = level
        self.block_types = {'L_left':[create_L_left, 4], 
                            'L_right':[create_L_right, 4],
                            'S_left':[create_S_left, 4],              
                            'S_right':[create_S_right, 4], 
                            'Long':[create_Long, 4], 
                            'T':[create_T, 4], 
                            'Box':[create_Box, 1]} 
                            
        self.levels = {1:[0, 1.0], 2:[0, 2.0], 3:[0, 3.0], 
                       4:[0, 4.0], 5:[0, 5.0], 6:[0, 6.0]}

        self.shifts =  {'L_left':{0:[[0, 40], [-40, 0], [0, -40], [40, -80]],  
                                  1:[[40, 40], [0, 80], [-40, 40], [-80, 0]], 
                                  2:[[40, -40], [80, 0], [40, 40], [0, 80]], 
                                  3:[[-80, 0], [-40, -40], [0, 0], [40, 40]]},  
                       'L_right':{0:[[-40, 0], [0, 40], [40, 0], [80, -40]], 
                                  1:[[0, 80], [40, 40], [0, 0], [-40, -40]],
                                  2:[[80, -40], [40, -80], [0, -40], [-40, 0]],
                                  3:[[-40, -40], [-80, 0], [-40, 40], [0, 80]]},
                       'S_left':{0:[[0, 80], [-40, 40], [0, 0], [-40, -40]],
                                 1:[[80, -40], [40, 0], [0, -40], [-40, 0]],
                                 2:[[-40, -40], [0, 0], [-40, 40], [0, 80]],
                                 3:[[-40, 0], [0, -40], [40, 0], [80, -40]]},
                       'S_right':{0:[[0, 40], [-40, 0], [80, 40], [40, 0]],  
                                  1:[[0, 0], [-40, 40], [0, -80], [-40, -40]],
                                  2:[[40, 0], [80, 40], [-40, 0], [0, 40]],
                                  3:[[-40, -40], [0, -80], [-40, 40], [0, 0]]},
                       'Long':{0:[[40, 120], [0, 80], [-40, 40], [-80, 0]],
                               1:[[80, -120], [40, -80], [0, -40], [-40, 0]],
                               2:[[-80, 0], [-40, 40], [0, 80], [40, 120]],
                               3:[[-40, 0], [0, -40], [40, -80], [80, -120]]},
                       'T':{0:[[0, 80], [-40, 40], [-80, 0], [0, 0]],
                            1:[[80, 0], [40, 40], [0, 80], [0, 0]],
                            2:[[0, -80], [40, -40], [80, 0], [0, 0]],
                            3:[[-80, 0], [-40, -40], [0, -80], [0, 0]]},
                       'Box':{0:[[0, 0], [0, 0], [0, 0], [0, 0]]}
                 }
                       
        self.speed = self.levels[self.level]
        
    def new_block(self):
        self.block = random.choice(self.block_types.keys())
        position_range = xrange(self.block_types[self.block][1])
        self.positions = itertools.cycle(position_range)
        self.cur_pos = self.positions.next()
        create_block = self.block_types[self.block][0]
        self.blocks = create_block()

    def rotate_block(self):
        shift_amnt = self.shifts[self.block]
        idx = 0
        for blk in self.blocks:
            self.blocks[blk][0] += shift_amnt[self.cur_pos][idx][0]
            self.blocks[blk][1] += shift_amnt[self.cur_pos][idx][1]
            idx += 1         
        self.cur_pos = self.positions.next()  
        
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
        game_over = False
        for node in board:
            for blk in node:
                if any(self.blocks[v].left == node[blk].left and 
                       self.blocks[v].bottom == node[blk].top 
                       for v in self.blocks):
                    for b in self.blocks:
                        if self.blocks[b].top == 20:
                            game_over = True
                            self.speed = [0, 0]
                    self.speed = [0, 0]

    def clear_on_left(self, board):
        for node in board:
            for blk in node:                
                if any(self.blocks[i].left == node[blk].right and
                       self.blocks[i].top >= node[blk].top and
                       self.blocks[i].top < node[blk].bottom or
                       self.blocks[i].left == node[blk].right and
                       self.blocks[i].bottom > node[blk].top and
                       self.blocks[i].bottom <= node[blk].bottom 
                       for i in self.blocks):
                    return False
        return True					               

    def clear_on_right(self, board):
        for node in board:
            for blk in node:
                if any(self.blocks[i].right == node[blk].left and
                       self.blocks[i].top >= node[blk].top and
                       self.blocks[i].top < node[blk].bottom or
                       self.blocks[i].right == node[blk].left and
                       self.blocks[i].bottom > node[blk].top and
                       self.blocks[i].bottom <= node[blk].bottom 
                       for i in self.blocks):
                    return False
        return True
        
    def update(self): 
        pass
        
           
def main():
    game_over = False
    cur_brd = list()
    level = 1
    game = GameScreen()
    while not game_over:
        tetris = Tetris(level)
        tetris.new_block()
        while all(tetris.blocks[i].bottom < 740 for i in tetris.blocks):
            game.update_block(tetris.blocks, cur_brd)
            tetris.overflow_check(cur_brd)
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_LSHIFT):
                    # check here or in rotate_blocks for collision with other piece or bottom
                    tetris.rotate_block()
                    if any(tetris.blocks[i].right > 520 for i in tetris.blocks):
                        tetris.shift_right()
                    if any(tetris.blocks[i].left < 40 for i in tetris.blocks):
                        tetris.shift_left()
                if (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_RIGHT and 
                    all(tetris.blocks[i].right < 520 for i in tetris.blocks) and
                    tetris.clear_on_right(cur_brd)):
                    for blk in tetris.blocks:
                        tetris.blocks[blk][0] += 40
                if (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_LEFT and 
                    all(tetris.blocks[i].left > 40 for i in tetris.blocks) and
                    tetris.clear_on_left(cur_brd)):
                    for blk in tetris.blocks:
                        tetris.blocks[blk][0] -= 40
                if (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_ESCAPE):
                    game.font_file.close()
                    sys.exit()
            if tetris.speed[1]:
                for i in tetris.blocks:
                    tetris.blocks[i].move_ip(tetris.speed)
                    if tetris.blocks[i].bottom > 740:
                        tetris.blocks[i].bottom = 740
                    # this semi works
            else:
                break
            pygame.display.flip()

        for blk in tetris.blocks:
            cur_brd.append({blk:tetris.blocks[blk]})
        row_count = collections.Counter()
        for node in cur_brd:
            for blk in node:
                row_count[node[blk][1]] += 1        

        if any(row_count[i] == 12 for i in row_count):   
            complete_row = [i for i in row_count if row_count[i] == 12]      
            cur_brd = game.complete_line(complete_row, cur_brd, tetris.speed[1])

#        if int(lines) >= 5:
#            level = str(int(level) + 1)
#            level = ('0' * (3 - len(level))) + level
#            level_text = font.render('Level: %s' % level, True, (0, 255, 0))
#            lines = '00000'
#            lines_text = font.render('Lines: %s' % lines, True, (0, 255, 0))
#            cur_brd = list()
#        screen.blit(stats, (540, 20))
#        screen.blit(score_text, (555, 35))
#        screen.blit(lines_text, (555, 95))
#        screen.blit(level_text, (555, 155))
        while game_over:
            screen.blit(gameover, (75, 220))
            pygame.display.flip()
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and
                    event.key == pygame.K_ESCAPE):
                        sys.exit()

if __name__ == '__main__':
    main()
