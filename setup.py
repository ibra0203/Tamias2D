from setuptools import setup

setup(name='Tamias2D',
      version='0.1',
      description='A physics engine',
      url='',
      author='Olu',
      license='MIT',
      packages=['Tamias2D'],
      install_requires=[
          'collision',
          'matplotlib',
          'pygame',
      ],
      zip_safe=False)