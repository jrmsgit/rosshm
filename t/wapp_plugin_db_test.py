# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from rosshm.db.conn import DBConn
from rosshm.db.drv.sqlite import IntegrityError
from rosshm.wapp.plugin.db import DBPlugin

def _new(ctx):
	debug = ctx.wapp.config.getbool('debug')
	dbcfg = ctx.wapp.config.database()
	return DBPlugin(dbcfg, debug)

def test_setup(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx)
		p.setup(ctx.wapp.wapp)
		assert p.name == 'rosshm.db'
		assert p.api == 2

def _callback(db, *args, **kwargs):
	tdata = kwargs.get('tdata', None)
	return {'db': db, 'tdata': tdata}

def test_apply(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx)
		del ctx.callback
		ctx.callback = _callback
		d = p.apply(ctx.callback, ctx.route)(tdata = 'testing')
		assert isinstance(d, dict)
		assert d['tdata'] == 'testing'
		assert isinstance(d['db'], DBConn)

def test_db_integrity_error(testing_wapp_plugin):
	with testing_wapp_plugin() as ctx:
		p = _new(ctx)
		err = IntegrityError('testing')
		ctx.callback.side_effect = err
		with ctx.wapp.error(500, 'database error', err = err):
			p.apply(ctx.callback, ctx.route)()
