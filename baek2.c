#include<stdio.h>
#include<time.h>
#include<stdlib.h>
int catcherror(int **A[10][10], int x, int y)
{
	if (x >= 10 || y >= 10) return 0;
	if (x < 0 || y < 0) return 0;
	else if (A[x][y] == -1) return 1;
	return 0;
}
int check(int **A[10][10], int x, int y)
{
	int i, j, count = 0;
	for (i = x - 2; i < x + 3; i++)
	{
		for (j = y - 2; j < y + 3; j++)
		{
			count += catcherror(A, i, j);
		}
	}
	A[x][y] = count;
}

int main()
{
	int i, j;
	srand((unsigned)time(NULL));
	int **map[10][10] = { {0,}, };
	for (i = 0; i < 9; i++) map[rand() % 9][rand()*rand() % 9] = -1;
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		{
			if (map[i][j] == -1) printf("$ ");
			else {
				check(map, i, j);
				printf("%d ",map[i][j]);

			}
		}
		printf("\n");
	}

	return 0;
}