# -*- coding: utf-8 -*-
#
# Copyright 2013, Qunar OPSDEV
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# Author: jaypei <jaypei97159@gmail.com>
#

from qg.core.context.globals import _app_ctx_stack
from qg.core.context.localdef import LocalStack


class _AppCtxGlobals(object):
    """A plain object."""

    def get(self, name, default=None):
        return self.__dict__.get(name, default)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __repr__(self):
        top = _app_ctx_stack.top
        if top is not None:
            return '<qg.core.context of %r>' % top.app.name
        return object.__repr__(self)


class QApplicationContext(object):

    def __init__(self, app):
        super(QApplicationContext, self).__init__()
        self.app = app
        self.g = app.app_ctx_globals_class()
        self._task_ctx = LocalStack()

    def __enter__(self):
        return self.enter()

    def __exit__(self, type, value, trace):
        self.exit()

    def enter(self):
        _app_ctx_stack.push(self)
        return self

    def exit(self):
        _app_ctx_stack.pop()
