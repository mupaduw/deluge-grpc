# deluge-gprc


[![pypi](https://img.shields.io/pypi/v/deluge-gprc.svg)](https://pypi.org/project/deluge-gprc/)
[![python](https://img.shields.io/pypi/pyversions/deluge-gprc.svg)](https://pypi.org/project/deluge-gprc/)
[![Build Status](https://github.com/mupaduw/deluge-gprc/actions/workflows/dev.yml/badge.svg)](https://github.com/mupaduw/deluge-gprc/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/mupaduw/deluge-gprc/branch/main/graphs/badge.svg)](https://codecov.io/github/mupaduw/deluge-gprc)



RPC interface to deluge-card.


* Documentation: <https://mupaduw.github.io/deluge-gprc>
* GitHub: <https://github.com/mupaduw/deluge-gprc>
* PyPI: <https://pypi.org/project/deluge-gprc/>
* Free software: GPL-3.0-only


This project uses [deluge-card](https://github.com/mupaduw/deluge-card) which provides a python API for the Deluge Folder System.

## Features

- run a local gRPC service with async_server.py - listens on `locahost:50057` by default.
- demos for Python3 and nodejs (see [Usage](./deluge-grpc/usage))

## Exmample

```
bash-3.2$ time python demo_client.py samples ~/Music/DELUGE/04 -p "**/Rol*/808 Sna*.*"
INFO:root:ListContents request (streaming) card_root: "/Users/chrisbc/Music/DELUGE/04"
pattern: "**/Rol*/808 Sna*.*"
content_type: SAMPLE

SAMPLES/xLDk/Roland TR-808/808 Snare_hi1.wav
SAMPLES/xLDk/Roland TR-808/808 Snare_hi2.wav
SAMPLES/xLDk/Roland TR-808/808 Snare_hi3.wav
SAMPLES/xLDk/Roland TR-808/808 Snare_lo1.wav
SAMPLES/xLDk/Roland TR-808/808 Snare_lo2.wav
SAMPLES/xLDk/Roland TR-808/808 Snare_lo3.wav

real	0m1.702s
user	0m0.164s
sys	0m0.049s
```

## Credits

## Issues

```
(deluge-gprc-2JayzDdQ-py3.9) bash-3.2$ python3 -m grpc_tools.protoc -I ./deluge_gprc/ --python_out=./deluge_gprc/__protoc_gen__/ --gprc_out=./deluge_gprc/__protoc_gen__/ deluge_gprc/deluge_dfs.proto
protoc-gen-gprc: program not found or is not executable
Please specify a program using absolute path or make sure the program is available in your PATH system variable
--gprc_out: protoc-gen-gprc: Plugin failed with status code 1.
(deluge-gprc-2JayzDdQ-py3.9) bash-3.2$
```
