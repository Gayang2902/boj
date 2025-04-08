/** [큐]
 * 
 */

#include <stdio.h>
#include <string.h>

typedef struct queue_ {
    int data[10001];
    int size;
} queue;

queue q = {.size = 0};

int size(void)
{
    return q.size;
}

int empty(void)
{
    if (size() == 0) {
        return 1;
    } else {
        return 0;
    }
}

void push(int X)
{
    q.data[q.size++] = X;
}

void pop(void)
{
    if (empty()) {
        puts("-1");
        return;
    }
    printf("%d\n", q.data[0]);

    for (int i = 0; i < q.size - 1; i++) {
        q.data[i] = q.data[i + 1];
    }
    q.size--;
}

void front(void)
{
    if (empty()) {
        puts("-1");
        return;
    }

    printf("%d\n", q.data[0]);
}

void back(void)
{
    if (empty()) {
        puts("-1");
        return;
    }

    printf("%d\n", q.data[q.size - 1]);
}

int main(void)
{
    int N;
    int X;
    char command[6];

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%s", command);
        if (!strcmp(command, "push")) {
            scanf("%d", &X);
            push(X);
        } else if (!strcmp(command, "pop")) {
            pop();
        } else if (!strcmp(command, "size")) {
            printf("%d\n", size());
        } else if (!strcmp(command, "empty")) {
            printf("%d\n", empty());
        } else if (!strcmp(command, "front")) {
            front();
        } else if (!strcmp(command, "back")) {
            back();
        }
    }

    return 0;
}