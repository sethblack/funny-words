from distutils.core import setup

setup(
    name='funny-words',
    version='1.0',
    packages=['funny_words'],
    include_package_data=True,
    author='Seth Black',
    author_email='sblack@sethserver.com',
    url='www.sethserver.com',
    scripts=['funny-words'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)