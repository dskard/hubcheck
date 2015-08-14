RAPPTURE_PATH = $(shell . /etc/environ.sh; use -e -r rappture; echo $$RAPPTURE_PATH)
INCLUDES      = -I${RAPPTURE_PATH}/include
LIBS          = -L${RAPPTURE_PATH}/lib -lrappture
CFLAGS        = -g -Wall ${INCLUDES} ${LIBS}

all: helloworld

helloworld: helloworld.c
	gcc ${CFLAGS} -o $@ $^

install: helloworld
	install --mode 0755 -D helloworld ../bin/

clean:
	rm -f helloworld

distclean: clean
	rm -f ../bin/helloworld
