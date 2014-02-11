Name:           python-requests
Version:        2.2.1
Release:        0
Summary:        Awesome Python HTTP Library That's Actually Usable
License:        Apache-2.0
GROUP:          Development/Python
URL:            http://python-requests.org
Source:         %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  fdupes
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python
BuildArch:      noarch

%description
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python’s built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.

Features:

- Extremely simple GET, HEAD, POST, PUT, DELETE Requests
    + Simple HTTP Header Request Attachment
    + Simple Data/Params Request Attachment
    + Simple Multipart File Uploads
    + CookieJar Support
    + Redirection History
    + Redirection Recursion Urllib Fix
    + Auto Decompression of GZipped Content
    + Unicode URL Support
- Simple Authentication
    + Simple URL + HTTP Auth Registry

%prep
%setup -q -n requests-%{version}
cp  %{SOURCE1001} .
# for rpmlint warning: remove shebang from python library
sed -i '/^#!/d' ./requests/certs.py
sed -i '/^#!/d' ./requests/packages/chardet/chardetect.py

%build
python setup.py build

%check
python setup.py test

%install
python setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot}
%fdupes $RPM_BUILD_ROOT

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license LICENSE
%{python_sitelib}/*
