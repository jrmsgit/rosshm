# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import MySQLdb

from rosshm import log
from rosshm.db import sql
from rosshm.db.lang.mysql import MySQLLang

Error = MySQLdb.OperationalError
IntegrityError = MySQLdb.IntegrityError

def connect(cfg):
	log.debug('connect')
	sql.setLang(MySQLLang())
	return MySQLdb.connect(
		host            = cfg.get('host'    , 'localhost'),
		db              = cfg.get('name'    , 'rosshmdb'),
		user            = cfg.get('user'    , 'rosshm'),
		passwd          = cfg.get('password', None),
		connect_timeout = cfg.get('timeout' , 60),
		charset         = cfg.get('charset' , 'utf8'),
		use_unicode     = True,
	)