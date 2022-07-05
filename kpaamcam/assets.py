from pathlib import Path

from clld.web.assets import environment

import kpaamcam


environment.append_path(
    Path(kpaamcam.__file__).parent.joinpath('static').as_posix(),
    url='/kpaamcam:static/')
environment.load_path = list(reversed(environment.load_path))
