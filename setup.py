from distutils.core import setup
setup(
  name = 'MSDSF22M024',        
  packages = ['MSDSF22M024'],   
  version = '0.1',     
  license='MIT',     
  description = 'HAVE SOME FUNCTIONS',  
  author = 'RIDA',                  
  author_email = 'www.rida275@gmail.com',      
  url = 'https://github.com/rida-manzoor/MSDSF22M024',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'FUNCTION'],   
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)