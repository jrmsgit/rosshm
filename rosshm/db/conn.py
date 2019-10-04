# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class DBConn(object):

	def __init__(self, conn):
		self._conn = conn
		self._cur = None
		self._closed = False

	def __del__(self):
		if not self._closed:
			self.close()

	def close(self):
		if self._cur is not None:
			self._cur.close()
		self._conn.close()
		self._closed = True

	def commit(self):
		self._conn.commit()

	def rollback(self):
		self._conn.rollback()

	def execute(self, op, param = None):
		if self._cur is not None:
			self._cur.close()
			del self._cur
		self._cur = self._conn.cursor()
		if param is None:
			self._cur.execute(op)
		else:
			self._cur.execute(op, param)
		return self._cur
