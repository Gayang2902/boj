#include <unistd.h>

#define REATINT(n) { \
    char c = *p++; \
    for (; ~c & 16; c = *p++); \
    for (; c & 16; c = *p++) n = 10 * n + (c & 15); }

__libc_start_main() {
    char r[2048], w[2048], *p = r; syscall(0, 0, r, 2049)
}