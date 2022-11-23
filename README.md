# mecab-python-msvc

[![Build](https://github.com/Pusnow/mecab-python-msvc/actions/workflows/build-python-lib.yml/badge.svg)](https://github.com/Pusnow/mecab-python-msvc/actions/workflows/build-python-lib.yml)

mecab-python-msvc는 mecab-ko-msvc에서 사용할 수 있는 mecab-python을 빌드하는 프로젝트입니다.

## 설치

* [mecab-ko-msvc](https://github.com/Pusnow/mecab-ko-msvc/)를 설치하지 않았으면 설치해야 합니다.
* [mecab-ko-dic-msvc](https://github.com/Pusnow/mecab-ko-dic-msvc/)를 설치하지 않았으면 설치해야 합니다.
* 실행 환경에 맞는 [최신버전](https://github.com/Pusnow/mecab-python-msvc/releases/latest)을 다운로드합니다. 32bit, 64bit 버전의 Python 2.7, 3.3, 3.4, 3.5, 3.6 을 지원합니다.
* `pip install <다운로드한 whl 파일>` 로 설치할 수 있습니다. venv를 사용하지 않을 경우 관리자 권한이 필요합니다.  

## 빌드 정보

* mecab-python-msvc 는 [Appveyor](https://www.appveyor.com)를 이용합니다.
* 빌드 과정은 [Appveyor 페이지](https://ci.appveyor.com/project/Pusnow/mecab-python-msvc) 에 기록되어 있습니다.
* 개인적으로 빌드를 하고 싶으신 분은 [appveyor.yml](https://github.com/Pusnow/mecab-python-msvc/blob/master/appveyor.yml) 을 참고하시기 바랍니다.

## 관련 프로젝트

* [Mecab-Ko-MSVC](https://github.com/Pusnow/mecab-ko-msvc)
* [Mecab-Ko-Dic-MSVC](https://github.com/Pusnow/mecab-ko-dic-msvc)
* [Mecab-Java-MSVC](https://github.com/Pusnow/mecab-java-msvc)


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
