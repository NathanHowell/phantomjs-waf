#! /usr/bin/env python
# encoding: utf-8

top = '.'
out = 'build'

def options(opt):
	pass

def configure(conf):
	pass

def build(bld):
	bld.recurse('src')

