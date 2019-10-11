# YOUR_PACKAGE
A Python template.

## Replace
* ``YOUR_PACKAGE`` - package name (also folder)
* ``YOUR_NAME`` - your real name
* ``YOUR_EMAIL`` - your email address
* ``YOUR_GITHUB_NAME`` - your github name or organization
* ``YOUR_TWINE_USERNAME`` - your user name on PyPI, see ``.travis.yml``

## External Services
* [Read the Docs](https://readthedocs.org/) - Host for Sphinx generated DOCS
* [TravisCI](https://travis-ci.org/) - Continous Integration for testing, coverage, deplyoment to PyPI
* [Coveralls](https://coveralls.io/) - Host for calculated coverage and overview
* [PyPI](https://pypi.org/) - Host for the package wheels
* [Test-PyPI](https://test.pypi.org/) - Testing host for the package wheels
* [Zenodo](https://zenodo.org/) - Get a DOI for each release

Use the same login data for pypi and test.pypi.
Set your pypi password as a environment variable on Travis under ``TWINE_PASSWORD`` as a privat key.

## Workflow
After granting the above mentioned services access to your GitHub repository,
the following will/should happen:

* Bevor each commit:
  * use the script `black YOUR_PACKAGE/` after you have written your code to get a unique code-format
  * have a look at the [black code formater](https://github.com/python/black)

* On each commit:
  * Travis run will be triggered
    * run tests on travis (only on Python 3.6 and Linux in this configuration, see ``.travis.yml``)
    * calculate coverage during tests (see ``.coveragerc``)
    * build wheels (universel wheels for py2 and py3 in this configuration, see ``setup.cfg``)
    * deploy wheels to Test-PyPI

* On each release:
  * last commit bevor release should be a version bump in ``_version.py`` to release version
    * example: "0.0.1.dev0" -> "0.0.2"
    * commit message: "release version bump 0.0.2"
    * then create a release on the GitHub page
  * Travis run will be triggered
    * same happens as mentioned for every commit above
    * deploy wheels to PyPI -> these are then **installable via pip**
  * a Zenodo release will be triggered and a DOI will be generated
  * after release: commit version bump to ``dev0`` status
    * example: "0.0.2" -> "0.0.3.dev0"
    * commit message: "version bump 0.0.3.dev0 [skip ci]" (Travis will be skipped)

* try to report your changes in the ``CHANGELOG.md`` file
  * on release, copy everything under "Unreleased" to the release notes
  * replace "[Unreleased]" with the version number and add a link to the comparrison
  * create a new "Unreleased" section
  * example: https://github.com/GeoStat-Framework/ogs5py/blob/master/CHANGELOG.md

### Versioning
Have a look here, for a versioning policy: [semver.org/](https://semver.org/)

### Documentation
* use the numpy doc style: [NumPyDoc](https://numpydoc.readthedocs.io/en/latest/format.html)
* example: [Numpy doc example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html)
* the ``docs/source/package.rst`` will read the docstring from ``YOUR_PACKAGE/__init__.py``
  * use ``.. autosummary::`` there (see the source)
  * create a ``module.rst`` for each submodule in your package like ``core.py`` and ``core.rst``
  * if your submodule is a folder, create a __init__.py there
  * include submodules in ``YOUR_PACKAGE/__init__.py`` and in the toc-tree in ``docs/source/package.rst``
* to create the Documentation locally, run: ``make clean && make html`` in the ``docs`` folder

## Cython
For an example including cython functions, have a look here:
https://github.com/LSchueler/Python-Deployment