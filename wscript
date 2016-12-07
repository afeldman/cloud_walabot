#!/usr/bin/env python
# encoding: utf-8
# waf script for builduing project
# author: Anton Feldmann
# Copyright 2014 anton.feldmann@gmail.com
# license: MIT

import os, sys
from waflib import Build, TaskGen

name = 'libwalabot'

major  = 0
minor  = 1
bugfix = 0

name_version = '%s-%d.%d.%d' % (name, major, minor, bugfix)

application = name
version     = '%d.%d.%d' % (major, minor, bugfix)

top = '.'
out = 'build'

def options(opt):
    opt.load('compiler_cxx compiler_c python')

    #Add configuration options in python
    walaopt = opt.add_option_group ("%s Options" % name.upper())

    walaopt.add_option('--shared',
                      action='store_true',
                      default=False,
                      help='build all libs as shared libs')
    walaopt.add_option('--clang',
                      action='store_true',
                      default=True,
                      help='build with clang')
    waladebugopt = opt.add_option_group ("%s_Debugging Options" % name.upper())
    waladebugopt.add_option('--debug',
                            action='store_true',
                            default=False,
                            help='compile the project in debug mode')

    walascriptopt = opt.add_option_group ("%s_Scripting Options" % name.upper())
    walascriptopt.add_option('--python',
                            action='store_true',
                            default=False,
                            help='compile the project with a python interface')

    walascriptopt.add_option('--lua',
                            action='store_true',
                            default=False,
                            help='compile the project with a lua interface')
def configure(conf):

    env=conf.env
    opt=conf.options

    from waflib import Options

    if not os.name == 'nt':
        if Options.options.clang:
            env.CXX = 'clang++'
            env.CC = 'clang'

    conf.load('compiler_c compiler_cxx')

    conf.load('swig')
    if conf.check_swig_version() < (1, 2, 27):
        conf.fatal('this swig version is too old')

    if Options.options.lua:
        conf.load('lua')

    if Options.options.python:
        conf.load('python')
	conf.check_python_version((2,7,0))
	conf.check_python_headers()


def build(bld):

    bld.install_files('${PREFIX}/include/libwalabot/',
                      bld.path.ant_glob(['include/libwalabot/*.hpp'],
                                        remove=False))

    libwalabot=bld(
        features     = ['cxx'],
        target       = 'libWalabot',
        cxxflags     = ['-Wall','-std=c++11'],
        source       = bld.path.ant_glob(['src/*.cpp']),
        includes     = ['include/libWalabot/'],
        install_path = '${PREFIX}/lib',
        use          = []
    )

    from waflib import Options
    if Options.options.debug:
        libwalabot.cxxflags.append(['-g', '-O0'])
    else:
        libwalabot.cxxflags.append('-O3')

    if Options.options.clang:
        libwalabot.cxxflags.append('-stdlib=libstdc++')

    libwalabot.features.append('cxxshlib' if Options.options.shared else 'cxxstlib')

#    if Options.options.python:


    # process libwalabot.pc.in -> libwalabot.pc - by default it use the task "env" attribute
    pcf = bld(
        features = 'subst',
        source = '%s.pc.in' % name,
        target = '%s.pc' % name,
        install_path = '${PREFIX}/lib/pkgconfig/'
        )

    pcf.env.table.update(
        {'LIBS':'',
         'VERSION': version,
         'NAME': name,
         'PREFIX': '%s' % Options.options.prefix,
         'INCLUDEDIR': 'include/%s' % name}
        )
