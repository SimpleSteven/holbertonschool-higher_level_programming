#include "hash_tables.h"

/**
 * hash_table_set - add or update a new element to the hash table
 * @ht: the hash table
 * @key: the key of the element to add or update
 * @value: the value of the element
 * Return: 1 if success, 0 otherwise
 */


int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	if (!key)
		return 0;
	unsigned int index = key_index((const unsigned char *)key, ht->size);
	hash_node_t *new_node = malloc(sizeof(hash_node_t));
	if (new_node == NULL)
		return 0;
	new_node->key = (char *)key;
	new_node->value = (char *)value;
	new_node->next = NULL;
	if (ht->array[index])
	{
		ht->array[index]->next = NULL;
		new_node->next = ht->array[index]->next;
		ht->array[index] = new_node;
	}
	else
		ht->array[index] = new_node;
	return 1;
}

