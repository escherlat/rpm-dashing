# disable debug symbol stripping on the files from this rpm
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:	dashing	
Version:	1.3.2
Release:	1%{dist}
Summary:  Dashing is a Sinatra based framework that lets you build beautiful dashboards	

Group:		Metrics
License:	MIT
URL:	http://dashing.io	
Source0: %{name}.tar.gz	
Source1: %{name}.init
Source2: %{name}.nginx.conf
Source3: scl-ruby193.sh
BuildArch: x86_64 
Requires(pre): shadow-utils
Requires: nginx 
Requires: libxslt
Requires: ruby193-ruby
Requires: ruby193-rubygem-bundler

%description
This is an RPM build of dashing designed to run via SCL ruby193 with nginx front-end

%pre

# check for, and if necessary, create the tdclient user/group
getent group dashing >/dev/null  || groupadd -r dashing
getent passwd dashing >/dev/null || useradd -r -g dashing -d /opt/dashing -s /sbin/nologin -c "dashing service account" dashing
exit 0

%prep
%setup -q -n %{name}

%build

%install
export DONT_STRIP=1

mkdir -p %{buildroot}/opt/%{name}
mkdir -p %{buildroot}/etc/nginx/conf.d
mkdir -p %{buildroot}/etc/init.d
mkdir -p %{buildroot}/etc/profile.d

tar xf %{SOURCE0} -C %{buildroot}/opt

install -m 755 %{SOURCE1} %{buildroot}/etc/init.d/dashing
install -m 755 %{SOURCE2} %{buildroot}/etc/nginx/conf.d/dashing.conf
install -m 755 %{SOURCE3} %{buildroot}/etc/profile.d/scl-ruby193.sh

%files
%defattr(700, dashing, dashing, 700)
/opt/dashing/*
/opt/dashing/.bundle/*
%attr(755, root, root) /etc/nginx/conf.d/dashing.conf
%attr(755, root, root) /etc/init.d/dashing
%attr(755, root, root) /etc/profile.d/scl-ruby193.sh

%changelog
* Fri Apr 18 2014 waz0wski <waz0wski@mass-distortion.net> - 1.3.2-1
- Initial RPM packaging of dashing