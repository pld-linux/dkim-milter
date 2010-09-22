# TODO: Init script
# TODO: Devel package 
Summary:	DomainKeys Identified Mail service provider
# Summary(pl.UTF-8):	-
Name:		dkim-milter
Version:	2.8.3
Release:	0.2
License:	Sendmail Open Source License
Group:		Applications
Source0:	http://downloads.sourceforge.net/project/dkim-milter/DKIM%20Milter/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d2043c269f1720cc095a9b4f163cf3df
URL:		http://www.sendmail.com/sm/wp/dkim/
BuildRequires:	libmilter-devel
# Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A milter-based application (dkim-filter) which plugs in to Sendmail to
provide DomainKeys Identified Mail service. Library (libdkim) which
can be used to build DKIM-compliant applications or MTAs

# %description -l pl.UTF-8

%prep
%setup -q

cat > devtools/Site/site.config.m4 <<'EOF'
define(`confMANROOT', `%{_mandir}/man')
define(`confUBINDIR', `%{_sbindir}')
define(`confCCOPTS', `%{optflags}')
EOF


%build
#%%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -p -m 644 -D dkim-filter/dkim-filter.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/mail/%{name}/dkim-filter.conf

install -p -d $RPM_BUILD_ROOT%{_mandir}/man{3,5,8}
install -p -d $RPM_BUILD_ROOT%{_sbindir}
install -p -d $RPM_BUILD_ROOT%{_includedir}


%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	{UBIN,MAN}OWN=$(whoami) {UBIN,MAN}GRP=$(id -ng) UBINMODE=755 MANMODE=644


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man3/ar.3*
%{_mandir}/man5/*
%{_mandir}/man8/*
/etc/mail/dkim-milter/dkim-filter.conf
