from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'dego',         
  packages = ['dego'],
  version = '0.0.2',      
  license='MIT',
  description = 'The Python RPC Wrapper for DeroGoldd and WalletAPI.',
  long_description=long_description,
  long_description_content_type='text/markdown',   
  author = 'Sayan Bhattacharyya',                
  author_email = 'sohamb03@outlook.com',    
  url = 'https://github.com/sohamb03/dego-py', 
  download_url = 'https://github.com/sohamb03/dego-py/archive/v_002.tar.gz',
  python_requires=">=3.6",
  install_requires=[           
          'requests'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  project_urls={
        'Documentation': 'https://dego-py.sohamb03.me',
  },
)
