import pathlib
import re

from setuptools import setup


ROOT_PATH = pathlib.Path(__file__).parent

SCRIPT_PATH = ROOT_PATH / 'bin' / 'kernel-env'

VERSION_PATTERN = re.compile(r'''VERSION *= *["']([.\d]+)["']''', re.I)


with SCRIPT_PATH.open() as script_desc:
    for script_line in script_desc:
        version_match = VERSION_PATTERN.match(script_line)
        if version_match:
            break
    else:
        raise RuntimeError("failed to find version in script")

VERSION = version_match.group(1)


setup(
    name='kernel-env',
    url='https://github.com/uchicagods/infratools',
    version=VERSION,
    install_requires=[
        'argcmdr==0.6.0',
    ],
    scripts=[
        str(SCRIPT_PATH),
    ],
)
