#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
import collections
import os


PATH = os.getcwd()

def create_L():
    blocks = collections.OrderedDict()
    coords = [240, 0]
    for i in xrange(2):
        block = pygame.image.load(PATH + '/images/orange_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 40]
    for i in xrange(2):
        block = pygame.image.load(PATH + '/images/orange_block.png')
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
        block = pygame.image.load(PATH + '/images/blue_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] -= 40
    coords = [240, 40]
    for i in xrange(2):
        block = pygame.image.load(PATH + '/images/blue_block.png')
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
        block = pygame.image.load(PATH + '/images/red_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 40]
    for i in xrange(2):
        block = pygame.image.load(PATH + '/images/red_block.png')
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
        block = pygame.image.load(PATH + '/images/green_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [200, 40]
    for i in xrange(2):
        block = pygame.image.load(PATH + '/images/green_block.png')
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
        block = pygame.image.load(PATH + '/images/aqua_block.png')
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
        block = pygame.image.load(PATH + '/images/purple_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [280, 40]
    block = pygame.image.load(PATH + '/images/purple_block.png')
    block.convert_alpha()
    block_rect = block.get_rect()
    block_rect.topleft = coords
    blocks[block] = block_rect
    return blocks

def create_O():
    blocks = collections.OrderedDict()
    coords = [240, 0]
    for i in xrange(2):
        block = pygame.image.load(PATH + '/images/yellow_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    coords = [240, 40]
    for i in xrange(2):
        block = pygame.image.load(PATH + '/images/yellow_block.png')
        block.convert_alpha()
        block_rect = block.get_rect()
        block_rect.topleft = coords
        blocks[block] = block_rect
        coords[0] += 40
    return blocks
