from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='dtmvisual',
      version='1.0.0',
      description='This package consists of functionalities for dynamic topic modelling and its visualization',
      url='https://github.com/GSukr/dtmvisual',
      author='Svitlana',
      author_email='svitlana.galeshchuk@gmail.com',
      license='MIT',
      packages=['dtmvisual'],
      install_requires=['gensim==3.4.0', 'pickle-mixin', 'pprint', 'seaborn==0.8.1', 'matplotlib==2.0.2'],
      include_package_data=True,
      zip_safe=True)

