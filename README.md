<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/setupcfg-generator.svg?maxAge=3600)](https://pypi.org/project/setupcfg-generator/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/setupcfg-generator.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/setupcfg-generator.py/actions)

### Installation
```bash
$ [sudo] pip install setupcfg-generator
```

#### Features
`[metadata]`|files/environment variables
-|-
`name`|current directory basename or `$NAME`
`classifiers`|`classifiers.txt`, `$CLASSIFIERS`
`description`|`description.txt`, `$DESCRIPTION`
`keywords`|`keywords.txt`, `$KEYWORDS`
`long_description`|`README.md`/`README.rst`, `$LONG_DESCRIPTION`
`long_description_content_type`|`text/markdown` if `long_description` is `.md` file
`version`|`version.txt`, `$VERSION`
`url`|`$URL`

`[options]`|files/environment variables
-|-
`install_requires`|`requirements.txt`
`packages`|`setuptools.find_packages()`result, folders with `__init__.py`
`py_modules`|python files in a current directory
`scripts`|`bin/*` or `scripts/*` files

files can be in the current directory or any subdirectory

#### Examples
```
project-name.py/
├── bin
|   └── script
├── classifiers.txt
├── description.txt
├── subfolder/keywords.txt
├── requirements.txt
├── module.py
├── package
|   └── __init__.py
├── README.md
├── scripts
|   └── script
├── setup.py
├── subfolder/version.txt
```

```bash
$ cd path/to/project-name.py
$ export URL="https://github.com/owner/repo"
$ python -m setupcfg_generator
$ cat setup.cfg
[metadata]
name = project-name
version = 1.0.0
url = https://github.com/owner/repo
classifiers = file: classifiers.txt
description = file: description.txt
long_description = file: README.md
long_description_content_type = text/markdown
keywords = key1 key2

[options]
install_requires =
    req1
    req2
packages =
    pkgname
py_modules =
    module
scripts =
    bin/script
    scripts/script
```

#### Related
+   [`setuppy-generator` - `setup.py` generator](https://pypi.org/project/setuppy-generator/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>