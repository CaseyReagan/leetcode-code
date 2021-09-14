# include <stdio.h>
int main(void)
{
    int nums[10] = {0, 1, 1, 1, 2, 2, 4, 4, 6, 7};

    int n,count,num,i,j;
    int k=1;

    printf("input n\n");
    //scanf("%d",&n);
    n = 5;
    count = n;
    num = nums[0];

    for(i=1;;i++)
    {
        if(count > 1)
        {
            if(num == nums[k])
            {
                for(j=k;j<(sizeof(nums)/sizeof(int)-1);j++)
                    nums[j] = nums[j+1];
            }
            else
            {
                num = nums[k];
                k ++;
                count -= 1;
            }
        }
        else
            break;
    }

    printf("%d, nums = [",n);
    for(i=0;i<n;i++)
        printf("%d",nums[i]);
    printf("]\n");
}

