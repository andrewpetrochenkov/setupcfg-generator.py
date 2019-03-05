#!/usr/bin/env python
"""create `setup.cfg`"""
import click
import setupcfg_generator


MODULE_NAME = "setupcfg_generator"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [path]' % MODULE_NAME


@click.command()
@click.argument('path', required=False)
def _cli(path=None):
    setupcfg_generator.create(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
