# TODO: Init script
# TODO: Devel package
Summary:	DomainKeys Identified Mail sender authentication sendmail milter
Name:		dkim-milter
Version:	2.8.3
Release:	0.5
License:	Sendmail Open Source License
Group:		Applications
Source0:	http://downloads.sourceforge.net/dkim-milter/%{name}-%{version}.tar.gz
# Source0-md5:	d2043c269f1720cc095a9b4f163cf3df
URL:		http://www.dkim.org/
BuildRequires:	libmilter-devel
# postfix or sendmail have milter support
Requires:	/usr/lib/sendmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The dkim-milter package is an open source implementation of the DKIM
sender authentication system proposed by the E-mail Signing Technology
Group (ESTG), now a proposed standard of the IETF (RFC4871).

DKIM is an amalgamation of the DomainKeys (DK) proposal by Yahoo!,
Inc. and the Internet Identified Mail (IIM) proposal by Cisco.

This package consists of a library that implements the DKIM service
and a milter-based filter application that can plug in to the sendmail
MTA to provide that service to sufficiently recent sendmail MTAs and
other MTAs that support the milter protocol.

%prep
%setup -q

cat > devtools/Site/site.config.m4 <<'EOF'
define(`confMANROOT', `%{_mandir}/man')
define(`confUBINDIR', `%{_sbindir}')
define(`confCCOPTS', `%{rpmcflags}')
APPENDDEF(`confLIBS', `-lresolv')
EOF

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{3,5,8},%{_sysconfdir}/mail/%{name},%{_includedir}}

%{__make} install \
	{UBIN,MAN}OWN=$(whoami) \
	{UBIN,MAN}GRP=$(id -ng) \
	UBINMODE=755 \
	MANMODE=644 \
	DESTDIR=$RPM_BUILD_ROOT

cp -p dkim-filter/dkim-filter.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/mail/%{name}/dkim-filter.conf

# no -devel yet
%{__rm} $RPM_BUILD_ROOT%{_includedir}/dkim.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE RELEASE_NOTES INSTALL KNOWNBUGS FEATURES
%attr(755,root,root) %{_sbindir}/dkim-filter
%attr(755,root,root) %{_sbindir}/dkim-genkey
%attr(755,root,root) %{_sbindir}/dkim-testkey
%attr(755,root,root) %{_sbindir}/dkim-testssp
%{_mandir}/man3/ar.3*
%{_mandir}/man5/dkim-filter.conf.5*
%{_mandir}/man8/dkim-filter.8*
%{_mandir}/man8/dkim-genkey.8*
%{_mandir}/man8/dkim-stats.8*
%{_mandir}/man8/dkim-testkey.8*
%{_mandir}/man8/dkim-testssp.8*
%dir %{_sysconfdir}/mail/dkim-milter
%{_sysconfdir}/mail/dkim-milter/dkim-filter.conf
