/*
 * Copyright (c) 2017 Koninklijke Philips N.V. All rights reserved. A
 * copyright license for redistribution and use in source and binary
 * forms, with or without modification, is hereby granted for
 * non-commercial, experimental, research, public review and
 * evaluation purposes, provided that the following conditions are
 * met:
 * - Redistributions of source code must retain the above copyright
 *   notice, this list of conditions and the following disclaimer.
 * - Redistributions in binary form must reproduce the above copyright
 *   notice, this list of conditions and the following disclaimer in
 *   the documentation and/or other materials provided with the
 *   distribution. If you wish to use this software commercially,
 *   kindly contact info.licensing@philips.com to obtain a commercial
 *   license.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
 * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 */

/** @cond DEVELOP
 * @file
 * Declaration of miscellaneous macros and functions.
 *
 * @author Hayo Baan
 * @endcond
 */

#ifndef MISC_H
#define MISC_H

#include <stdlib.h>
#include <stdint.h>

/**
 * Macro to round a floating point value to an integer value.
 *
 * @param[in] x the value to round
 * @return _round(x)_
 */
#define ROUND(x) ((int)(x + 0.5))

/**
 * Macro to calculate _ceil(a/b)_.
 *
 * Note: only for _a_ and _b > 0_!
 *
 * @param[in] a, b the values of _a_ and _b_
 * @return _ceil(a/b)_
 */
#define CEIL_DIV(a,b) ((a-1)/b + 1)

/**
 * Macro to converts a number of bits into a number of bytes.
 *
 * @param[in] b the number of bits to convert to number of bytes
 * @return _ceil(b/8)_
 */
#define BITS_TO_BYTES(b) (CEIL_DIV(b,8))

#ifdef __cplusplus
extern "C" {
#endif

    /**
     * Prints the given data as hex digits.
     *
     * @param[in] var          the name of the data variable, printed before the data followed by an `=`,
     *                         can be `NULL` to inhibit printing of `var=` and the final newline
     * @param[in] data         the data to print
     * @param[in] nr_elements  the number of elements in the data
     * @param[in] element_size the size of the elements in bytes (bytes will be reversed inside element)
     */
    void print_hex(const char *var, const unsigned char *data, const size_t nr_elements, const size_t element_size);

    /**
     * Prints the given vector in a format usable within sage.
     *
     * @param[in] var         the name of the variable, printed before the vector content followed by an `=`,
     *                        can be `NULL` to inhibit printing of `var=` and the final newline
     * @param[in] vector      the vector
     * @param[in] nr_elements the number of elements of the vector
     */
    void print_sage_u_vector(const char *var, const uint16_t *vector, const size_t nr_elements);

    /**
     * Prints the given scalar matrix in a format usable within sage.
     *
     * @param[in] var        the name of the variable, printed before the matrix content followed by an `=`,
     *                       can be `NULL` to inhibit printing of `var=` and the final newline
     * @param[in] matrix     the matrix
     * @param[in] nr_rows    the number of rows
     * @param[in] nr_columns the number of columns
     */
    void print_sage_u_matrix(const char *var, const uint16_t *matrix, const size_t nr_rows, const size_t nr_columns);

    /**
     * Prints the given matrix of vectors in a format usable within sage.
     *
     * @param[in] var         the name of the variable, printed before the matrix content followed by an `=`,
     *                        can be `NULL` to inhibit printing of `var=` and the final newline
     * @param[in] matrix      the matrix
     * @param[in] nr_rows     the number of rows
     * @param[in] nr_columns  the number of columns
     * @param[in] nr_elements the number of elements of the vectors
     */
    void print_sage_u_vector_matrix(const char *var, const uint16_t *matrix, const size_t nr_rows, const size_t nr_columns, const size_t nr_elements);

    /**
     * Prints the given vector in a format usable within sage.
     *
     * @param[in] var         the name of the variable, printed before the vector content followed by an `=`,
     *                        can be `NULL` to inhibit printing of `var=` and the final newline
     * @param[in] vector      the vector
     * @param[in] nr_elements the number of elements of the vector
     */
    void print_sage_s_vector(const char *var, const int16_t *vector, const size_t nr_elements);

    /**
     * Prints the given scalar matrix in a format usable within sage.
     *
     * @param[in] var        the name of the variable, printed before the matrix content followed by an `=`,
     *                       can be `NULL` to inhibit printing of `var=` and the final newline
     * @param[in] matrix     the matrix
     * @param[in] nr_rows    the number of rows
     * @param[in] nr_columns the number of columns
     */
    void print_sage_s_matrix(const char *var, const int16_t *matrix, const size_t nr_rows, const size_t nr_columns);

    /**
     * Prints the given matrix of vectors in a format usable within sage.
     *
     * @param[in] var         the name of the variable, printed before the matrix content followed by an `=`,
     *                        can be `NULL` to inhibit printing of `var=` and the final newline
     * @param[in] matrix      the matrix
     * @param[in] nr_rows     the number of rows
     * @param[in] nr_columns  the number of columns
     * @param[in] nr_elements the number of elements of the vectors
     */
    void print_sage_s_vector_matrix(const char *var, const int16_t *matrix, const size_t nr_rows, const size_t nr_columns, const size_t nr_elements);

    /**
     * Checked version of `malloc`, aborts if memory could not be allocated.
     *
     * @param size the size of the memory to allocate
     * @return pointer to the allocated memory
     */
    void *checked_malloc(size_t size);

    /**
     * Checked version of `calloc`, aborts if memory could not be allocated.
     *
     * @param count the number of elements to allocate
     * @param size the size of each element
     * @return pointer to the allocated memory
     */
    void *checked_calloc(size_t count, size_t size);

    /**
     * Checked version of `realloc`, aborts if memory could not be reallocated.
     *
     * @param ptr the pointer to the originally allocated memory
     * @param size the size of the memory to allocate instead
     * @return pointer to the reallocated memory
     */
    void *checked_realloc(void *ptr, size_t size);

    /**
     * Computes the log2 of a number, rounding up if it's not exact.
     *
     * @param[in] x  the value to compute the log2 for
     * @return ceil(log2(x))
     */
    uint16_t ceil_log2(uint16_t x);

#ifdef __cplusplus
}
#endif

#endif /* MISC_H */

