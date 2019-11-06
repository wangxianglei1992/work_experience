#include<pthread.h>
#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t  cond = PTHREAD_COND_INITIALIZER;  //init cond

void *thread1(void*);
void *thread2(void*);

int i = 1; //global

int main(void){
    pthread_t t_a;
    pthread_t t_b;//two thread

    pthread_create(&t_a,NULL,thread2,(void*)NULL);
    pthread_create(&t_b,NULL,thread1,(void*)NULL);  //Create thread

    printf("t_a:0x%x, t_b:0x%x:", t_a, t_b);
    pthread_join(t_b,NULL);//wait a_b thread end
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond);
   exit(0);
}

void *thread1(void *junk){
    for(i = 1;i<= 9; i++){
        pthread_mutex_lock(&mutex);
        printf("call thread1 \n");
        if(i%3 == 0)
            {
            pthread_cond_signal(&cond);  //send sianal to t_b
            printf("thread1:******i=%d\n", i);
            }
        else
            printf("thread1: %d\n", i);
        pthread_mutex_unlock(&mutex);

        printf("thread1: sleep i=%d\n", i);
        sleep(1);
        printf("thread1: sleep i=%d******end\n", i);
    }
}

void *thread2(void*junk){
    while(i < 9)
    {
        pthread_mutex_lock(&mutex);
        printf("call thread2 \n");
        if(i%3 != 0)
            pthread_cond_wait(&cond,&mutex);  //wait
        printf("thread2: %d\n",i);
        pthread_mutex_unlock(&mutex);

        printf("thread2: sleep i=%d\n", i);
        sleep(1);
        printf("thread2: sleep i=%d******end\n", i);
    }
}