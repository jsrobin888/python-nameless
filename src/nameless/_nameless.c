
char* longest(int argc, char *argv[]) {
    if (argc) {
        int len,
            max = 0,
            pos = 0;
        for (int i = 0; i < argc; i++) {
            len = strlen(argv[i]);
            if (len > max) {
                max = len;
                pos = i;
            }
        }
        return argv[pos];
    } else {
        return NULL;
    }
}

