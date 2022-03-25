#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python parser
Summary(pl.UTF-8):	Parser Pythona
Name:		python-parso
# keep 0.7.x here for python2 support
Version:	0.7.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/parso/
Source0:	https://files.pythonhosted.org/packages/source/p/parso/parso-%{version}.tar.gz
# Source0-md5:	eac40cda515ee71e3bb008c404ca3ac1
URL:		https://pypi.org/project/parso/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-docopt
BuildRequires:	python-pytest >= 3.0.7
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-docopt
BuildRequires:	python3-pytest >= 3.0.7
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python versions).
Parso is also able to list multiple syntax errors in your python file.

%description -l pl.UTF-8
Parso to parser Pythona obsługujący wznawianie po błędach i obustronną
analizę dla różnych wersji Pythona (w wielu wersjach Pythona). Parso
potrafi także wypisać wiele błędów składni w pliku pythonowym.

%package -n python3-parso
Summary:	Python parser
Summary(pl.UTF-8):	Parser Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-parso
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python versions).
Parso is also able to list multiple syntax errors in your python file.

%description -n python3-parso -l pl.UTF-8
Parso to parser Pythona obsługujący wznawianie po błędach i obustronną
analizę dla różnych wersji Pythona (w wielu wersjach Pythona). Parso
potrafi także wypisać wiele błędów składni w pliku pythonowym.

%package apidocs
Summary:	API documentation for Python parso module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona parso
Group:		Documentation

%description apidocs
API documentation for Python parso module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona parso.

%prep
%setup -q -n parso-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGELOG.rst LICENSE.txt README.rst
%{py_sitescriptdir}/parso
%{py_sitescriptdir}/parso-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-parso
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGELOG.rst LICENSE.txt README.rst
%{py3_sitescriptdir}/parso
%{py3_sitescriptdir}/parso-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,docs,*.html,*.js}
%endif
