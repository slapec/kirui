# coding: utf-8

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import call, patch, MagicMock

from django.test import TestCase

from utils.static import find_components, BundleFinder


class FindComponentsTests(TestCase):
    def test_find_components(self):
        with TemporaryDirectory() as tmp_root:
            def d(root, path):
                return tmp_root + '/' + root + '/'+ path

            # A számozás direkt fordított.
            for root in ('2vendor', '1components'):
                # A find_components megfelelő sorrendben kell hogy visszatérjen
                for path in ('4component1', '3component2/css', '2component3/js', '1component4/js'):
                    Path(tmp_root, root, path).mkdir(parents=True, exist_ok=True)
                Path(root, tmp_root, 'file.js').touch()

            components = find_components(
                tmp_root + '/' + '2vendor',
                tmp_root + '/' + '1components'
            )

            self.assertEqual(components, [
                d('2vendor', '1component4'),
                d('2vendor', '2component3'),
                d('2vendor', '3component2'),
                d('2vendor', '4component1'),
                d('1components', '1component4'),
                d('1components', '2component3'),
                d('1components', '3component2'),
                d('1components', '4component1')
            ])


class BundleFinderTests(TestCase):
    def setUp(self):
        self.finder = BundleFinder()

    def test_list(self):
        self.assertEqual(
            list(self.finder.list(None)),
            []
        )

    @patch('django.contrib.staticfiles.finders.FileSystemFinder.find')
    def test_find(self, mock_find: MagicMock):
        self.finder.find('/root/child/file')
        self.finder.find('root/child/file')

        self.assertEqual(mock_find.mock_calls, [
            call('root/child/file'),
            call('child/file')
        ])
