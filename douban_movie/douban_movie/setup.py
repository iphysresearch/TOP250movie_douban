# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='scrapy-mymodule',
	entry_points={
		'scrapy.commands': [
			'crawlallcomment=douban_movie.commands:crawlallcomment',
			'crawlallpeople=douban_movie.commands:crawlallpeople',
			],
		},
	)