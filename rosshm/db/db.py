# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from rosshm.db.obj.base import DB
from rosshm.db.obj.status import DBStatus

__all__ = ['Error', 'connect', 'status']

Error = sqlite3.OperationalError

def connect(fn):
	conn = sqlite3.connect(fn)
	conn.row_factory = sqlite3.Row
	return conn

def status(conn):
	s = DBStatus()
	return s.get(conn, 'status', pk = 0)

def create(conn):
	for tbl in DB.tables:
		tbl.create(conn)
	s = DBStatus()
	s.set(conn, pk = 0, status = 'ok')
	conn.commit()
	return {}
