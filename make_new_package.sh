#!/bin/bash
# used for creating new rpm package

mkdir -p ./${1}
cd ${1}

cat << EOF > ${1}.spec
Name:    ${1}
Version: 1
Release: 1%{?dist}
Summary: Say hello, Texas style

License: Public Domain
Source0: ${1}
BuildArch: noarch

%description
A simple program to greet the user, Texas style.

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%files
%{_bindir}/${1}
%{_bindir}/TCP118v1_by_Tiziano_Consonni.jpg

%changelog
EOF

# fedpkg --release f27 local