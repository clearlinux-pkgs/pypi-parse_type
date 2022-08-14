#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-parse_type
Version  : 0.6.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/d6/d4/8d79b78547df1c670406146776e1a91b1d5a1f5b928c0d7249e4fd1019bb/parse_type-0.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/d4/8d79b78547df1c670406146776e1a91b1d5a1f5b928c0d7249e4fd1019bb/parse_type-0.6.0.tar.gz
Summary  : Simplifies to build parse types based on the parse module
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-parse_type-license = %{version}-%{release}
Requires: pypi-parse_type-python = %{version}-%{release}
Requires: pypi-parse_type-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(parse)
BuildRequires : pypi(six)

%description
===============================================================================
parse_type
===============================================================================

%package license
Summary: license components for the pypi-parse_type package.
Group: Default

%description license
license components for the pypi-parse_type package.


%package python
Summary: python components for the pypi-parse_type package.
Group: Default
Requires: pypi-parse_type-python3 = %{version}-%{release}

%description python
python components for the pypi-parse_type package.


%package python3
Summary: python3 components for the pypi-parse_type package.
Group: Default
Requires: python3-core
Provides: pypi(parse_type)
Requires: pypi(parse)
Requires: pypi(six)

%description python3
python3 components for the pypi-parse_type package.


%prep
%setup -q -n parse_type-0.6.0
cd %{_builddir}/parse_type-0.6.0
pushd ..
cp -a parse_type-0.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656392907
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-parse_type
cp %{_builddir}/parse_type-0.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-parse_type/6cd5ef4a9fc84461bee82c9674d9ba53d6baee52
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
/usr/share/package-licenses/pypi-parse_type/6cd5ef4a9fc84461bee82c9674d9ba53d6baee52

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
