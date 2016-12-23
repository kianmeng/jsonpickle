#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

extensions = [
    'sphinx.ext.autodoc',
    'rst.linker',
]

# General information about the project.

root = os.path.join(os.path.dirname(__file__), '..')
setup_script = os.path.join(root, 'setup.py')
dist_info_cmd = [sys.executable, setup_script, '--name', '--version', '--url']
output_bytes = subprocess.check_output(dist_info_cmd, cwd=root)
project, version, url = output_bytes.decode('utf-8').split()

copyright = '2016 Jason R. Coombs'

# The full version, including alpha/beta/rc tags.
release = version

master_doc = 'index'

link_files = {
	'../CHANGES.rst': dict(
		using=dict(
			GH='https://github.com',
			project=project,
			url=url,
		),
		replace=[
			dict(
				pattern=r"(Issue )?#(?P<issue>\d+)",
				url='{url}/issues/{issue}',
			),
			dict(
				pattern=r"^(?m)((?P<scm_version>v?\d+(\.\d+){1,2}))\n[-=]+\n",
				with_scm="{text}\n{rev[timestamp]:%d %b %Y}\n",
			),
		],
	),
}