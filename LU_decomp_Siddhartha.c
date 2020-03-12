//LU Decomposition
//Siddhartha
#include<stdio.h>
#include<gsl/gsl_linalg.h>
#include<gsl/gsl_matrix.h>
int main()
{
	float a[3][3]={{1, 0.67, 0.33}, {0.45, 1, 0.55},{0.67, 0.33, 1}}, U[3][3], L[3][3], P[3][3];
	gsl_matrix *A = gsl_matrix_alloc(3,3);
	gsl_permutation *p = gsl_permutation_alloc(3);
	int i, j;
	printf("A: \n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%.3f  ",a[i][j]);
		}
		printf("\n");
	}
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			gsl_matrix_set(A,i,j,a[i][j]);
		}
	}
	int n;
	gsl_linalg_LU_decomp(A, p, &n); //Doing the LU decomposition
	
	
	/***Getting U***/

	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			if(j<i)
			{
				U[i][j]=0.0;
			}
			else
			{
				U[i][j]=gsl_matrix_get(A,i,j);
			}
		}
		
	}
	
	/*Getting L*/

	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			if(j>i)
			{ 
				L[i][j]=0.0;
			}
			else if(i==j)
			{ 
				L[i][j]=1.0; 
					
			}
			else
			{ 
				L[i][j]=gsl_matrix_get(A,i,j); 
			}
		}
		printf("\n");
	}
	
	/*Getting P*/
	gsl_matrix *Unit=gsl_matrix_alloc(3,3);
	gsl_matrix_set_identity(Unit);
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			P[i][j]=gsl_matrix_get(Unit, i, gsl_permutation_get(p,j));
		}
	}
	

	/********PRINTING**********/
	printf("U:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%.3f  ",U[i][j]);
		}
		printf("\n");
	}
	
	printf("\nL:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%.3f\t",L[i][j]);
		}
		printf("\n");
	}
	
	printf("\nP:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%.3f\t",P[i][j]);
		}
		printf("\n");
	}
	
	



	/************CHECKING THE DECOMPOSITION************************/
	float Pa[3][3], LU[3][3];
	int k=0;
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			Pa[i][j]=0;
			LU[i][j]=0;
			for(k=0;k<3;k++)
			{
				Pa[i][j]+=P[i][k]*a[k][j];
				LU[i][j]+=L[i][k]*U[k][j];
			}
		}
	}
	printf("\nPA:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%.3f\t",Pa[i][j]);
		}
		printf("\n");
	}
	
	printf("\nLU:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%.3f\t",LU[i][j]);
		}
		printf("\n");
	}
	
	gsl_permutation_free(p);
	gsl_matrix_free(A);
	return 0;
}
