#include <stdio.h>
#define FOO_MACRO(x) ((x) * 2 + 3)

int foo(int a)
{
	int b;
	b = FOO_MACRO(a);
	return b;
}

int main(int argc, char const *argv[])
{
	printf("Hello world!\n");
	printf("%d\n", foo(12));
	return 0;
}
