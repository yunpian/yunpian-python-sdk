'''
Reference:
    https://packaging.python.org/tutorials/distributing-packages/    
'''
from setuptools import find_packages, setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


kwargs = dict(
    name='yunpian-python-sdk',
    version='1.0.0',
    description='Yunpian Python SDK',
    long_description=long_description,
    author='dzh',
    author_email='daizhong@yunpian.com',
    url='https://github.com/yunpian/yunpian-python-sdk',
    download_url='https://pypi.python.org/pypi/yunpian-python-sdk',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='yunpian sdk',
    packages=find_packages(exclude=['docs', 'tests', 'dist']),
    install_requires=['inotify'],
    # $ pip install -e .[dev,test]
    extras_require={
        # 'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    package_data={
        # 'sample': ['package_data.dat'],
    }
)

if __name__ == '__main__':
    setup(**kwargs)
