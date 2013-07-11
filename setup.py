from distutils.core import setup

setup(
    name='dt8601',
    version='0.2.0',
    author='Armin Hanisch',
    author_email='mail@arminhanisch.de',
    packages=['dt8601', 'dt8601.test'],
    url='http://pypi.python.org/pypi/dt8601/',
    license='MIT',
    description='Python date package according to ISO8601 with useful date routines, holiday calculation and an ISO8601 parser.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        ],
)
