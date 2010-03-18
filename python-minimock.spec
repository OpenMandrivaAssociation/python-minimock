Name:           python-minimock
Version:        1.2.5
Release:        %mkrel 2
Summary:        The simplest possible mock library
Group:          Development/Python
License:        MIT
URL:            http://pypi.python.org/pypi/MiniMock
Source0:        http://pypi.python.org/packages/source/M/MiniMock/MiniMock-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Minimock is a simple lbirary for doing Mock objects with doctest.

%prep
%setup -q -n MiniMock-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/MiniMock-%{version}-py?.?.egg-info
%{python_sitelib}/minimock*
