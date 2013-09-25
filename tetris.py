#!/usr/bin/env python

import pygame
import sys
import os
import time
import random
import itertools
import collections 


def create_L():
    blocks = collections.OrderedDict() 
    coords = [240, 0]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/orange_block.png') 
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 40]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/orange_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[1] += 40
    return blocks
    
def create_J():
    blocks = collections.OrderedDict()
    coords = [280, 0]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/blue_block.png') 
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] -= 40
    coords = [240, 40]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/blue_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[1] += 40
    return blocks

def create_Z():
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

def create_S():
    blocks = collections.OrderedDict()
    coords = [240, 0]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/green_block.png') 
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [200, 40]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/green_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    return blocks

def create_I():
    blocks = collections.OrderedDict()
    coords = [200, 0]
    for i in xrange(4):
        block = pygame.image.load(os.getcwd() + '/images/aqua_block.png') 
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
        block = pygame.image.load(os.getcwd() + '/images/purple_block.png') 
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 40]
    block = pygame.image.load(os.getcwd() + '/images/purple_block.png')
    block.convert_alpha()
    block_rect = block.get_rect()
    block_rect.topleft = coords
    blocks[block] = block_rect
    return blocks

def create_O():
    blocks = collections.OrderedDict()
    coords = [240, 0]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/yellow_block.png') 
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [240, 40]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/yellow_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    return blocks

def row_check(board):
    row_count = collections.Counter()
    for node in board:
        surface = node.keys()[0]
        row_count[node[surface][1]] += 1
    complete_row = [i for i in row_count if row_count[i] == 12]      
    return complete_row

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
        self.line_cnt = 0
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
        self.update_score(0)
    
    def update_board(self, board):
        for node in board:
            surface = node.keys()[0]
            self.screen.blit(surface, node[surface])
        
    def update_score(self, line_amnt):
        if line_amnt:
            self.line_cnt += line_amnt
            self.lines = str(int(self.lines) + line_amnt)
            self.score = str(int(self.score) + (line_amnt * 50))
            if self.line_cnt >= 5:
                self.line_cnt = 0
                self.level = str(int(self.level) + 1)
                self.level = ('0' * (3 - len(self.level))) + self.level
        self.lines = ('0' * (5 - len(self.lines))) + self.lines
        lines_text = self.font.render('Lines: %s' % 
                                      self.lines, True, (0, 255, 0)) 
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
  
    def complete_line(self, line_amnt, board):
        self.update_score(len(line_amnt))
        new_brd = list()
        for node in board:
            surface = node.keys()[0]
            if any(node[surface][1] == i for i in line_amnt):
                self.screen.blit(self.clear_block, node[surface][:2])
            else:
                new_brd.append(node)
        pygame.display.flip()
        board = new_brd
        time.sleep(0.1)
        displaced = list()
        for node in board:
            surface = node.keys()[0]
            if node[surface][1] < max(line_amnt):
                displaced.append(node[surface])
        while all(blk.bottom < 740 for blk in displaced):
            self.screen.blit(self.brd, (40, 20))
            for blk in displaced:            
                blk.move_ip([0, 2.0]) 
            self.update_board(board)
            for node in board:
                surface = node.keys()[0]
                if any(blk.left == node[surface].left and
                       blk.bottom == node[surface].top and
                       node[surface] not in displaced for blk in displaced): 
                    return board
            pygame.display.flip()
        return board

    @property   
    def over(self):
        while True:
            self.screen.blit(self.gameover, (75, 220))
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and
                    event.key == pygame.K_ESCAPE):
                        self.font_file.close()
                        sys.exit()
            pygame.display.flip()

class Tetris(object):

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
                            
        self.levels = {1:[0, 2.0], 2:[0, 2.0], 3:[0, 2.5], 
                       4:[0, 4.0], 5:[0, 5.0], 6:[0, 10.0]}

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
                       
        self.speed = self.levels[self.level]
        
    def new_block(self, block):
        self.block = block 
        position_range = xrange(self.block_types[self.block][1])
        self.positions = itertools.cycle(position_range)
        self.cur_pos = self.positions.next()
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
                self.clear_on_bottom(board)):
            self.blocks = save_block_pos         
        else:
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

    def clear_on_bottom(self, board):
        for node in board:
            for blk in node:
                if any(self.blocks[i].right == node[blk].right and
                       self.blocks[i].top >= node[blk].top and
                       self.blocks[i].top < node[blk].bottom or
                       self.blocks[i].right == node[blk].right and
                       self.blocks[i].bottom > node[blk].top and
                       self.blocks[i].bottom <= node[blk].bottom
                       for i in self.blocks):
                    return False
        return True
        
           
def main():
    cur_brd = list()
    cur_bag = list()
    tetri = ['L', 'J', 'Z', 'S', 'I', 'T', 'O']
    tetri_bags = list(itertools.permutations(tetri))
    game = GameScreen()
    while True:
        level = int(game.level)
        tetris = Tetris(level)
        if not cur_bag:
            cur_bag = list(random.choice(tetri_bags))
        cur_block = cur_bag.pop(0)
        tetris.new_block(cur_block)
        while all(tetris.blocks[i].bottom < 740 for i in tetris.blocks):
            game.update_block(tetris.blocks, cur_brd)
            tetris.overflow_check(cur_brd)
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_LSHIFT):
                    tetris.rotate_block(cur_brd)
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
            else:
                break
        for blk in tetris.blocks:
            cur_brd.append({blk:tetris.blocks[blk]})
        rows = row_check(cur_brd)        
        if rows:
            cur_brd = game.complete_line(rows, cur_brd)
        if tetris.gameover:
            game.over


if __name__ == '__main__':
    main()
