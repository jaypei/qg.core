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


from functools import partial
from qg.core.context.localdef import (
    LocalStack, LocalProxy
)


def _lookup_app_object(name):
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError('working outside of application context')
    return getattr(top, name)


def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError('working outside of application context')
    return top.app


def _lookup_task_object(name):
    app = _find_app()
    task = app._ext_mgr._task_ctx.top
    if task is None:
        raise RuntimeError('working outside of task context')
    return getattr(task, name)


# context locals
_app_ctx_stack = LocalStack()
current_app = LocalProxy(_find_app)
g = LocalProxy(partial(_lookup_app_object, 'g'))
app_ctx = None
task_ctx = LocalProxy(partial(_lookup_task_object, 'g'))
