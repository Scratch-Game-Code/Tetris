#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import pygame
import collections
import os
import sys


class GameScreen(object):
    
    def __init__(self):
        pygame.init()
        path = os.getcwd()
        size = width, height = 760, 760
        self.screen = pygame.display.set_mode((size))
        self.bg = pygame.image.load(path + '/images/background.png')
        self.bg.convert_alpha()
        self.brd = pygame.image.load(path + '/images/board.png')
        self.brd.convert_alpha()
        self.clear_block = pygame.image.load(path +
                                             '/images/clear_block.png')
        self.clear_block.convert_alpha()
        self.gameover = pygame.image.load(path +
                                          '/images/game_over.png')
        self.gameover.convert_alpha()
        self.stats = pygame.image.load(path + '/images/score_board.png')
        self.stats.convert_alpha()
        self.font_file = open(path + '/font/DS-DIGIB.TTF', 'r')
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
            surface = list(node.keys())[0]
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
            surface = list(node.keys())[0]
            if any(node[surface][1] == i for i in line_amnt):
                self.screen.blit(self.clear_block, node[surface][:2])
            else:
                new_brd.append(node)
        pygame.display.flip()
        board = new_brd
        time.sleep(0.1)
        displaced = dict()
        for node in board:
            surface = list(node.keys())[0]
            if node[surface][1] < max(line_amnt):
                displaced[surface] = node[surface]
        while displaced:
            self.screen.blit(self.brd, (40, 20))
            displaced = self.displace_blocks(displaced, board)
            for blk in displaced:
                displaced[blk].move_ip([0, 2.0])
            self.update_board(board)
            pygame.display.flip()
        return board

    def displace_blocks(self, dpl, board):
        stop_blk = dict()
        for node in board:
            surface = list(node.keys())[0]
            for blk in dpl:
                if (dpl[blk].bottom >= 740 or
                    dpl[blk].left == node[surface].left and
                    dpl[blk].bottom == node[surface].top and
                    surface not in dpl or
                    dpl[blk].left == node[surface].left and
                    dpl[blk].bottom == node[surface].top and
                    surface in stop_blk):
                    for stop in dpl:
                        if dpl[stop].bottom == dpl[blk].bottom:
                            stop_blk[stop] = dpl[stop]
        for blk in stop_blk:
            del dpl[blk]
        return dpl

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
