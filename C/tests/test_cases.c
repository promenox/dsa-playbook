#include <CUnit/Basic.h>
#include "../src/fibonacci.h"

// test cases
void test_fibonacci(void) {
    CU_ASSERT(fibonacci(-1) == 0);
    CU_ASSERT(fibonacci(0) == 0);
    CU_ASSERT(fibonacci(9) == 34);
}

// other tests
/* 
void test_other_module(void) {
    CU_ASSERT(other_function(2) == 4);
}
*/

int main() {
    // maintain registry for tests
    CU_initialize_registry();

    // collection of related tests 
    // 0 pointers for setup and teardown
    CU_pSuite suite = CU_add_suite("AllTests", 0, 0);

    // adding tests
    CU_add_test(suite, "Fibonacci tests", test_fibonacci);
    
    // CU_add_test(suite, "Other module tests", test_other_module);

    // run all test suites
    CU_basic_run_tests();
    // free memory and clean registry
    CU_cleanup_registry();
    return 0; // program success exit
}