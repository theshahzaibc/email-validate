import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='email_validate',
    version='1.0.0',
    author='Shahzaib Chadhar',
    author_email='shahzaibsaifullah@gmail.com',
    description='A Basic package for email verification',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/theshahzaibc/email_validate',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
    install_requires=[
        # -*- Extra requirements: -*-
        'requests',
        're'
    ],
)
