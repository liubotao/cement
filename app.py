import os
import sys

from cement import App, Controller, ex
from cement.utils import fs

class Base(Controller):
    class Meta:
        label = 'base'

    @ex(help='example sub-command')
    def cmd1(self):
        print('Inside Base.cmd1()')


class Nested(Controller):
    class Meta:
        label = 'nested'
        stacked_on = 'base'
        stacked_type = 'nested'

    @ex(help='example sub-command')
    def cmd1(self):
        app.log.debug('This is a debug message.')
        app.log.info('This is an info message')
        app.log.warning('This is an warning message')
        app.log.error('This is an error message')
        app.log.fatal('This is a fatal message')
        print('Inside Nested.cmd1()')
        print(app.config.get_sections())

class MyApp(App):
    class Meta:
        label = 'myapp'
        handlers = [
            Base,
            Nested,
        ]
        path = os.path.join('.', 'config', '%s%s' % (label, '.conf'))
        print(path)
        config_files = [path]

with MyApp() as app:
    app.run()
