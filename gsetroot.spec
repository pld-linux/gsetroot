Summary:	gsetroot - front-end for Esetroot
Summary(pl.UTF-8):	gsetroot - frontend dla programu Esetroot
Name:		gsetroot
Version:	1.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gsetroot/%{name}-%{version}.tar.gz
# Source0-md5:	611ec41489ef50405aca545e32edf264
URL:		http://gsetroot.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.10.40
BuildRequires:	glitz-devel
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	Esetroot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gsetroot is a front-ent for Esetroot. It can be used to choose a
wallpaper and configure root window. It works under Window Managers
like FluxBox, Enlightenment, WindowMaker, NextStep, BlackBox, IceWM
and others.

%description -l pl.UTF-8
gsetroot jest frontendem dla programu Esetroot. Może być używany do
wybierania tapety i konfigurowania nadrzędnego okna. Działa w takich
zarządcach okien jak fluxbox, Enlightement, WindowMaker, NextStep,
BlackBox, IceWM oraz innych.

%prep
%setup -q

%build
%{__intltoolize}
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc $RPM_BUILD_ROOT%{_prefix}/doc/%{name}/*
%attr(755,root,root) %{_bindir}/*
