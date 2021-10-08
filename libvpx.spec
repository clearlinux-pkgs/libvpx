#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvpx
Version  : 1.11.0
Release  : 23
URL      : https://github.com/webmproject/libvpx/archive/v1.11.0/libvpx-1.11.0.tar.gz
Source0  : https://github.com/webmproject/libvpx/archive/v1.11.0/libvpx-1.11.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause HPND
Requires: libvpx-bin = %{version}-%{release}
Requires: libvpx-filemap = %{version}-%{release}
Requires: libvpx-lib = %{version}-%{release}
Requires: libvpx-license = %{version}-%{release}
BuildRequires : nasm
BuildRequires : yasm
Patch1: build.patch

%description
Welcome to the WebM VP8/VP9 Codec SDK!
COMPILING THE APPLICATIONS/LIBRARIES:
The build system used is similar to autotools. Building generally consists of
"configuring" with your desired build options, then using GNU make to build
the application.

%package bin
Summary: bin components for the libvpx package.
Group: Binaries
Requires: libvpx-license = %{version}-%{release}
Requires: libvpx-filemap = %{version}-%{release}

%description bin
bin components for the libvpx package.


%package dev
Summary: dev components for the libvpx package.
Group: Development
Requires: libvpx-lib = %{version}-%{release}
Requires: libvpx-bin = %{version}-%{release}
Provides: libvpx-devel = %{version}-%{release}
Requires: libvpx = %{version}-%{release}

%description dev
dev components for the libvpx package.


%package filemap
Summary: filemap components for the libvpx package.
Group: Default

%description filemap
filemap components for the libvpx package.


%package lib
Summary: lib components for the libvpx package.
Group: Libraries
Requires: libvpx-license = %{version}-%{release}
Requires: libvpx-filemap = %{version}-%{release}

%description lib
lib components for the libvpx package.


%package license
Summary: license components for the libvpx package.
Group: Default

%description license
license components for the libvpx package.


%prep
%setup -q -n libvpx-1.11.0
cd %{_builddir}/libvpx-1.11.0
%patch1 -p1
pushd ..
cp -a libvpx-1.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633724640
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure --disable-static || : ; CC=gcc CXX=g++ AR=ar STRIP=strip NM=nm ./configure --prefix=/usr --libdir=/usr/lib64 --target=x86_64-linux-gnu --disable-static --enable-libs --enable-vp8 --enable-vp9 --enable-runtime-cpu-detect --enable-shared --enable-webm-io --enable-experimental
make  %{?_smp_mflags}  V=1 AS_FLAGS="-a AMD64"

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static || : ; CC=gcc CXX=g++ AR=ar STRIP=strip NM=nm ./configure --prefix=/usr --libdir=/usr/lib64 --target=x86_64-linux-gnu --disable-static --enable-libs --enable-vp8 --enable-vp9 --enable-runtime-cpu-detect --enable-shared --enable-webm-io --enable-experimental
make  %{?_smp_mflags}  V=1 AS_FLAGS="-a AMD64"
popd
%install
export SOURCE_DATE_EPOCH=1633724640
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libvpx
cp %{_builddir}/libvpx-1.11.0/LICENSE %{buildroot}/usr/share/package-licenses/libvpx/4dbe7c1f3a1833a88333a7c282119323e9ef44fa
cp %{_builddir}/libvpx-1.11.0/third_party/googletest/src/LICENSE %{buildroot}/usr/share/package-licenses/libvpx/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/libvpx-1.11.0/third_party/libwebm/LICENSE.TXT %{buildroot}/usr/share/package-licenses/libvpx/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9
cp %{_builddir}/libvpx-1.11.0/third_party/libyuv/LICENSE %{buildroot}/usr/share/package-licenses/libvpx/f71908f9aaa4aee0f15f9983b6cf83791d18cfd7
cp %{_builddir}/libvpx-1.11.0/third_party/x86inc/LICENSE %{buildroot}/usr/share/package-licenses/libvpx/697c7d5a9839cf4160acd85431b0c58be874dba8
pushd ../buildavx2/
%make_install_v3
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vpxdec
/usr/bin/vpxenc
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/vpx/vp8.h
/usr/include/vpx/vp8cx.h
/usr/include/vpx/vp8dx.h
/usr/include/vpx/vpx_codec.h
/usr/include/vpx/vpx_decoder.h
/usr/include/vpx/vpx_encoder.h
/usr/include/vpx/vpx_ext_ratectrl.h
/usr/include/vpx/vpx_frame_buffer.h
/usr/include/vpx/vpx_image.h
/usr/include/vpx/vpx_integer.h
/usr/lib64/libvpx.so
/usr/lib64/pkgconfig/vpx.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-libvpx

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvpx.so.7
/usr/lib64/libvpx.so.7.0
/usr/lib64/libvpx.so.7.0.0
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvpx/4dbe7c1f3a1833a88333a7c282119323e9ef44fa
/usr/share/package-licenses/libvpx/59cd938fcbd6735b1ef91781280d6eb6c4b7c5d9
/usr/share/package-licenses/libvpx/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/libvpx/697c7d5a9839cf4160acd85431b0c58be874dba8
/usr/share/package-licenses/libvpx/f71908f9aaa4aee0f15f9983b6cf83791d18cfd7
