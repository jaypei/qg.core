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

from testtools import TestCase
from testtools.matchers import Equals

from qg.core.app import QApplication
from qg.core import context
import qg.test.mocks


class AppCtxTestCase(TestCase):

    def test_app1_run(self):
        def fun_test_app_name():
            self.assertThat(context.current_app.name, Equals("app193901"))

        def fun_set_v():
            context.g.a1 = "hello"

        def fun_test_v():
            self.assertThat(context.g.a1, Equals("hello"))

        class App1(QApplication):
            name = "app193901"
            version = "1.0"

            def run(self):
                fun_test_app_name()
                fun_set_v()
                fun_test_v()

        app1 = App1()
        with qg.test.mocks.mock_cli_options("test"):
            app1.main()

    def test_outside_app_ctx(self):
        self.assertRaises(RuntimeError, context.current_app)
        self.assertRaises(RuntimeError, context.g)
