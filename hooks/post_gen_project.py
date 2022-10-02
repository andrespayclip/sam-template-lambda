import subprocess

repository_prefix = 'https://github.com/andrespayclip/'
repository_name = repository_prefix+'{{ cookiecutter.project_name }}.git'


subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'remote', 'add', 'origin', 'repository_name'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])