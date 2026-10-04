# vidtoolz-text-overlay

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-text-overlay.svg)](https://pypi.org/project/vidtoolz-text-overlay/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-text-overlay?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-text-overlay/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-text-overlay/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-text-overlay/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-text-overlay/blob/main/LICENSE)

Add text overlay on video using ffmpeg

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-text-overlay
```
## Usage

type ``vid otext --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-text-overlay
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
