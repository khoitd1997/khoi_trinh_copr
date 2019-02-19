Name:    test_package
Version: 1
Release: 1%{?dist}
Summary: Say hello, Texas style

License: Public Domain
URL: https://github.com/khoitd1997/khoi_trinh_copr
Source0: test_package
Source1: TCP118v1_by_Tiziano_Consonni.jpg
BuildArch: noarch

Requires: dconf

%description
Test background image installation

%install
# mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE1} %{_datadir}/khoi_trinh_wallpaper   
# install -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}

%files
%{_bindir}/TCP118v1_by_Tiziano_Consonni.jpg

%post
dconf write /org/gnome/desktop/background/picture-uri "'file://%{_datadir}/khoi_trinh_wallpaper/TCP118v1_by_Tiziano_Consonni.jpg'"


%changelog