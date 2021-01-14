#include "hash_tables.h"

/**
 * hash_table_create - create a hash table of a given size
 * @size: the size of the new hash table
 * Return: a pointer to the newly created hash table
 */


hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *new_hash = malloc(sizeof(hash_table_t));
	if (new_hash == NULL)
		return NULL;
	new_hash->array = malloc(sizeof(hash_node_t*) * size);
	if (new_hash->array == NULL)
		return NULL;
	new_hash->size = size;
	return new_hash;
}
