#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools_scm_git_archive
Version  : 1.1
Release  : 13
URL      : https://files.pythonhosted.org/packages/7e/2c/0c15b29a1b5940250bfdc4a4f53272e35cd7cf8a34159291b6b4ec9eb291/setuptools_scm_git_archive-1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/7e/2c/0c15b29a1b5940250bfdc4a4f53272e35cd7cf8a34159291b6b4ec9eb291/setuptools_scm_git_archive-1.1.tar.gz
Summary  : setuptools_scm plugin for git archives
Group    : Development/Tools
License  : MIT
Requires: setuptools_scm_git_archive-license = %{version}-%{release}
Requires: setuptools_scm_git_archive-python = %{version}-%{release}
Requires: setuptools_scm_git_archive-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : setuptools_scm

%description
that adds support for git archives (for example the ones GitHub automatically
        generates).
        
        Note that it only works for archives of tagged commits (because git currently
        lacks a format option equivalent to ``git describe --tags``).
        
        Usage
        -----
        
        Add ``'setuptools_scm_git_archive'`` to the ``setup_requires`` parameter in your

%package license
Summary: license components for the setuptools_scm_git_archive package.
Group: Default

%description license
license components for the setuptools_scm_git_archive package.


%package python
Summary: python components for the setuptools_scm_git_archive package.
Group: Default
Requires: setuptools_scm_git_archive-python3 = %{version}-%{release}

%description python
python components for the setuptools_scm_git_archive package.


%package python3
Summary: python3 components for the setuptools_scm_git_archive package.
Group: Default
Requires: python3-core
Provides: pypi(setuptools_scm_git_archive)

%description python3
python3 components for the setuptools_scm_git_archive package.


%prep
%setup -q -n setuptools_scm_git_archive-1.1
cd %{_builddir}/setuptools_scm_git_archive-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583533399
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/setuptools_scm_git_archive
cp %{_builddir}/setuptools_scm_git_archive-1.1/LICENSE %{buildroot}/usr/share/package-licenses/setuptools_scm_git_archive/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/setuptools_scm_git_archive/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
