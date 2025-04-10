#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v23
# autospec commit: a88ffdc
#
Name     : R-RJSONIO
Version  : 2.0.0
Release  : 65
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/RJSONIO_2.0.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/RJSONIO_2.0.0.tar.gz
Summary  : Serialize R Objects to JSON, JavaScript Object Notation
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: R-RJSONIO-lib = %{version}-%{release}
Requires: R-RJSONIO-license = %{version}-%{release}
BuildRequires : buildreq-R

%description
data in Javascript object notation (JSON) format.
  This allows R objects to be inserted into Javascript/ECMAScript/ActionScript code
  and allows R programmers to read and convert JSON content to R objects.
  This is an alternative to rjson package. Originally, that was too slow for converting large R objects to JSON
  and was not extensible.  rjson's performance is now similar to this package, and perhaps slightly faster in some cases.
  This package uses methods and is readily extensible by defining methods for different classes, 
  vectorized operations, and C code and callbacks to R functions for deserializing JSON objects to R. 
  The two packages intentionally share the same basic interface. This package (RJSONIO) has many additional
  options to allow customizing the generation and processing of JSON content.
  This package uses libjson rather than implementing yet another JSON parser. The aim is to support
  other general projects by building on their work, providing feedback and benefit from their ongoing development.

%package lib
Summary: lib components for the R-RJSONIO package.
Group: Libraries
Requires: R-RJSONIO-license = %{version}-%{release}

%description lib
lib components for the R-RJSONIO package.


%package license
Summary: license components for the R-RJSONIO package.
Group: Default

%description license
license components for the R-RJSONIO package.


%prep
%setup -q -n RJSONIO
pushd ..
cp -a RJSONIO buildavx2
popd
pushd ..
cp -a RJSONIO buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744041368

%install
export SOURCE_DATE_EPOCH=1744041368
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-RJSONIO
cp %{_builddir}/RJSONIO/src/libjson/License.txt %{buildroot}/usr/share/package-licenses/R-RJSONIO/99e1860a6b62d89f4fdefcc6298decb025a882ae || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RJSONIO/DESCRIPTION
/usr/lib64/R/library/RJSONIO/INDEX
/usr/lib64/R/library/RJSONIO/LICENSE
/usr/lib64/R/library/RJSONIO/Meta/Rd.rds
/usr/lib64/R/library/RJSONIO/Meta/features.rds
/usr/lib64/R/library/RJSONIO/Meta/hsearch.rds
/usr/lib64/R/library/RJSONIO/Meta/links.rds
/usr/lib64/R/library/RJSONIO/Meta/nsInfo.rds
/usr/lib64/R/library/RJSONIO/Meta/package.rds
/usr/lib64/R/library/RJSONIO/NAMESPACE
/usr/lib64/R/library/RJSONIO/R/RJSONIO
/usr/lib64/R/library/RJSONIO/R/RJSONIO.rdb
/usr/lib64/R/library/RJSONIO/R/RJSONIO.rdx
/usr/lib64/R/library/RJSONIO/help/AnIndex
/usr/lib64/R/library/RJSONIO/help/RJSONIO.rdb
/usr/lib64/R/library/RJSONIO/help/RJSONIO.rdx
/usr/lib64/R/library/RJSONIO/help/aliases.rds
/usr/lib64/R/library/RJSONIO/help/paths.rds
/usr/lib64/R/library/RJSONIO/html/00Index.html
/usr/lib64/R/library/RJSONIO/html/R.css
/usr/lib64/R/library/RJSONIO/sampleData/array.json
/usr/lib64/R/library/RJSONIO/sampleData/array2.json
/usr/lib64/R/library/RJSONIO/sampleData/array3.json
/usr/lib64/R/library/RJSONIO/sampleData/embedded.json
/usr/lib64/R/library/RJSONIO/sampleData/glossay.json
/usr/lib64/R/library/RJSONIO/sampleData/int.json
/usr/lib64/R/library/RJSONIO/sampleData/intScalar.json
/usr/lib64/R/library/RJSONIO/sampleData/keys.json
/usr/lib64/R/library/RJSONIO/sampleData/menu.json
/usr/lib64/R/library/RJSONIO/sampleData/menu1.json
/usr/lib64/R/library/RJSONIO/sampleData/nestedArray.json
/usr/lib64/R/library/RJSONIO/sampleData/nestedObj.json
/usr/lib64/R/library/RJSONIO/sampleData/obj.json
/usr/lib64/R/library/RJSONIO/sampleData/obj1.json
/usr/lib64/R/library/RJSONIO/sampleData/obj2.json
/usr/lib64/R/library/RJSONIO/sampleData/obj3.json
/usr/lib64/R/library/RJSONIO/sampleData/usaColors.as
/usr/lib64/R/library/RJSONIO/sampleData/usaPolygons.as
/usr/lib64/R/library/RJSONIO/sampleData/widget.json
/usr/lib64/R/library/RJSONIO/tests/array.R
/usr/lib64/R/library/RJSONIO/tests/bigInt.R
/usr/lib64/R/library/RJSONIO/tests/charNULL.R
/usr/lib64/R/library/RJSONIO/tests/con1.R
/usr/lib64/R/library/RJSONIO/tests/con2.R
/usr/lib64/R/library/RJSONIO/tests/containers.R
/usr/lib64/R/library/RJSONIO/tests/empty.R
/usr/lib64/R/library/RJSONIO/tests/encoding.R
/usr/lib64/R/library/RJSONIO/tests/exp.R
/usr/lib64/R/library/RJSONIO/tests/flat.json
/usr/lib64/R/library/RJSONIO/tests/keys.R
/usr/lib64/R/library/RJSONIO/tests/nested.json
/usr/lib64/R/library/RJSONIO/tests/newsUTF8.rda
/usr/lib64/R/library/RJSONIO/tests/performance.R
/usr/lib64/R/library/RJSONIO/tests/prealloc.R
/usr/lib64/R/library/RJSONIO/tests/s4.R
/usr/lib64/R/library/RJSONIO/tests/scalarCollapse.R
/usr/lib64/R/library/RJSONIO/tests/serialize.R
/usr/lib64/R/library/RJSONIO/tests/simple.R
/usr/lib64/R/library/RJSONIO/tests/simplify.R
/usr/lib64/R/library/RJSONIO/tests/stringFun.R
/usr/lib64/R/library/RJSONIO/tests/toJSON.R
/usr/lib64/R/library/RJSONIO/tests/utf8.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/RJSONIO/libs/RJSONIO.so
/V4/usr/lib64/R/library/RJSONIO/libs/RJSONIO.so
/usr/lib64/R/library/RJSONIO/libs/RJSONIO.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-RJSONIO/99e1860a6b62d89f4fdefcc6298decb025a882ae
