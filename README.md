MeCab python module for MeCab 0.996
===================================

## 소개

[MeCab](http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html)에서 제공하는 [python 바인딩 소스](https://code.google.com/p/mecab/downloads/detail?name=mecab-python-0.996.tar.gz&can=2&q=)가 Python 3.x에서 문제를 일으키므로 SWIG를 최신  버전(SWIG 3.0.0)을 사용하여 다시 생성한 소스입니다.

## 설치

    :::text
    % git clone https://bitbucket.org/eunjeon/mecab-python-0.996.git
    % cd mecab-python-0.996
    % python setup.py build
    % su
    # python setup.py install
  
You can change the install directory with the --prefix option. For example:

    :::text
    % python setup.py install --prefix=/tmp/pybuild/foobar

## 사용법

샘플 프로그램인 test.py를 참조하세요.

## 라이센스
mecab-ko의 라이센스는 MeCab의 라이센스를 그대로 따릅니다.

> MeCab 는 무료 소프트웨어입니다. GPL (the GNU General Public License), LGPL (Lesser GNU General Public License) 또는 BSD 라이선스에 따라 소프트웨어를 사용, 재배포할 수 있습니다. 자세한 내용은 COPYING, GPL, LGPL, BSD 각 파일을 참조하십시오.
