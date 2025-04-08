/** [덱]
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef int data_t;

typedef struct deque_node_ {
    data_t data;

    struct deque_node_ *prev;
    struct deque_node_ *next;
} *deque_node;

typedef struct deque_ {
    deque_node head;
    deque_node tail;

    ssize_t size;
} *deque;

deque create_deque(void);
void free_deque(deque dq);
void push_front(deque dq, data_t d);
void push_back(deque dq, data_t d);
data_t pop_front(deque dq);
data_t pop_back(deque dq);
ssize_t size(deque dq);
ssize_t empty(deque dq);
data_t front(deque dq);
data_t back(deque dq);

int main(void)
{
    deque dq = create_deque();
    unsigned int N;
    data_t data;
    char command[11];

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%10s", command);
        
        if (!strcmp(command, "push_front")) {
            scanf("%d", &data);
            push_front(dq, data);
        } else if (!strcmp(command, "push_back")) {
            scanf("%d", &data);
            push_back(dq, data);
        } else if (!strcmp(command, "pop_front")) {
            printf("%d\n", pop_front(dq));
        } else if (!strcmp(command, "pop_back")) {
            printf("%d\n", pop_back(dq));
        } else if (!strcmp(command, "size")) {
            printf("%ld\n", size(dq));
        } else if (!strcmp(command, "empty")) {
            printf("%ld\n", empty(dq));
        } else if (!strcmp(command, "front")) {
            printf("%d\n", front(dq));
        } else if (!strcmp(command, "back")) {
            printf("%d\n", back(dq));
        }
    }

    free_deque(dq);
    return 0;
}

deque create_deque(void)
{
    deque new_dq = malloc(sizeof(struct deque_));

    new_dq->head = NULL;
    new_dq->tail = NULL;
    new_dq->size = 0;

    return new_dq;
}

void free_deque(deque dq)
{
    while (dq->size != 0) {
        pop_front(dq);
    }

    free(dq);
}

void push_front(deque dq, data_t d)
{
    deque_node new_node = malloc(sizeof(struct deque_node_));

    new_node->data = d;
    new_node->prev = NULL;
    new_node->next = dq->head;

    if (dq->head == NULL) {
        dq->head = new_node;
        dq->tail = new_node;
    } else {
        dq->head->prev = new_node;
        dq->head = new_node;
    }
    
    dq->size++;
}

void push_back(deque dq, data_t d)
{
    deque_node new_node = malloc(sizeof(struct deque_node_));

    new_node->data = d;
    new_node->prev = dq->tail;
    new_node->next = NULL;

    if (dq->tail == NULL) {
        dq->head = new_node;
        dq->tail = new_node; 
    } else {
        dq->tail->next = new_node;
        dq->tail = new_node;
    }
    
    dq->size++;
}

data_t pop_front(deque dq)
{
    if (dq->head == NULL) {
        return -1;
    }

    deque_node old = dq->head;
    data_t data = old->data;

    dq->head = old->next;

    if (dq->head != NULL) {
        dq->head->prev = NULL;
    } else {
        dq->tail = NULL;
    }

    dq->size--;
    free(old);

    return data;
}

data_t pop_back(deque dq)
{
    if (dq->tail == NULL) {
        return -1;
    }

    deque_node old = dq->tail;
    data_t data = old->data;

    dq->tail = old->prev;

    if (dq->tail != NULL) {
        dq->tail->next = NULL;
    } else {
        dq->head = NULL;
    }

    dq->size--;
    free(old);

    return data;
}

data_t front(deque dq)
{
    return dq->size != 0 ? dq->head->data : -1;
}

data_t back(deque dq)
{
    return dq->size != 0 ? dq->tail->data : -1;
}

ssize_t size(deque dq)
{
    return dq->size;
}

ssize_t empty(deque dq)
{
    return dq->size == 0 ? 1 : 0;
}