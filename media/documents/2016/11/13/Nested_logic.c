#include<stdio.h>

int main()
{
	int d,m,y,dd,mm,yy,a=0;
	scanf("%d %d %d",&dd,&mm,&yy);
	scanf("%d %d %d",&d,&m,&y);
	if(d>0 && d<=31 && dd>0 && dd<=31 && m>=1&& m<=12 && y>=1 && y<=3000){
    if(yy<y){
    printf("%d",a);
    }

    else if(yy>y){
    printf("10000");
    }

    else if(mm<m){
    printf("%d",a);
    }


    else if(mm>m){
    printf("%d",(mm-m)*500);
    }

    else if(dd<d){
    printf("%d",a);
    }

    else if(dd>d){
    printf("%d",(dd-d)*15);}
    else{
    printf("%d",a);
        }
        }
	return 0;
}
