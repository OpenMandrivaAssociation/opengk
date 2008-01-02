%define	cvs	20070503

Summary:	H.323 basic gatekeeper
Name:		opengk
Version:	1.4.2
Release:	%mkrel 0.%{cvs}.4
License:	MPL
Group:		Communications
Source0:	%{name}-%{cvs}.tar.bz2
Patch0:		%{name}-mak_files.patch
URL:		http://openh323.sourceforge.net/
BuildRequires:	opal3-devel
BuildRequires:	ptlib-devel
Conflicts:	vpb-devel
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a very basic H.323 Gatekeeper.

Basic features
---------------
OpenGatekeeper supports all the basic features of an H.323 Gatekeeper such
as registration, admissions and access control, address translation and 
bandwidth monitoring and control.

Advanced features
-----------------
- Gatekeeper routed calls 
- Support of H.323v2 alias types 
  (party number, URL, transport id and email address) 
- Support for gateway prefixes 
- Registration and call activity logs 
- Neighbour gatekeeper database 
- Registration time to live 

%prep

%setup -q -n %{name}
%patch0 -p1
perl -pi -e 's,BOOL,bool,g' main.h
perl -pi -e 's,BOOL,bool,g' main.cxx


%build
export CFLAGS="%{optflags} -DLDAP_DEPRECATED"
export CXXFLAGS="%{optflags} -DLDAP_DEPRECATED"

%make \
    USE_OPAL=1 \
    OPTCCFLAGS="%{optflags}" \
    PWLIBDIR=%{_datadir}/ptlib \
    OPALDIR=%{_datadir}/opal \
    PREFIX=%{_prefix} \
    OPAL_LIBDIR=%{_libdir} \
    OPAL_INCDIR=%{_includedir}/opal \
    PWLIB_BUILD=1 \
    optshared

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 obj_*/%{name} %{buildroot}%{_bindir}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ReadMe.txt
%attr(0755,root,root) %{_bindir}/*
