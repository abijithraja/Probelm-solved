#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";

    char* prefix = strs[0]; 
    int prefixLen = strlen(prefix);

    for (int i = 1; i < strsSize; i++) {
        int j = 0;
        while (j < prefixLen && strs[i][j] == prefix[j]) {
            j++; 
        }
        prefixLen = j; 

        if (prefixLen == 0) return ""; 
    }

    char* result = (char*)malloc(prefixLen + 1);
    strncpy(result, prefix, prefixLen);
    result[prefixLen] = '\0'; // Null-terminate the result
    return result;
}
