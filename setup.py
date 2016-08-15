try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='nose-timelimit',
    version='0.1.0',
    description='Enforced timelimits for nosetests',
    author='Manuel Schölling',
    author_email='manuel.schoelling@gmx.de',
    install_requires=['nose>=1.3.0'],
    py_modules=['nose_timelimit'],
    entry_points={
      'nose.plugins.0.10': [
        'timelimit = nose_timelimit:TimelimitPlugin'
      ]
    }
)
