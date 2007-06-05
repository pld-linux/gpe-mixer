#
Summary:	GPE mixer
Name:		gpe-mixer
Version:	0.42
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	41b1ef201e4583e55a7462f1404de70d
URL:		http://gpe.linuxtogo.org
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libgpewidget-devel
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define gpename %(echo %{name} | sed -e 's/gpe-//')

%description
GPE mixer, for embedded devices

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/alarm.png
%{_pixmapsdir}/%{name}.png
