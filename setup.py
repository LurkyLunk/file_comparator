from setuptools import setup, find_packages

setup(
    name='file_comparator',
    version='0.1',
    packages=find_packages(),
    description='A tool to compare files and output differences',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Gregory Dixon',
    author_email='shikobastudios@gmail.com',
    url='https://github.com/lurkylunk/file_comparator',
    install_requires=[
        python3
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
