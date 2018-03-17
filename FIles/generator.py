#!/usr/bin/python3

import sys
import os
import errno

# TODO : no namespace if no subfolder...


def class_scaffold():
    return '''<?php
            
namespace {dir};

class {file}{OPEN_BRACKET}

    public function __construct(){OPEN_BRACKET}
        // Do Something
    {CLOSE_BRACKET}

{CLOSE_BRACKET}'''


def generate_php_files():

    files = tuple(sys.argv[2:])
    for file in files:

        if len(file.split("/")) > 1:
            if not os.path.exists(os.path.dirname(file)):
                try:
                    os.makedirs(os.path.dirname(file))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise

        x = open(os.getcwd() + "/" + file + ".php", 'w+')
        x.write(class_scaffold().format(dir="\\".join(
                file.split("/")[:-1]),
                file=file.split("/")[-1],
                linebreak="\n",
                OPEN_BRACKET="{",
                CLOSE_BRACKET="}"))

        x.close()


def help_func():
    print('''
    Hello sweetheart, how can i assist you ? 
    
    Arguments:
        -php   : Creates a PHP Class
        -help  : Shows Help
    ''')


if len(sys.argv) >= 2:
    if "-php" in sys.argv[1]:
        generate_php_files()
    elif "-help" in sys.argv[1]:
        help_func()
else:
    help_func()
