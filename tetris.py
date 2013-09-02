#!/usr/bin/env python

import pygame
import sys
import os
import random
import itertools
import collections 


def create_L_left():
    blocks = collections.OrderedDict() 
    coords = [240, 20]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/blue_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 60]
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
    coords = [280, 20]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/yellow_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] -= 40
    coords = [240, 60]
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
    coords = [240, 20]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/red_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 60]
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
    coords = [240, 20]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/purple_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [200, 60]
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
    coords = [200, 20]
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
    coords = [240, 20]
    for i in xrange(3):
        block = pygame.image.load(os.getcwd() + '/images/pink_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 60]
    block = pygame.image.load(os.getcwd() + '/images/pink_block.png')
    block.convert_alpha()
    block_rect = block.get_rect()
    block_rect.topleft = coords
    blocks[block] = block_rect
    return blocks

def create_Box():
    blocks = collections.OrderedDict()
    coords = [240, 20]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/aqua_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [240, 60]
    for i in xrange(2):
        block = pygame.image.load(os.getcwd() + '/images/aqua_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    return blocks

def rotate_block(block, blocks, position):
    shift =  { 'L_left':{0:[[0, 40], [-40, 0], [0, -40], [40, -80]],  
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
    block = shift[block]
    idx = 0
    for blk in blocks:
        blocks[blk][0] += block[position][idx][0]
        blocks[blk][1] += block[position][idx][1]
        idx += 1         
    return blocks

def set_grid():
    h_sq = 0
    brd_arr = list()
    for row in xrange(1, 19):
        brd_arr.append(list())
        h_sq += 40
        w_sq = 60
        for col in xrange(1, 13):
            node = {0:[w_sq, h_sq]}
            brd_arr[row - 1].append(node)
            w_sq += 40
    return brd_arr
    
def overflow_check(board, blocks, speed):
    game_over = False
    for node in board:
        for blk in node:
            if any(blocks[v].left == node[blk].left and 
                   blocks[v].bottom == node[blk].top for v in blocks):
                for b in blocks:
                    if blocks[b].top == 20:
                        game_over = True
                        speed = [0, 0]
                        return speed, game_over
                speed = [0, 0]
                return speed, game_over
    return speed, game_over

def clear_on_left(board, blocks):
    for node in board:
        for blk in node:                
            if any(blocks[i].left == node[blk].right and
                   blocks[i].top >= node[blk].top and
                   blocks[i].top < node[blk].bottom or
                   blocks[i].left == node[blk].right and
                   blocks[i].bottom > node[blk].top and
                   blocks[i].bottom <= node[blk].bottom for i in blocks):
                return False
    return True					               

def clear_on_right(board, blocks):
    for node in board:
        for blk in node:
            if any(blocks[i].right == node[blk].left and
                   blocks[i].top >= node[blk].top and
                   blocks[i].top < node[blk].bottom or
                   blocks[i].right == node[blk].left and
                   blocks[i].bottom > node[blk].top and
                   blocks[i].bottom <= node[blk].bottom for i in blocks):
                return False
    return True
    
def main():
    pygame.init()
    size = width, height = 760, 760
    screen = pygame.display.set_mode((size))
    bg = pygame.image.load(os.getcwd() + '/background.png')
    bg.convert_alpha()
    brd = pygame.image.load(os.getcwd() + '/board.png')
    brd.convert_alpha()
    screen.blit(bg, (0, 0))
    screen.blit(brd, (40, 20)) 
    shapes = {'L_left':[create_L_left, 4], 
              'L_right':[create_L_right, 4],
              'S_left':[create_S_left, 4],              
              'S_right':[create_S_right, 4], 
              'Long':[create_Long, 4], 
              'T':[create_T, 4], 
              'Box':[create_Box, 1]} 
    game_over = False
    cur_brd = list()
    grid = set_grid()
    while not game_over:
        block = random.choice(shapes.keys())
        speed = [0, 2]
        shape_block = shapes[block][0]
        blocks = shape_block()
        positions = itertools.cycle(range(shapes[block][1]))
        cur_pos = positions.next()
        row_count = collections.Counter()
        for node in cur_brd:
            for blk in node:
                row_count[node[blk][1]] += 1
        if any(row_count[i] == 12 for i in row_count):   
            complete_row = [i for i in row_count if row_count[i] == 12]         
            break_speed = [0, 4]
            for node in cur_brd:
                for blk in node:
                    if any(node[blk][1] == i for i in complete_row):
                        del node[blk]
            displaced = list()
            for node in cur_brd:
                for blk in node:
                    if node[blk][1] < max(complete_row):
                        displaced.append(node[blk])
            while all(blk.bottom < 740 for blk in displaced):
                for blk in displaced:            
                    blk.move_ip(break_speed) 
                screen.blit(bg, (0, 0))
                screen.blit(brd, (40, 20))
                for node in cur_brd:
                    for blk in node:
                        screen.blit(blk, node[blk])
                pygame.display.flip()
                for node in cur_brd:
                    for n in node:
                        if any(blk.left == node[n].left and
                               blk.bottom == node[n].top and
                               node[n] not in displaced for blk in displaced): 
                            break_speed = [0, 0]
                            break
                if not break_speed[1]:
                    break
        while all(blocks[i].bottom < 740 for i in blocks):
            screen.blit(bg, (0, 0))
            screen.blit(brd, (40, 20))
            for blk in blocks:
                screen.blit(blk, blocks[blk])
            for node in cur_brd:
                for blk in node: 
    			    screen.blit(blk, node[blk])
            pygame.display.flip()
            speed, game_over = overflow_check(cur_brd, blocks, speed)
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_LSHIFT):
                    # check here or in rotate_blocks for collision with other piece or bottom
                    blocks = rotate_block(block, blocks, cur_pos)
                    cur_pos = positions.next()                    
                    if any(blocks[i].right > 520 for i in blocks):
                        shift = max(blocks[i].right for i in blocks)
                        adj_brd = shift - 520
                        for i in blocks:
                            blocks[i].right -= adj_brd
                    if any(blocks[i].left < 40 for i in blocks):
                        shift = min(blocks[i].left for i in blocks)
                        adj_brd = 40 - shift
                        for i in blocks:
                            blocks[i].left += adj_brd
                if (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_RIGHT and 
                    all(blocks[i].right < 520 for i in blocks) and
                    clear_on_right(cur_brd, blocks)):
                    for blk in blocks:
                        blocks[blk][0] += 40

                if (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_LEFT and 
                    all(blocks[i].left > 40 for i in blocks) and
                    clear_on_left(cur_brd, blocks)):
                    for blk in blocks:
                        blocks[blk][0] -= 40
                if (event.type == pygame.KEYDOWN and 
                    event.key == pygame.K_ESCAPE):
                    sys.exit()
            if speed[1]:
                for i in blocks:
                    blocks[i].move_ip(speed)
            else:
                break
        cur_brd.append(blocks)
        pygame.display.flip()
        while game_over:
            pass

if __name__ == '__main__':
    main()
