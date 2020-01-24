# benchbuild.projects

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This includes a set of projects curated by benchbuild that serves as reference implementation for projects in benchbuild.

## Projects:

## Installation

benchbuild.projects is available via PyPI. You can install the latest release with pip.
```bash
# Global install
$ pip install benchbuild.projects
# Local install
$ pip install --user benchbuild.projects
```

```bash
# Recommended: Install into a virutalenv.
$ virtualenv benchbuild
...
$ source benchbuild/bin/activate
...
$ pip install benchbuild.projects
```

Make sure you specify the projects you want to load in benchbuild's configuration. The environment variable is named:
``BB_PLUGINS_PROJECTS``. Please refer to benchbuild's configuration dump for details.
