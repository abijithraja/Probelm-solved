#include <stdio.h>

int minimumIndex(int* nums, int numsSize) {
    int candidate = 0, count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (count == 0) {
            candidate = nums[i];
        }
        count += (nums[i] == candidate) ? 1 : -1;
    }
    int total_count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == candidate) {
            total_count++;
        }
    }
    if (total_count * 2 <= numsSize) {
        return -1; 
    }
    int left_count = 0;
    for (int i = 0; i < numsSize - 1; i++) { 
        if (nums[i] == candidate) {
            left_count++;
        }
        int right_count = total_count - left_count;
        
        if (left_count * 2 > (i + 1) && right_count * 2 > (numsSize - i - 1)) {
            return i; 
        }
    }

    return -1; 
}

