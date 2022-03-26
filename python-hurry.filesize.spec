# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		hurry.filesize
%define		egg_name	hurry.filesize
%define		pypi_name	hurry.filesize
Summary:	Python library for human readable file sizes (or anything sized in bytes)
Name:		python-%{pypi_name}
Version:	0.9
Release:	6
License:	ZPL v2.1
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	8549ccd09bb31b5ff1e8e8c1eacc7794
URL:		https://pypi.org/project/hurry.filesize/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python library for human readable file sizes (or anything sized in
bytes).

%package -n python3-%{pypi_name}
Summary:	Python library for human readable file sizes (or anything sized in bytes)
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{pypi_name}
Python library for human readable file sizes (or anything sized in
bytes).

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

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
%doc CHANGES.txt
%dir %{py_sitescriptdir}/hurry
%{py_sitescriptdir}/hurry/filesize
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.pth
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc CHANGES.txt
%dir %{py3_sitescriptdir}/hurry
%{py3_sitescriptdir}/hurry/filesize
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.pth
%endif
