# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from configparser import ConfigParser, ExtendedInterpolation
from os import getenv, path

__all__ = ['init', 'filename', 'get', 'getbool']

def _new():
	"""create a new configuration parser"""
	return ConfigParser(
	delimiters = ('=',),
	comment_prefixes = ('#', ';'),
	default_section = 'default',
	allow_no_value = False,
	strict = False,
	interpolation = ExtendedInterpolation(),
	defaults = {
		'debug': False,
		'datadir': path.join(path.expanduser('~'), '.local', 'rosshm'),
		'log.level': 'warn',
		'core.enable': True,
		'db.driver': 'sqlite',
		'db.name': 'rosshmdb',
		'db.config': '',
		'static.enable': True,
		'web.enable': True,
	},
)
_cfg = _new()

_cfgfn = getenv('ROSSHM_CONFIG', '')
if _cfgfn == '':
	_cfgfn = path.join(path.expanduser('~'), '.config', 'rosshm.ini')

def init(fn = None):
	"""initialize configuration from filename"""
	global _cfgfn
	if fn is None:
		fn = _cfgfn
	fn = path.abspath(fn)
	if path.isfile(fn):
		with open(fn, 'r') as fh:
			_cfg.read_file(fh)
	_cfgfn = fn
	if not _cfg.has_section('rosshm'):
		_cfg.add_section('rosshm')

def filename():
	"""return configuration read filename"""
	global _cfgfn
	return _cfgfn

def database():
	"""return an option:key dict with parsed database configuration"""
	cfg = {}
	for k, v in _cfg.items('rosshm'):
		if k.startswith('db.'):
			opt = k.replace('db.', '', 1)
			cfg[opt] = v
	drv = get('db.driver')
	name = get('db.name')
	cfgfn = get('db.config')
	if cfgfn != '':
		cfgfn = path.abspath(path.expanduser(cfgfn))
	cfg.update({
		'driver': drv,
		'name': name,
		'config': cfgfn,
	})
	if drv == 'sqlite' and not name.startswith(':memory:'):
		cfg['name'] = path.abspath(path.join(get('datadir'), f"{name}.{drv}"))
	return cfg

def get(option, default = None):
	"""get option value (string)"""
	return _cfg.get('rosshm', option, fallback = default)

def getbool(option, default = None):
	"""get option boolean value"""
	return _cfg.getboolean('rosshm', option, fallback = default)
