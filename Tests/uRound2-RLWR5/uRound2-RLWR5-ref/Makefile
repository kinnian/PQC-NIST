CC      = gcc
LDLIBS  = -lcrypto -lkeccak -I. -lm
CFLAGS  = -std=c99 -O3 -fomit-frame-pointer -DROUND2_INTERMEDIATE

PQCgenKAT_kem:
	@$(CC) $(CFLAGS) -o $@ *.c $(LDLIBS)
