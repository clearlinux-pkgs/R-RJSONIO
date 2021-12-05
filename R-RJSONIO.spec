#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RJSONIO
Version  : 1.3.1.6
Release  : 44
URL      : https://cran.r-project.org/src/contrib/RJSONIO_1.3-1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RJSONIO_1.3-1.6.tar.gz
Summary  : Serialize R Objects to JSON, JavaScript Object Notation
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: R-RJSONIO-lib = %{version}-%{release}
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

%description lib
lib components for the R-RJSONIO package.


%prep
%setup -q -c -n RJSONIO
cd %{_builddir}/RJSONIO

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638695907

%install
export SOURCE_DATE_EPOCH=1638695907
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RJSONIO
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RJSONIO
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RJSONIO
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RJSONIO || :


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
/usr/lib64/R/library/RJSONIO/doc/Changes
/usr/lib64/R/library/RJSONIO/doc/Changes.html
/usr/lib64/R/library/RJSONIO/doc/biblio.xml
/usr/lib64/R/library/RJSONIO/doc/fromJSONTimes.rda
/usr/lib64/R/library/RJSONIO/doc/missingValues.Rdb
/usr/lib64/R/library/RJSONIO/doc/missingValues.html
/usr/lib64/R/library/RJSONIO/doc/overview.Rdb
/usr/lib64/R/library/RJSONIO/doc/overview.bib
/usr/lib64/R/library/RJSONIO/doc/overview.html
/usr/lib64/R/library/RJSONIO/doc/overview.pdf
/usr/lib64/R/library/RJSONIO/doc/performance.R
/usr/lib64/R/library/RJSONIO/doc/timings.docx
/usr/lib64/R/library/RJSONIO/doc/toJSONTimes.rda
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
/usr/lib64/R/library/RJSONIO/libs/RJSONIO.so
/usr/lib64/R/library/RJSONIO/libs/RJSONIO.so.avx512
