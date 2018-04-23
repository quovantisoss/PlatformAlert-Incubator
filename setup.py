import uuid

from platalert import get_current_version
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


import setuptools
setuptools.setup(
    name='PlatformAlert',
    packages=setuptools.find_packages(),
    version=get_current_version(),
    license='BSD',
    platforms=['any'],
    install_requires=[str(ir.req) for ir in parse_requirements('py-requirements/dev.txt', session=uuid.uuid4())],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    include_package_data=True,
    zip_safe=True
)
