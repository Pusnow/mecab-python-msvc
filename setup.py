#!/usr/bin/env python

from distutils.core import setup,Extension,os
import string

def cmd1(str):
    return os.popen(str).readlines()[0][:1]


setup(name = "mecab-python",
	version = cmd1("C:\mecab\mecab.exe --version"),
	py_modules=["MeCab"],
	data_files = [("lib\\site-packages\\", ["C:\\mecab\\libmecab.dll"])],
	ext_modules = [
		Extension("_MeCab",
			["MeCab_wrap.cxx",],
			include_dirs=["C:\\mecab\\"],
			library_dirs=["C:\\mecab\\"],
			libraries=["libmecab"])
			])
