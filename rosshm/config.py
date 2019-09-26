# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from configparser import ConfigParser, ExtendedInterpolation
from os import getenv, path

__all__ = ['init', 'get', 'getbool']

_cfg = ConfigParser(
	delimiters = ('=',),
	comment_prefixes = ('#', ';'),
	default_section = 'default',
	allow_no_value = False,
	strict = False,
	interpolation = ExtendedInterpolation(),
	defaults = {
		'debug': False,
		'log.level': 'warn',
		'core.enable': True,
		'web.enable': True,
	},
)

def init(fn = None):
	if fn is None:
		fn = getenv('ROSSHM_CONFIG',
			path.expanduser(path.join('~', '.config', 'rosshm.ini')))
	with open(fn, 'r') as fh:
		_cfg.read_file(fh)
	if not _cfg.has_section('rosshm'):
		_cfg.add_section('rosshm')

def get(option, **kwargs):
	return _cfg.get('rosshm', option, **kwargs)

def getbool(option, **kwargs):
	return _cfg.getboolean('rosshm', option, **kwargs)
