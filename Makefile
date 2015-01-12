#
# Package acta-diurna into an RPM

# git rev-list HEAD --count
help:
	@echo "Available make targets:"
	@echo
	@echo "help: print this message"
	@echo "rpm: Package acta-diurna"
	@echo "clean: remove fakeroot"
	@echo "superclean: remove fakeroot, nuke all rpms"

h: help

clean:
	@-rm -fr fakeroot

superclean: clean
	@-rm -f *.rpm

fakeroot-dirs:
	mkdir -p fakeroot/usr/local/sbin
	sudo chown -R root fakeroot/usr/local/sbin

fakeroot-files: fakeroot-dirs
	sudo cp acta-diurna.py fakeroot/usr/local/sbin/acta-diurna

fakeroot-permfix: fakeroot-files
	sudo chown -R root fakeroot

rpm: fakeroot-permfix
	fpm -a noarch \
		-t rpm \
		-s dir \
		-n acta-diurna \
		--version 0.1 \
		--license BSD \
		--iteration $(shell git rev-list HEAD --count) \
		--description "Acta-Diurna creates /etc/motd from scripts. See https://github.com/unixorn/acta-diurna for details" \
		-C fakeroot \
		usr
