# deluge-gprc


[![pypi](https://img.shields.io/pypi/v/deluge-gprc.svg)](https://pypi.org/project/deluge-gprc/)
[![python](https://img.shields.io/pypi/pyversions/deluge-gprc.svg)](https://pypi.org/project/deluge-gprc/)
[![Build Status](https://github.com/chrisbc/deluge-gprc/actions/workflows/dev.yml/badge.svg)](https://github.com/chrisbc/deluge-gprc/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/chrisbc/deluge-gprc/branch/main/graphs/badge.svg)](https://codecov.io/github/chrisbc/deluge-gprc)



RPC interface to deluge-card.


* Documentation: <https://chrisbc.github.io/deluge-gprc>
* GitHub: <https://github.com/chrisbc/deluge-gprc>
* PyPI: <https://pypi.org/project/deluge-gprc/>
* Free software: GPL-3.0-only


## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.

## Issues

```
(deluge-gprc-2JayzDdQ-py3.9) bash-3.2$ python3 -m grpc_tools.protoc -I ./deluge_gprc/ --python_out=./deluge_gprc/__protoc_gen__/ --gprc_out=./deluge_gprc/__protoc_gen__/ deluge_gprc/deluge_dfs.proto
protoc-gen-gprc: program not found or is not executable
Please specify a program using absolute path or make sure the program is available in your PATH system variable
--gprc_out: protoc-gen-gprc: Plugin failed with status code 1.
(deluge-gprc-2JayzDdQ-py3.9) bash-3.2$
```
