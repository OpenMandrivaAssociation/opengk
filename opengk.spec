%define	name	opengk
%define	version	1.4.2
%define	cvs	20070503
%define	release	%mkrel 0.%{cvs}.1

Summary:	H.323 basic gatekeeper
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MPL
Group:		Communications
Source0:	%{name}-%{cvs}.tar.bz2
Patch0:		%{name}-mak_files.patch
URL:		http://openh323.sourceforge.net/
BuildRequires:	openh323-devel pwlib-devel
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


%build
export CFLAGS="%{optflags} -DLDAP_DEPRECATED"
export CXXFLAGS="%{optflags} -DLDAP_DEPRECATED"

%make \
    OPTCCFLAGS="%{optflags}" \
    PWLIBDIR=%{_datadir}/pwlib \
    OPENH323DIR=%{_prefix} \
    PREFIX=%{_prefix} \
    PWLIB_BUILD=1 \
    optshared \

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
