import argparse
import json
import os
import os.path
import re
import subprocess
import sys

from xdg.BaseDirectory import xdg_config_home

__version__ = '0.0.1rc3'
supported_repo_types = ('hg', 'git', 'svn')


def execute_cmd(*args):
    return subprocess.call(args, stdout=sys.stdout, stderr=sys.stderr)


def main():
    parser = argparse.ArgumentParser(prog='repo-sync')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {:s}'.format(__version__))
    parser.parse_args()

    if xdg_config_home is None or xdg_config_home == '':
        config_dir = os.path.join(os.path.expanduser('~'), '.config')
    else:
        config_dir = xdg_config_home

    conf = None
    with open(os.path.join(config_dir, 'sync-repos.conf'), 'r') as conf_file:
        try:
            conf = json.load(conf_file)
        except ValueError as json_exception:
            print(json_exception, file=sys.stderr)
            sys.exit(1)

    for item in conf:
        repo_type = item['repo-type']
        if repo_type in supported_repo_types:
            dir_ = re.sub(r'\$HOME(?=/|\$|\Z)', os.environ['HOME'],
                          item['dir'])
            os.chdir(dir_)
            print('{:s} >>> {:s}'.format(repo_type, dir_))
            if repo_type == 'hg':
                execute_cmd('hg', 'pull')
            elif repo_type == 'git':
                execute_cmd('git', 'fetch')
            elif repo_type == 'svn':
                execute_cmd('svn', 'update')
            else:
                print('unknown repo type: \"{}\"'.format(repo_type),
                      file=sys.stderr)
