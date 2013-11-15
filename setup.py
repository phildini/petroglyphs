import os
from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='petroglyphs',
    version='0.1dev',
    packages=['petroglyphs'],
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple ORM-based settings manager and injector for Django',
    long_description=README,
    url='https://github.com/phildini/petroglyphs',
    author='Philip James',
    author_email='pjj@philipjohnjames.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # replace these appropriately if you are using Python 3
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)