#include "hamming.h"
#include <cstddef>
#include <stdexcept>
#include <string>

    // Some questions from my side:
    //  1. Why does std::string& need to be defined as const? I understand that this
    //  is the right way to go as the input string indeed is a constant but what
    //  i dont understand is why i am not able to compile when it is not defined
    //  as constant.
    //
    //  2. Why am i only able to compile if the function output is of type
    //  size_t? For example, i am not able to compile if i defined the return
    //  type of the function as a unsigned int for example. i.e. it only seems
    //  to compile if the type is of size_t
 
namespace hamming {
    // Pass by reference. Otherwise function will make a copy of the argument
    // variables which is inefficient. Could ofcourse also pass by pointer.
   size_t compute(const std::string& a, const std::string& b) {

        if (a.length() != b.length())
            throw std::domain_error("Error: Strings are of different lengths");

        size_t result = 0;

        // i needs to be of size_t since a.length() returns a type of size_t
        for (size_t i = 0; i < a.length(); i++) {
            if (a[i] != b[i])
                result++;
        }
    return result;
    }
}  // namespace hamming
