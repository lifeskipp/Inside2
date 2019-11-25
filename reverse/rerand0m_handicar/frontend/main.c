#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
	int sock, i;
	struct sockaddr_in addr;
	char login[255], pass[255], buf[255];

	addr.sin_family = AF_INET;
	addr.sin_port = htons(1778);
	addr.sin_addr.s_addr = htonl((194 << 24) | (135 << 16) | (94 << 8) | 122);

	sock = socket(AF_INET, SOCK_STREAM, 0);
	if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
		perror("connect failed:");
		exit(1);
	}
	printf("login:\n");
	scanf("%s", login);
	i = strlen(login);
	login[i] = '\n';
	login[i+1] = 0;
	send(sock, login, strlen(login), 0);
	printf("password:\n");
	scanf("%s", pass);
	i = strlen(pass);
	pass[i] = '\n';
	pass[i+1] = 0;
	send(sock, pass, strlen(pass), 0);
	recv(sock, buf, sizeof(buf), 0);
	if (strncmp(buf, "200", 3) != 0) {
		printf("something wrong\n");
		close(sock);
		exit(1);
	}
	recv(sock, buf, sizeof(buf), 0);
	printf("Choose cmd:\n1.Check engine\n2.Get mileage\n3.Get engine param\n\n");
	scanf("%d", &i);
	switch(i) {
		case 1:
			send(sock, ">+++++++[<+++++++>-]<[>+>+<<-]>++++++++++++++++++++++\n", 54, 0);
			break;
		case 2:
			send(sock, ">+++++[<++++++++++>-]<[>+>+<<-]>+++++++++++++++++++++\n", 54, 0);
			break;
		case 3:
			send(sock, ">+++++++++++++++++[<+++>-]<[>+>+<<-]++++[>+++++<-]\n", 51, 0);
			break;
		default:
			printf("Hm.. Bye!\n");
			close(sock);
			return 0;
	}
	memset(buf, 0, sizeof(buf));
	recv(sock, buf, sizeof(buf), 0);
	printf("%s", buf);
	return 0;
}
