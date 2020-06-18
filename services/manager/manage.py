import coverage
import unittest
import click

from flask.cli import FlaskGroup
from project import create_app

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccesful():
        COV.stop()
        COV.save()
        print('Coverage Summary')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


@cli.command('test')
@click.option('--all', 'only', flag_value='test', default=True)
@click.option('--only', 'only', flag_value='only_')
@click.option('--name', default=None)
def test(only, name):
    """Runs the test without code coverage"""
    loader = unittest.TestLoader()
    loader.testMethodPrefix = only
    if name is None:
        tests = loader.discover('project/tests', 'test*.py')
    else:
        tests = loader.loadTestsFromName(name)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
