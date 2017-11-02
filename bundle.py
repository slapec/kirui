import logging

from webassets import Bundle
from webassets import Environment
from webassets.script import CommandLineEnvironment

env = Environment(
    directory='../components/',
    url='./static')


js = Bundle(
    'jquery/js/jquery.min.js',
    'sidebar/js/sidebar.js',
    filters='jsmin',
    output='static/kirui.js'
)
env.register('js_all', js)

# Setup a logger
log = logging.getLogger('webassets')
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

cmdenv = CommandLineEnvironment(env, log)
cmdenv.build(directory='./static')
