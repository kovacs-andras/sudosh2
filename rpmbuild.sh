yum -y groupinstall 'Development Tools'
yum -y install -y rpm* gcc gpg* rng-tools

rpmdev-setuptree
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
wget -P ~/rpmbuild/SOURCES/ https://github.com/kovacs-andras/sudosh2/archive/1.0.7.zip
unzip -j ~/rpmbuild/SOURCES/1.0.7.zip sudosh2-1.0.7/sudosh.spec -d ~/rpmbuild/SPECS/

rpmbuild -ba /root/rpmbuild/SPECS/sudosh.spec
