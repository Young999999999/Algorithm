#include<stdio.h>
int main()
{
	int ADDH=0, ADDT=0, MINT=0, ADDO=0, MINO=0 ;
	int i,j,N,T,t=0;
	scanf("%d",&N);
	for(i=0;i<N;i++)
	{
		ADDH=0, ADDT=0, MINT=0, ADDO=0, MINO=0;
		scanf("%d",&T);
		
		while(T>=60)
		{
			T-=60;
			ADDH+=1;
		}
		if(T-10>=0) //두자릿 수     
		{
			if(T<=35)		//기존 10~39까지였던 것을  10~34로 변경
			{	
			ADDT=T/10;
				if(T%10>5) //한자릿 수가 5 이상일  
				{
					T=T%10;
					ADDT+=1;
					for(j=0;j<10-T;j++)
					{
						MINO+=1;
					}
				}
				if(T%10<=5) 
				{
					T=T%10;
					for(j=0;j<T;j++)
					{
						ADDO+=1;
					}
				}
			}
			if(T>35 && T<=39)
			{
				ADDH+=1;
				MINT=2;
				for(j=0;j<40-T;j++)	MINO+=1;
				
				
			}
			
			
			
			if(T/10==4)
			{
			ADDH+=1;
			MINT=2;
			if(T%10>=5)   
			{
				T=T%10;
				MINT-=1;
				for(j=0;j<10-T;j++)
				{
					MINO+=1;
				}
			}
			else
			{
				T=T%10;
				for(j=0;j<T;j++)
				{
					ADDO+=1;
				}
			}
			}
			
			
			if(T/10==5)
			{
			ADDH+=1;
			MINT=1;
			if(T%10>=5)  
			{
				T=T%10;
				MINT-=1;
				for(j=0;j<10-T;j++)
				{
					MINO+=1;
				}
			}
			else
			{
				T=T%10;
				for(j=0;j<T;j++)
				{
					ADDO+=1;
				}
			}
			}
		}
		
		
		
		else	// 한자릿 수 
		{
			if(T>5)   
			{
				ADDT+=1;
				for(j=0;j<10-T;j++)
				{
					MINO+=1;
				}
			}
			else
			{
				for(j=0;j<T;j++)
				{
					ADDO+=1;
				}
			}
		}
		
			printf("%d %d %d %d %d\n",ADDH,ADDT,MINT,ADDO,MINO);
		
	}	
}