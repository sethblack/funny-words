from distutils.core import setup

setup(
    name='funny-words',
    version='1.7',
    packages=['funny_words'],
    author='Seth Black',
    author_email='sblack@sethserver.com',
    url='https://github.com/sethblack/funny-words',
    license='Apache 2.0',
    description='Generates a list of funny words for naming things such as app releases, internal projects, servers and children.',
    scripts=['funny-words'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)