#include <stdio.h>
#include <string.h>
#include <stack>

int check_palin(const char *s)
{
    std::stack<char> stack;
    
    for (int i = 0; i < strlen(s) / 2; i++) 
        stack.push(s[i]);

    for (int i = strlen(s) / 2 + (strlen(s) % 2 ? 1 : 0); i < strlen(s); i++, stack.pop()) 
        if (stack.top() != s[i]) return 0;

    return 1;
}

int main(void)
{
    char buf[102];

    fgets(buf, 102, stdin);
    buf[strlen(buf) - 1] = '\0';

    printf("%d\n", check_palin(buf));

    return 0;
}