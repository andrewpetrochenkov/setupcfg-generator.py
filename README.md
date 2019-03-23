<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/setupcfg-generator.svg?longCache=True)](https://pypi.org/project/setupcfg-generator/)
[![](https://img.shields.io/pypi/v/setupcfg-generator.svg?maxAge=3600)](https://pypi.org/project/setupcfg-generator/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/setupcfg-generator.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/setupcfg-generator.py/)

#### Installation
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

#### Functions
function|`__doc__`
-|-
`setupcfg_generator.create(path='setup.cfg')` |create `setup.cfg`

#### CLI
usage|`__doc__`
-|-
`python -m setupcfg_generator [path]` |create `setup.cfg`

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

#### Related projects
+   [`classifiers-generator` - classifiers generator](https://pypi.org/project/classifiers-generator/)
+   [`readme-badges` - `README.md` badges](https://pypi.org/project/readme-badges/)
+   [`readme-docstring` - generate README.md from python docstrings](https://pypi.org/project/readme-docstring/)
+   [`readme-generator` - `README.md` generator](https://pypi.org/project/readme-generator/)
+   [`setupcfg-generator` - `setup.cfg` generator](https://pypi.org/project/setupcfg-generator/)
+   [`travis-generator` - `.travis.yml` generator](https://pypi.org/project/travis-generator/)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>