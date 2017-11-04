# coding: utf-8

from pathlib import Path
from typing import List


def find_components(*roots: str) -> List[str]:
    components = []

    for root in roots:
        root_components = []
        for path in Path(root).glob('*'):  # type: Path
            if path.is_dir():
                root_components.append(str(path))
        components.extend(sorted(root_components))

    return components
