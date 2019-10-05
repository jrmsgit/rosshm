# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.lang.base import BaseLang

class MySQLLang(BaseLang):
	name = 'mysql'
	paramstyle = None # set at connect time
