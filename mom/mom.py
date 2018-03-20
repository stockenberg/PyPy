#!/usr/bin/python3
"""PHP File Generator"""
import sys
import os
import errno


class Scaffold:
    """Used to define some scaffolds"""

    @staticmethod
    def class_scaffold():
        """Define Scaffold for Base CLass"""
        return '''<?php
                
namespace {dir};

class {file}{OPEN_BRACKET}

    public function __construct(){OPEN_BRACKET}
        // Do Something
    {CLOSE_BRACKET}

{CLOSE_BRACKET}'''

    @staticmethod
    def database_trait():
        """Define scaffold for Database Class"""
        return '''<?php
 namespace {dir};

class {file}{OPEN_BRACKET}

    protected $db;
    
    public function __construct()
    {OPEN_BRACKET}
        $this->db = new PDO(DSN, DBUSER, DBPASS);
        $this->db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    {CLOSE_BRACKET}
    
    protected function fetch(String $sql, array $executeArray) : array
    {OPEN_BRACKET}
        $stmt = $this->db->prepare($sql);
        $stmt->execute($executeArray);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    {CLOSE_BRACKET}
    
    protected function set(String $sql, array $executeArray) : void
    {OPEN_BRACKET}
        $stmt = $this->db->prepare($sql);
        $stmt->execute($executeArray);
    {CLOSE_BRACKET}

{CLOSE_BRACKET}
        '''


def generate_php_files(file_type):
    """This function generates PHP Files from scaffold class"""
    if file_type == "-pc":
        files = tuple(sys.argv[2:])
        for file in files:

            if len(file.split("/")) > 1:
                if not os.path.exists(os.path.dirname(file)):
                    try:
                        os.makedirs(os.path.dirname(file))
                    except OSError as exc:
                        if exc.errno != errno.EEXIST:
                            raise

            with open(os.getcwd() + "/" + file + ".php", 'w+') as tmp:
                tmp.write(Scaffold.class_scaffold().format(dir="\\".join(file.split("/")[:-1]),
                                                           file=file.split("/")[-1], linebreak="\n",
                                                           OPEN_BRACKET="{", CLOSE_BRACKET="}"))


def help_func():
    """Show help"""
    print('''
    Hello sweetheart, how can i assist you ? 
    
    Arguments:
        -pc   : Creates a PHP Class
        -help  : Shows Help
    ''')


def main():
    """ Main Entry Point straight from command line"""
    if len(sys.argv) >= 2:
        if "-pc" in sys.argv[1]:
            generate_php_files(file_type='-pc')

        if "-help" in sys.argv[1]:
            help_func()

    else:
        help_func()


if __name__ == '__main__':
    main()
