#include<stdio.h>
#include<malloc.h>
#include<math.h>
int *x,*y;
int m[50],div[50]; 
void gener(int *a,int *b);
void final();
int n;
main()
{
 int i,j;

printf("how many coordinate you want to enter\n");
scanf("%d",&n);
 x=(int*)calloc(n,sizeof(int));

 y=(int*)calloc(n,sizeof(int));

 for(i=0;i<n;i++)
  {
    printf("give x and y=\t");
    scanf("%d%d",&x[i],&y[i]);
  }

 if(n==2)
{
  printf("(%d,%d)",(x[0]+x[1])/2,(y[0]+y[1])/2);/*give one point on line between 2 point*/

}

else
 gener(x,y);
 
}



void gener(int *a,int *b)
{ 
   int e1,e2, i,k1=0,j,u,v;
 
 for(j=0;j<n-2;j++)
  {
  
        for(i=0;i<3;i++) 
   {
           /*to get distance between every pair of three  point*/
      e1=j+i;   
      e2=j+((i+1)%n);  
         u =(a[e1] - a[e2])*(a[e1] - a[e2]) ;

         v =(b[e1]-b[e2])*(b[e1]-b[e2]);
     
         m[k1]=sqrt(u+v);     
 
        div[j]+=m[k1]; /*to get sum of three side of triangle*/
  
  
        k1++;
 
    }   

 }
 final();

}

void final()
{
 int i,k2=0,j;
 float l,o,g=0,h=0;
 float num1[50],num2[50];
  
 for(j=0;j<n-2;j++)
 {
  
  for(i=0;i<3;i++) 
  {
    
    num1[j]*=m[j+i]*(x[2*j+3-(i+1)%n]);
   
     num2[j]*=m[j+i]*(y[2*j+3-(i+1)%n]);
   }

 }



	if(n==3)
	{
           l = num1[0]/div[0];
	   o = num2[0]/div[0];
          printf("point is = (%f,%f)\n",l,o);  
         
         }


  else
   {
     for(i=0;i<n;i++)     
     {      
       g+=num1[i]/div[i];          
       h+=num2[i]/div[i];
     }
     g=g/n;
     h=h/n;
     printf("point is = (%f,%f)",g,h);

   }




}
