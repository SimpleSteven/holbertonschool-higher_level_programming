#include "hash_tables.h"

/**
 * key_index - create a hash table of a given size
 * @key: the size of the new hash table
 * @size: the size of the new hash table
 * Return: a pointer to the newly created hash table
 */


unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	int int_key = hash_djb2(key);
	return (int_key % size);
}

