'''
Reference:
    https://packaging.python.org/tutorials/distributing-packages/
'''
from os import path

from setuptools import find_packages, setup


with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    LONG_DESC = f.read()


KWARGS = dict(
    name='yunpian-python-sdk',
    version='1.0.0',
    description='Yunpian Python SDK',
    long_description=LONG_DESC,
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
        # 'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='yunpian sdk',
    packages=find_packages(exclude=['docs', 'tests', 'dist']),
    install_requires=[],
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
    setup(**KWARGS)
