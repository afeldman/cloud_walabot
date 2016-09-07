#!/usr/bin/env python
# encoding: utf-8
# waf script for builduing project
# author: Anton Feldmann
# Copyright 2014 anton.feldmann@gmail.com
# license: MIT

import os, sys
from waflib import Build, TaskGen

name = 'robcon'

major  = 0
minor  = 1
bugfix = 0

name_version = '%s-%d.%d.%d' % (name, major, minor, bugfix)

application = name
version     = '%d.%d.%d' % (major, minor, bugfix)

top = '.'
out = 'build'

def options(opt):
    opt.load('compiler_cxx boost compiler_c')

    #Add configuration options in python
    walaopt = opt.add_option_group ("%s Options" % name.upper())

    walaopt.add_option('--shared',
                      action='store_true',
                      default=False,
                      help='build all libs as shared libs')
    walaopt.add_option('--clang',
                      action='store_true',
                      default=False,
                      help='build with clang')
    waladebugopt = opt.add_option_group ("%s_Debugging Options" % name.upper())

    daladebugopt.add_option('--debug',
                            action='store_true',
                            default=False,
                            help='compile the project in debug mode')

def configure(conf):
    env=conf.env
    opt=conf.options

    from waflib import Options

    opts = Options.options

    if not os.name == 'nt':
        if(opts.clang):
            env.CXX = 'clang++'
            env.CC = 'clang'


def build(bld):
    bld(features='py',
        source=bld.path.ant_glob('src/walabot/*.py'),
        install_from='.')
