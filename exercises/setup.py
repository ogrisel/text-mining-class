from setuptools import setup, find_packages


setup(
    name='text-mining-class-exercises',
    version='1.0.0.dev0',
    description="Introduction to text processing and mining",
    author='Olivier Grisel',
    author_email='olivier.grisel@ensta.org',
    zip_safe=False,
    license='BSD',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
    ],
    platforms='any',
    install_requires=[],  # TODO
    tests_require=['pytest'],
)
