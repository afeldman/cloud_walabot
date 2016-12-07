#!/usr/bin/env python
# encoding: utf-8
# waf script for builduing project
# author: Anton Feldmann
# Copyright 2014 anton.feldmann@gmail.com
# license: MIT

import os, sys
from waflib import Build, TaskGen

name = 'walabot'

major  = 0
minor  = 1
bugfix = 0

name_version = '%s-%d.%d.%d' % (name, major, minor, bugfix)

application = name
version     = '%d.%d.%d' % (major, minor, bugfix)

top = '.'
out = 'build'

def options(opt):
    opt.load('compiler_cxx compiler_c swig lua java ruby python')

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
    waladebugopt.add_option('--scripting',
                            action='store_true',
                            default=True,
                            help='compile the project with the scripting interface')

def configure(conf):

    env=conf.env
    opt=conf.options

    from waflib import Options

    if not os.name == 'nt':
        if Options.options.clang:
            env.CXX = 'clang++'
            env.CC = 'clang'

    conf.load('compiler_cxx compiler_c')

    if Options.options.scripting:
        conf.load('lua ruby swig java python')

        #check python version
        conf.check_python_version((2,7,0))
        conf.check_python_headers()

        # check for ruby
        conf.check_ruby_version((1,8,0))
        conf.check_ruby_ext_devel()

def build(bld):

    bld.install_files('${PREFIX}/include/libwalabot/',
                      bld.path.ant_glob(['include/libwalabot/*.hpp'],
                                        remove=False))

    libwalabot=bld(
        features     = ['cxx'],
        target       = name,
        cxxflags     = ['-Wall','-std=c++11'],
        source       = bld.path.ant_glob(['src/*.cpp']),
        includes     = ['include/libWalabot/'],
        install_path = '${PREFIX}/lib',
        vnum         = version,
        use          = []
    )

    from waflib import Options
    if Options.options.debug:
        libwalabot.cxxflags.append(['-g', '-O0'])
    else:
        libwalabot.cxxflags.append('-O3')

    if Options.options.clang:
        libwalabot.cxxflags.append('-stdlib=libstdc++')

    libwalabot.features.append('cxxshlib' if (Options.options.shared or Options.options.scripting) else 'cxxstlib')

    # use swig_flags = '-c++ -python -debug-classes' for debugging


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
