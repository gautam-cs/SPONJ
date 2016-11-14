#include<stdio.h>
#include<math.h>
#include<string.h>
void push(int x);
int pop();
int calcu(int z,int a, int b);
char str[100];
int top=-1,stack[100],i,d;
int oprand1,oprand2,value,p; 
int main()
	{
	printf("enter the expression in prefix style\n");
	scanf("%s",str);
	p=strlen(str);
	for(i=p-1;i>=0;i--)
		{
			if(str[i]>=48 && str[i]<=57)
				{//printf("%c\n",str[i]);
				push(str[i]);	
				}
			else
			{
			oprand1=pop(stack)-48;
			oprand2=pop(stack)-48;printf("%d %d\n",oprand1,oprand2);			
			value=calcu(str[i],oprand1,oprand2);//printf("%d\n",value);
			push(value+48);
			}
		}
	printf("evaluated value of this infix expression = %d\n",value);
	return 0;
}
void push(int x)
	{
		top=top+1;
		stack[top]=x;
	}
int pop()
	{
		d=stack[top];
		top=top-1;
		return d;
	}
int calcu(int z,int a,int b)
	{
switch(z)
	{
		case '+' :{ return (a+b);break;}
		case '-' :{ return (a-b);break;}
		case '*' :{ return (a*b);break;}
		case '/' :{ return (a/b);break;}
		//case '$' : return (pow(a, b));
		default :
		 printf("wrong operator\n");
		
	}


	}
