import setuptools

setuptools.setup(
    name='setupcfg-generator',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
