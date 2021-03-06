#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-setuptools_scm_git_archive
Version  : 1.4
Release  : 24
URL      : https://files.pythonhosted.org/packages/69/5f/7135eec07395c51d3dd6899251b277405ecc2f8f7a80ef80a483e3c5a2bd/setuptools_scm_git_archive-1.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/69/5f/7135eec07395c51d3dd6899251b277405ecc2f8f7a80ef80a483e3c5a2bd/setuptools_scm_git_archive-1.4.tar.gz
Summary  : setuptools_scm plugin for git archives
Group    : Development/Tools
License  : MIT
Requires: pypi-setuptools_scm_git_archive-license = %{version}-%{release}
Requires: pypi-setuptools_scm_git_archive-python = %{version}-%{release}
Requires: pypi-setuptools_scm_git_archive-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools_scm)

%description
**This plugin is obsolete. ``setuptools_scm >= 7.0.0`` supports Git archives by itself.**

%package license
Summary: license components for the pypi-setuptools_scm_git_archive package.
Group: Default

%description license
license components for the pypi-setuptools_scm_git_archive package.


%package python
Summary: python components for the pypi-setuptools_scm_git_archive package.
Group: Default
Requires: pypi-setuptools_scm_git_archive-python3 = %{version}-%{release}

%description python
python components for the pypi-setuptools_scm_git_archive package.


%package python3
Summary: python3 components for the pypi-setuptools_scm_git_archive package.
Group: Default
Requires: python3-core
Provides: pypi(setuptools_scm_git_archive)

%description python3
python3 components for the pypi-setuptools_scm_git_archive package.


%prep
%setup -q -n setuptools_scm_git_archive-1.4
cd %{_builddir}/setuptools_scm_git_archive-1.4
pushd ..
cp -a setuptools_scm_git_archive-1.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656543295
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-setuptools_scm_git_archive
cp %{_builddir}/setuptools_scm_git_archive-1.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-setuptools_scm_git_archive/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-setuptools_scm_git_archive/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
