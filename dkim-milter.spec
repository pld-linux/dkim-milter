# TODO: Fix make system so PLD flags will be used
# TODO: Make it install
Summary:	DomainKeys Identified Mail service provider
# Summary(pl.UTF-8):	-
Name:		dkim-milter
Version:	2.8.3
Release:	0.1
License:	Sendmail Open Source License
Group:		Applications
Source0:	http://downloads.sourceforge.net/project/dkim-milter/DKIM%20Milter/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d2043c269f1720cc095a9b4f163cf3df
URL:		http://www.sendmail.com/sm/wp/dkim/
# BuildRequires:	-
# Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A milter-based application (dkim-filter) which plugs in to Sendmail to
provide DomainKeys Identified Mail service. Library (libdkim) which
can be used to build DKIM-compliant applications or MTAs

# %description -l pl.UTF-8

%prep
%setup -q

%build
#%%configure
#%%{__make}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
