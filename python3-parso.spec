#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Python parser
Summary(pl.UTF-8):	Parser Pythona
Name:		python3-parso
Version:	0.8.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/parso/
Source0:	https://files.pythonhosted.org/packages/source/p/parso/parso-%{version}.tar.gz
# Source0-md5:	f83b2e4164f6589ccae39b16c30ed5de
URL:		https://pypi.org/project/parso/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-docopt
BuildRequires:	python3-pytest >= 3.0.7
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.6
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
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test -k 'not test_python_errors'
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGELOG.rst LICENSE.txt README.rst
%{py3_sitescriptdir}/parso
%{py3_sitescriptdir}/parso-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,docs,*.html,*.js}
%endif
