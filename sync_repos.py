import json
import os
import os.path
import subprocess
import sys

from xdg.BaseDirectory import xdg_config_home

supported_repo_types = ['hg', 'git', 'svn']


def execute_cmd(*args):
    return subprocess.call(args, stdout=sys.stdout, stderr=sys.stderr)


def main():
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
            os.chdir(item['dir'])
            print('%s >>> %s' % (repo_type, item['dir']))
            if repo_type == 'hg':
                execute_cmd('hg', 'pull', '-u')
            elif repo_type == 'git':
                execute_cmd('git', 'pull')
            elif repo_type == 'svn':
                execute_cmd('svn', 'update')
            else:
                print('unknown')
