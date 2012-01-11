#!/usr/bin/python
# -*- coding: utf-8 -*-



class Screen:
	SCREEN = (650, 650)
	L_SCREEN = range(70, 580)

class Background:
	icon = 'Img/star_2.png'
	background_img = 'Img/bg_4.png'
	black_img = 'Img/black.png'
	back_img = 'Img/back.png'

class Sprites:
	dt_star_1 = ['Img/star_1.png', -2, 28, [0.0008, 2, 4]]
	dt_star_2 = ['Img/star_2.png', 2, 28, [0.0008, 2, 2.8]]
	dt_fly = [[0.0003, 2, 3.3], ['Img/fly_1.png', 'Img/fly_3.png']]
	arrow_img = 'Img/arrow.png'
	lives_img = 'Img/live_4.png'
	heart_img = 'Img/live_3.png'
	bug_img = 'Img/Bug/body_2.png'
	dt_legs =	[[1, 'Img/Bug/f_l.png', (-4, -9)], 
				[2, 'Img/Bug/f_r.png', (4, -9)],
				[3, 'Img/Bug/m_l.png', (-9, -7)],
				[4, 'Img/Bug/m_r.png', (9, -7)],
				[5, 'Img/Bug/b_l.png', (-4, 10.5), -12],
				[6, 'Img/Bug/b_r.png', (4, 10.5), 12]]
	dt_feeler =		[[1, 'Img/Bug/fuehler_l.png', (11, 4.5)],
					[2, 'Img/Bug/fuehler_r.png', (-8.5, 10.5)]]

class Snd:
	arrow_snd = 'Snd/arrow.wav'
	bug_snd = 'Snd/bug.wav'
	fall_snd = 'Snd/fall.wav'
	final_snd = 'Snd/final.wav'
	get_snd = 'Snd/get.wav'

class Color:
	grew_2 = (160, 160, 140)
	color_7 = (55, 150, 250)
	color_8 = (235, 182, 37)
	colors = [color_7, color_8]

class Txt:
	font = 'Fnt/FreeMono.ttf'
	sz_poem = 21
	sz_menu = 19
	sz_big = 47

	ka_txt = 'Kafkahoi'
	mo_txt = 'Mouseclick to start'
	d_txt = 'D'
	di_txt = 'ificulty:'
	s_txt = 'S'
	so_txt = 'ound:'
	p_txt = 'P'
	po_txt = 'oem:'
	e_txt = 'E'
	ed_txt = 'ditor'
	snd_txt = ['aus', 'ein']

