import os
import pathlib
import shutil
import subprocess
import sys

from setuptools import find_packages, setup, Extension
from setuptools.command.build_py import build_py
from wasabi import Printer

msg = Printer()
IS_OBFUSCATE = True
SOURCE_PATH = "src"
OBFUSCATED_PATH = "obfuscated"

def obfuscate(input_path, output_path):

    output_path = pathlib.Path(output_path)

    shutil.rmtree(str(output_path.parent), ignore_errors=True)
    msg.good("Deleted: {}".format(output_path.parent))
    
    subprocess.call(["pyarmor",  "obfuscate", "--recursive", "--platform", "linux.x86_64", "--platform", "windows.x86_64", "--output", str(output_path), str(input_path)], env=os.environ)

    msg.good("Obfuscated: {}".format(output_path))

def obfuscate_package(name):
    input_path = "{}/{}/__init__.py".format(SOURCE_PATH, name)
    output_path = "{}/{}".format(OBFUSCATED_PATH, name)
    source_path = OBFUSCATED_PATH
    package_data = {"": ["pytransform/*.so", "pytransform/*.key", "pytransform/*.lic", "pytransform/platforms/linux/x86_64/*.so", "pytransform/platforms/windows/x86_64/*.dll"]}
    obfuscate(input_path, output_path)
    return source_path, package_data

name = "sample2"
version = "1.0"
description = "sample2"
long_description = description
long_description_content_type = 'text/x-rst'
url = "https://fx-git.fx.com/sample1"
author = "fx"
author_email = "fx@adv-fx.com"
license = None # "MIT"
keywords = "fx",

requirements = ["pyarmor==6.2.0"]

source_path, package_data = obfuscate_package(name)

package_dir = {"": source_path}

ext_modules = None
cmdclass = {"build_py": build_py}

setup(name = name,
    version = version,
    description = description,
    long_description = long_description,
    long_description_content_type = long_description_content_type,
    url = url,
    author = author,
    author_email = author_email,
    #license = "MIT",
    keywords = keywords,
    install_requires = requirements,
    package_dir = package_dir,
    packages = find_packages(source_path),
    package_data = package_data,
    zip_safe = False,
    ext_modules = ext_modules,
    cmdclass = cmdclass,
)

msg.info("Mode: Obfuscation = {}".format(IS_OBFUSCATE))
