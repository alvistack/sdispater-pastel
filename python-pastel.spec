# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pastel
Epoch: 100
Version: 0.2.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Bring colors to your terminal
License: MIT
URL: https://github.com/sdispater/pastel/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Pastel is a simple library to help you colorize strings in your
terminal.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/tests
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pastel
Summary: Bring colors to your terminal
Requires: python3
Provides: python3-pastel = %{epoch}:%{version}-%{release}
Provides: python3dist(pastel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pastel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pastel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pastel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pastel) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pastel
Pastel is a simple library to help you colorize strings in your
terminal.

%files -n python%{python3_version_nodots}-pastel
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pastel
Summary: Bring colors to your terminal
Requires: python3
Provides: python3-pastel = %{epoch}:%{version}-%{release}
Provides: python3dist(pastel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pastel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pastel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pastel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pastel) = %{epoch}:%{version}-%{release}

%description -n python3-pastel
Pastel is a simple library to help you colorize strings in your
terminal.

%files -n python3-pastel
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
