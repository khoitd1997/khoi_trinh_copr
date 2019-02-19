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

%files
%{_datadir}/kd_wallpaper/TCP118v1_by_Tiziano_Consonni.jpg

%install
mkdir -p %{buildroot}%{_datadir}/kd_wallpaper/
# install -p -m 755 %{SOURCE1} %{_datadir}/kd_wallpaper
install -D -p -m755 %{SOURCE1} %{buildroot}%{_datadir}/kd_wallpaper/

%post
sudo cat << EOF >> /usr/share/glib-2.0/schemas/99_my_custom_settings.gschema.override
[org.cinnamon.desktop.background]
picture-uri='file:///usr/share/kd_wallpaper/TCP118v1_by_Tiziano_Consonni.jpg'

[org.gnome.desktop.background]
picture-uri='file:///usr/share/kd_wallpaper/TCP118v1_by_Tiziano_Consonni.jpg'
EOF
chmod a+rx /usr/share/kd_wallpaper/TCP118v1_by_Tiziano_Consonni.jpg
chmod a+rx /usr/share/glib-2.0/schemas/99_my_custom_settings.gschema.override
sudo glib-compile-schemas /usr/share/glib-2.0/schemas/

%changelog