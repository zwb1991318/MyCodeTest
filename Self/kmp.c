/*
*在t字符串中查找p子串
*/
int KMP (char * t,char * p,int *next)
{
    int i =0 ,j = 0;

    while (i < strlen(t) && j < strlen(p))
    {
        if(j = -1 || t[i] == p[j])
        {
            i++;
            j++;
        }
        else
        {
            //next数组根据PMT（部分匹配表）计算得出
            j = next[j];
        }
    }

    //p长度完全匹配
    if(j == strlen(p))
    {
        return i - j;
    }
    else
    {
        return -1;
    }
}

int * getNext(char *p)
{
    static next[100] = {0};
    int i = 0,j = -1;
    //便于程序计算将next[0]直接赋值为-1
    next[0] = -1;

    while (i < strlen(p))
    {
        if(j == -1 || p[i] == p[j])
        {
            ++i;++j;
            next[i] = j;
        }
        else
        {
            j = next[j];
        }
    }
}
