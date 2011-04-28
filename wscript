#! /usr/bin/env python
# encoding: utf-8

top = '.'
out = 'build'

def options(opt):
	opt.recurse('src')

def configure(conf):
	conf.recurse('src')

def build(bld):
	bld.recurse('src')

