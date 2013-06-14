Name:           python-minimock
Version:        1.2.8
Release:        1
Summary:        The simplest possible mock library
Group:          Development/Python
License:        MIT
URL:            http://pypi.python.org/pypi/MiniMock
Source0:        http://pypi.python.org/packages/source/M/MiniMock/MiniMock-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildArch:	noarch

%description
Minimock is a simple lbirary for doing Mock objects with doctest.

%prep
%setup -q -n MiniMock-%{version}

%build

%install
%{__python} setup.py install --root=%{buildroot}
 
%files
%doc docs/*
%{python_sitelib}/MiniMock-%{version}-py?.?.egg-info
%{python_sitelib}/minimock*


%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.6-1mdv2011.0
+ Revision: 662535
- update to new version 1.2.6

* Thu Mar 18 2010 Caio Begotti <caio1982@mandriva.org> 1.2.5-2mdv2011.0
+ Revision: 525008
- missing buildrequires entry
- import python-minimock


