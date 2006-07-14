Summary:	gsetroot - front-end for Esetroot
Summary(pl):	gsetroot - front-end dla Esetroot
Name:		gsetroot
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gsetroot/%{name}-%{version}.tar.gz
# Source0-md5:	8abbb5cf0cae3128059d6a1151d29604
URL:		http://gsetroot.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glitz-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
Requires:	Esetroot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gsetroot is a front-ent for Esetroot. It can be used to choose a
wallpaper and configure root window. It works under Window Managers
like FluxBox, Enlightenment, WindowMaker, NextStep, BlackBox, IceWM
and others.

%description -l pl
gsetroot jest front-endem dla Esetroot. Mo¿e byæ u¿ywany do wybierania
tapety i konfigurowania nadrzêdnego okna. Dzia³a w takich Mened¿erach
Okien jak fluxbox, Enlightement, Windowmaker, NextStep, BlackBox,
IceWM oraz innych.

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
