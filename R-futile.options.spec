#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-futile.options
Version  : 1.0.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/futile.options_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/futile.options_1.0.1.tar.gz
Summary  : Futile Options Management
Group    : Development/Tools
License  : LGPL-3.0
BuildRequires : clr-R-helpers

%description
The âfutile.optionsâ subsystem provides an easy user-defined options management
system that is properly scoped. This means that options created via
âfutile.optionsâ are fully self-contained and will not collide with options
defined in other packages. This package is a self-contained package within the
futile suite of libraries.

%prep
%setup -q -c -n futile.options

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524275111

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1524275111
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library futile.options
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library futile.options
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library futile.options
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library futile.options|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/futile.options/DESCRIPTION
/usr/lib64/R/library/futile.options/INDEX
/usr/lib64/R/library/futile.options/Meta/Rd.rds
/usr/lib64/R/library/futile.options/Meta/features.rds
/usr/lib64/R/library/futile.options/Meta/hsearch.rds
/usr/lib64/R/library/futile.options/Meta/links.rds
/usr/lib64/R/library/futile.options/Meta/nsInfo.rds
/usr/lib64/R/library/futile.options/Meta/package.rds
/usr/lib64/R/library/futile.options/NAMESPACE
/usr/lib64/R/library/futile.options/R/futile.options
/usr/lib64/R/library/futile.options/R/futile.options.rdb
/usr/lib64/R/library/futile.options/R/futile.options.rdx
/usr/lib64/R/library/futile.options/help/AnIndex
/usr/lib64/R/library/futile.options/help/aliases.rds
/usr/lib64/R/library/futile.options/help/futile.options.rdb
/usr/lib64/R/library/futile.options/help/futile.options.rdx
/usr/lib64/R/library/futile.options/help/paths.rds
/usr/lib64/R/library/futile.options/html/00Index.html
/usr/lib64/R/library/futile.options/html/R.css
