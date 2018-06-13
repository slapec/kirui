# coding: utf-8

from pathlib import Path
from typing import List

from django.contrib.staticfiles.finders import FileSystemFinder


def find_components(*roots: str) -> List[str]:
    components = []

    for root in roots:
        root_components = []
        for path in Path(root).glob('*'):  # type: Path
            if path.is_dir():
                root_components.append(str(path))
        components.extend(sorted(root_components))

    return components


class BundleFinder(FileSystemFinder):
    def find(self, path: str, all=False):
        return super().find(path.split('/', 1)[1])

    def list(self, ignore_patterns):
        return []
