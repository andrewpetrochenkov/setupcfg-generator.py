#!/usr/bin/env python
import os
import public
import setupcfg
import setuptools


FILE_TYPES = ["classifiers", "description", "long_description"]
STRING_TYPES = ["keywords", "version"]


def files():
    for root, dirs, files in os.walk(os.getcwd(), followlinks=True):
        for f in files:
            yield os.path.join(root, f)


def name():
    """return `name` string - working dir name without extension"""
    return os.path.basename(os.getcwd()).split(".")[0].lower()


def packages():
    """return `packages` list - `setuptools.find_packages()`"""
    return setuptools.find_packages()


def py_modules():
    """return a list with python modules in project root"""
    def ismodule(f):
        return os.path.splitext(f)[1] == ".py" and f != "setup.py"

    def module_name(f):
        return os.path.splitext(f)[0]
    return list(map(module_name, filter(ismodule, os.listdir(os.getcwd()))))


def install_requires():
    """return `install_requires` list. content of `requirements.txt`"""
    result = []

    def readline(l):
        return l.split("#")[0].lstrip().rstrip()
    for f in list(files()):
        if os.path.basename(f) in ["requirements.txt"]:
            result += list(map(readline, open(f).read().splitlines()))
    return list(sorted(filter(None, set(result))))


def scripts():
    """return `scripts` list. `bin/`, `scripts/` files"""
    result = []
    exclude = ['.DS_Store', 'Icon\r']
    for path in ["bin", "scripts"]:
        if os.path.exists(path) and os.path.isdir(path):
            files = list(filter(lambda f: f not in exclude, os.listdir(path)))
            result += list(map(lambda f: os.path.join(path, f), files))
    return result


def _get_env(key):
    for _key in [key, key.upper()]:
        if _key in os.environ:
            return os.environ[_key]


def _env_data(keys):
    result = dict()
    for key in keys:
        value = _get_env(key)
        if value:
            result[key] = value
    return result


def get_file(filenames, files):
    for filename in filenames:
        if os.path.exists(filename):
            return filename
    for filename in filenames:
        matches = list(filter(lambda f: os.path.basename(f) == filename, files))
        if len(matches) == 1:
            return matches[0]


def get_value(key, path):
    if key in FILE_TYPES:
        return "file: %s" % path
    if key in STRING_TYPES:
        return open(path).read().strip()


def metadata():
    """return a dictionary with `metadata` sesction"""
    data = dict(name=name())
    _files = list(files())
    key_files = dict(
        classifiers=["classifiers.txt"],
        description=["description.txt"],
        keywords=["keywords.txt"],
        long_description=["README.rst", "README.md"],
        version=["version.txt"]
    )
    for key, filenames in key_files.items():
        path = get_file(filenames, _files)
        if path:
            data[key] = get_value(key, path)
    data.update(_env_data(setupcfg.metadata.KEYS))
    if os.path.splitext(data.get("long_description", ""))[1] == ".md":
        data["long_description_content_type"] = "text/markdown"
    return data


def options():
    """return a dictionary with `options` sesction"""
    return dict(
        install_requires=install_requires(),
        packages=packages(),
        py_modules=py_modules(),
        scripts=scripts()
    )


@public.add
def create(path="setup.cfg"):
    """create `setup.cfg`"""
    if not path:
        path = "setup.cfg"
    if not os.path.exists("setup.py"):
        raise OSError("%s/setup.py not exists" % os.getcwd())
    cfg = setupcfg.Setupcfg(metadata=metadata(), options=options())
    dirname = os.path.dirname(path)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)
    string = """# https://pypi.org/project/setupcfg-generator/
%s
""" % str(cfg)
    open(path, "w").write(string)
