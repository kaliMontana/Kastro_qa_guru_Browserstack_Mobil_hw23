from pathlib import Path

from browserstack_mobil import utils


def relative_from_root(path: str):
    return (
        Path(utils.__file__)
        .parent.parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
