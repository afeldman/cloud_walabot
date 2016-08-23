top = '.'

def options(opt):
    opt.load('python')

def configure(conf):
    conf.load('python')
    conf.check_python_version((2,7,0))

    try:
        conf.check_python_module('azure')
    except:
        print('python module azure missing')

    try:
        conf.check_python_module('socket')
    except:
        print('python module socket missing')

    try:
        conf.check_python_module('sys')
    except:
        print('python module sys missing')

    try:
        conf.check_python_module('WalabotAPI')
    except:
        print('python module WalabotAPI missing')

    try:
        conf.check_python_module('json')
    except:
        print('python module json missing')
'''
def build(bld):
    bld(features='py',
        source=bld.path.ant_glob('src/**.py'),
        install_from='.')
'''