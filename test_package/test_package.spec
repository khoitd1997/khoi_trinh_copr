Name:    test_package
Version: 1
Release: 1%{?dist}
Summary: Say hello, Texas style

License: Public Domain
Source0: test_package

%description
A simple program to greet the user, Texas style.

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%files
%{_bindir}/test_package

%changelog