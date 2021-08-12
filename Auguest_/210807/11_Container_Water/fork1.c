#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>

int main(){
	
	srand(time(NULL));
	pid_t cid[4];
	int rcid[4], temp[4];
	int i, pid;
	for(i = 0; i < 4; i++){
		temp[i] = rand()%5 + 1; //1 ~ 4까지의 랜덤한 난수 생성하여 저장
	}
	pid = (int)getpid(); //부모 pid저장
	for(i = 0; i < 4; i++){
		if((int)getpid() == pid){
			cid[i] = fork(); //부모 프로세스가 자식 프로세스 4개 생성
			if(cid[i] < 0){
				perror("Fork error!\n");
				exit(1);
			}
		}
	}
	if(getpid() == pid) printf("PPID : %d\n", pid); //자식 프로세스 생성후 부모 프로세스 아이디 출력
	for(i = 0; i < 4; i++){
		if(cid[i] == 0){
			rcid[i] = (int)getpid();
			printf("Create Child Process ID : %d\n", rcid[i]); //자식 프로세스 아이디도 출력
			sleep(temp[i]); //random한 슬립 시간
			printf("CID %d terminated\n", rcid[i]); ///종료메세지 출력 후
			exit(temp[i]); //자식 프로세스 종료
		}
	}
	int sleeptime[4]; //잔 시간 status를 받아오는 int형 배열 선언
	for(i = 0; i < 4; i++){
		waitpid(cid[i], &sleeptime[i], 0); //모든 자식 프로세스가 종료될때까지 기다림
		printf("Child Process ID : %d, Sleep time : %d\n", cid[i], WEXITSTATUS(sleeptime[i])); // 이후 종료시마다 잔시간과 pid를 출력
	}
	printf("Parent Process(%d) terminated.\n", pid); //부모 프로세스 종료
	exit(0);
	

}
