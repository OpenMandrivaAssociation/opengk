%define	name	opengk
%define	version	1.4.2
%define	snap	20050322
%define	release	0.%{snap}.6mdk

%{expand:%%define o_ver %(echo v%{version}| sed "s#\.#_#g")}
%define openh323_version 1.15.3
%define pwlib_version 1.8.4

Summary:	H.323 basic gatekeeper
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MPL
Group:		Communications
Source0:	%{name}-%{o_ver}-%{snap}-src.tar.bz2
Patch0:		%{name}-mak_files.patch.bz2
URL:		http://openh323.sourceforge.net/
BuildRequires:	openh323-devel >= %{openh323_version} pwlib-devel >= %{pwlib_version}
Conflicts:	vpb-devel
Requires:	openh323_1 >= %{openh323_version}
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
