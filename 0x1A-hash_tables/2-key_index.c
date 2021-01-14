#include "hash_tables.h"

/**
 * key_index - a function that gives you the index of a key
 * @key: the string key to obtain the index
 * @size: the size of the hash table
 * Return: the index
 */


unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned int int_key = hash_djb2(key);
	return (int_key % size);
}

