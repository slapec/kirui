# coding: utf-8

import logging
from pathlib import Path
from distutils.dir_util import copy_tree
from typing import List

from webassets import Bundle
from webassets import Environment
from webassets.script import CommandLineEnvironment

IN_ROOT = './'
OUT_ROOT = Path('kirui/static/kirui')

log = logging.getLogger('webassets')


def out(filename):
    return str(OUT_ROOT / filename)


def find_js(root: str) -> List[str]:
    paths = []

    for child in Path(root).glob('*'):
        if child.is_dir():
            js_path = child / 'js'  # type: Path

            if js_path.exists():
                paths.extend(list(str(_) for _ in js_path.glob('*.js')))

    return sorted(paths)


def copy_static(*roots: str):
    log.info('Copying static files')

    for root in roots:
        for child in Path(IN_ROOT, root).glob('*'):  # type: Path
            if child.is_dir():
                font_dir = child / 'font'
                img_dir = child / 'img'

                if font_dir.exists():
                    target = str(Path(OUT_ROOT, 'font'))
                    copy_tree(str(font_dir), target)
                    log.debug('{0} -> {1}'.format(font_dir, target))
                elif img_dir.exists():
                    target = str(Path(OUT_ROOT, 'img'))
                    copy_tree(str(img_dir), target)
                    log.debug('{0} -> {1}'.format(img_dir, target))


env = Environment(
    directory=IN_ROOT,
    url='./static'
)

env.register('vendor_js', Bundle(
    *find_js('vendor'),
    filters='jsmin',
    output=out('js/vendor.js')
))

env.register('kirui_js', Bundle(
    *find_js('components'),
    filters='jsmin',
    output=out('js/kirui.js')
))

env.register('kirui_css', Bundle(
    'components/bundle.scss',
    filters=('libsass', 'cssmin'),
    output=out('css/kirui.css')
))


def bundle():
    # Setup a logger
    log.addHandler(logging.StreamHandler())
    log.setLevel(logging.DEBUG)

    cmdenv = CommandLineEnvironment(env, log)
    cmdenv.build()

    copy_static('vendor', 'components')


if __name__ == '__main__':
    bundle()
