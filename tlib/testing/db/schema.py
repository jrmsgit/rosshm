# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.obj import DBObject

class DBTesting(DBObject):
	table = 'testing'
	schema = {
		0: {
			'option': (str, {'size': 32}),
			'value': (str, {}),
		}
	}