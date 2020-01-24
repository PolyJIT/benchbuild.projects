from setuptools import setup, find_namespace_packages

with open('README.md') as f:
    long_description = f.read()

src_extra_files = ["patches/linpack.patch"]

setup(name='benchbuild.projects',
      use_scm_version=True,
      url='https://github.com/PolyJIT/benchbuild.projects',
      packages=find_namespace_packages(include=['benchbuild.projects*']),
      package_data={"becnbuild.projects": src_extra_files},
      include_package_data=True,
      setup_requires=["pytest-runner", "setuptools_scm"],
      tests_require=["pytest"],
      install_requires=["attrs>=17.4.0", "benchbuild>4.0.1"],
      author="Andreas Simbuerger",
      author_email="simbuerg@fim.uni-passau.de",
      description=
      "Projects curated for the benchbuild empirical research toolkit.",
      long_description=long_description,
      long_description_content_type='text/markdown',
      license="MIT",
      classifiers=[
          'Development Status :: 4 - Beta', 'Intended Audience :: Developers',
          'Topic :: Software Development :: Testing',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      keywords="benchbuild projects run-time")
