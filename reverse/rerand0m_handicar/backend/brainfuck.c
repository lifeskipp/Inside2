#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define OP_END          0
#define OP_INC_DP       1
#define OP_DEC_DP       2
#define OP_INC_VAL      3
#define OP_DEC_VAL      4
#define OP_OUT          5
#define OP_IN           6
#define OP_JMP_FWD      7
#define OP_JMP_BCK      8

#define SUCCESS         0
#define FAILURE         1

#define PROGRAM_SIZE    4096
#define STACK_SIZE      512
#define DATA_SIZE       65535

#define STACK_PUSH(A)   (STACK[SP++] = A)
#define STACK_POP()     (STACK[--SP])
#define STACK_EMPTY()   (SP == 0)
#define STACK_FULL()    (SP == STACK_SIZE)

#define VERB 0

struct instruction_t {
	unsigned short operator;
	unsigned short operand;
};

static struct instruction_t PROGRAM[PROGRAM_SIZE];
static unsigned short STACK[STACK_SIZE];
static unsigned int SP = 0;

static int admin = 0;

int add_user(char *l, char *p) {
	FILE *f;

	f = fopen("db", "a");

	fwrite("\n", 1, 1, f);
	fwrite(l, 1, strlen(l) + 1, f);
	fwrite("\n", 1, 1, f);
	fwrite(p, 1, strlen(p) + 1, f);

	fclose(f);

	return 0;
}

int auth(char *l, char *p) {
	FILE *f;
	char login[25];
	char password[25];
	char c = 1, i;

	f = fopen("db", "r");
	if (f == NULL) {
		if (errno == ENOENT) {
			goto f;
		}
		perror("fail: ");
	}
#if VERB
	printf("auth %s %s\n", l, p);
#endif

	memset(login, 0, sizeof(login));
	memset(password, 0, sizeof(password));

	while (strncmp(l, login, sizeof(login)) != 0 &&
			strncmp(p, password, sizeof(password)) != 0) {
#if VERB
		printf("read %s %s\n", login, password);
#endif

		if (c == EOF) {
			goto f;
		}

		memset(login, 0, sizeof(login));
		memset(password, 0, sizeof(password));

		//read login
		i = 0;
		while ((c = getc(f)) != EOF && c != '\n' && i < sizeof(password)) {
			login[i++] = c;
		}
		if (c == EOF) {
			goto f;
		}
		while (c != '\n' && c != EOF) {
			c = getc(f);
		}

		//read password
		i = 0;
		while ((c = getc(f)) != EOF && c != '\n' && i < sizeof(password)) {
			password[i++] = c;
		}
		while (c != '\n' && c != EOF) {
			c = getc(f);
		}
	}

	fclose(f);
	return 1;
f:
	fclose(f);
	return 0;
}

int compile_bf(char *str) {
	unsigned short pc = 0, jmp_pc;
	unsigned int i = 0;
	char c;
	while ((c = *(str++)) != 0 && pc < PROGRAM_SIZE) {
		switch (c) {
			case '>': PROGRAM[pc].operator = OP_INC_DP; break;
			case '<': PROGRAM[pc].operator = OP_DEC_DP; break;
			case '+': PROGRAM[pc].operator = OP_INC_VAL; break;
			case '-': PROGRAM[pc].operator = OP_DEC_VAL; break;
			case '.': PROGRAM[pc].operator = OP_OUT; break;
			case ',': PROGRAM[pc].operator = OP_IN; break;
			case '[':
				PROGRAM[pc].operator = OP_JMP_FWD;
				if (STACK_FULL()) {
					return FAILURE;
				}
				STACK_PUSH(pc);
				break;
			case ']':
				if (STACK_EMPTY()) {
					return FAILURE;
				}
				jmp_pc = STACK_POP();
				PROGRAM[pc].operator =  OP_JMP_BCK;
				PROGRAM[pc].operand = jmp_pc;
				PROGRAM[jmp_pc].operand = pc;
				break;
			default: pc--; break;
		}
		pc++;
	}
	if (!STACK_EMPTY() || pc == PROGRAM_SIZE) {
		return FAILURE;
	}
	PROGRAM[pc].operator = OP_END;
	return SUCCESS;
}

int execute_bf(char **resp) {
	unsigned short data[DATA_SIZE], pc = 0;
	unsigned int ptr = DATA_SIZE;
	while (--ptr) { data[ptr] = 0; }
	while (PROGRAM[pc].operator != OP_END && ptr < DATA_SIZE) {
		switch (PROGRAM[pc].operator) {
			case OP_INC_DP: ptr++; break;
			case OP_DEC_DP: ptr--; break;
			case OP_INC_VAL: data[ptr]++; break;
			case OP_DEC_VAL: data[ptr]--; break;
			case OP_OUT: putchar(data[ptr]); break;
			case OP_IN: data[ptr] = (unsigned int)getchar(); break;
			case OP_JMP_FWD: if(!data[ptr]) { pc = PROGRAM[pc].operand; } break;
			case OP_JMP_BCK: if(data[ptr]) { pc = PROGRAM[pc].operand; } break;
			default: return FAILURE;
		}
		pc++;
	}
	if (ptr >= DATA_SIZE) {
		return FAILURE;
	}
	if ((char)data[1] == 'A' && (char)data[2] == 'U') {
		//add user
		char uu[25];
		char ppp[25];
		int i;
		memset(uu, 0, sizeof(uu));
		memset(ppp, 0, sizeof(ppp));
		for (i = 0; i < sizeof(uu-1) && data[3+i]; ++i) {
			uu[i] = data[3+i];
		}
		for (i = 0; i < sizeof(ppp-1) && data[3+i]; ++i) {
			ppp[i] = data[3+i];
		}
		add_user(uu, ppp);
	} else if ((char)data[1] == 'G' && (char)data[2] == '1') {
		//get param 1
		strcpy(*resp, "Check engine... OK!\n");
	} else if ((char)data[1] == 'G' && (char)data[2] == '2') {
		//get param 2
		FILE *f;
		char mileage[25];

		f = fopen("mil", "r");
		memset(mileage, 0, sizeof(mileage));
		fread(mileage, 1, sizeof(mileage), f);
		fclose(f);
		sprintf(*resp, "Mileage: %s\n", mileage);
	} else if ((char)data[1] == 'G' && (char)data[2] == '3') {
		//get param 3
		strcpy(*resp, "0.25 0.27 0.25 0.24 0.24 0.23\n");
	} else if (admin && (char)data[1] == 'F' && (char)data[2] == 'L' &&
			(char)data[3] == 'A' && (char)data[4] == 'G') {
		strcpy(*resp, "ELON{1_4m_4_70p_n07ch_m3ch4n1c}\n");
	} else if (admin && (char)data[1] == 'S' && (char)data[2] == '2') {
		//set param 2
		FILE *f;
		char mileage[25], i;

		while (i < sizeof(mileage) && data[i+1] != 0) {
			mileage[i] = (char)data[i+1];
		}

		f = fopen("mil", "w");
		fwrite(mileage, 1, sizeof(mileage), f);
		fclose(f);
		sprintf(*resp, "OK\n");
	} else if ((char)data[1] == 'S' && (char)data[2] == '2') {
		strcpy(*resp, "unauthorized\n");
	} else if ((char)data[1] == 'F' && (char)data[2] == 'L' &&
			(char)data[3] == 'A' && (char)data[4] == 'G') {
		strcpy(*resp, "unauthorized\n");
	} else {
		strcpy(*resp, "cmd unrecognized\n");
	}
	return 0;
}

int main() {
	char login[255], password[255];
	char *cmd = (char*) malloc(PROGRAM_SIZE);
	int ret;

	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

#if VERB
	printf("Welcome to the car's internal diagnostic system!\n");
#endif


#if VERB
	printf("login:\n");
#endif
	scanf("%s", login);
	if (strlen(login) > 25) {
		printf("501\n");
		exit(1);
	}

#if VERB
	printf("password:\n");
#endif
	scanf("%s", password);
	if (strlen(password) > 25) {
		printf("501\n");
		exit(1);
	}
	admin = auth(login, password);

	printf("200\n");

#if VERB
	printf("Ok, give me a program:\n");
#endif
	scanf("%s", cmd);
	if (strlen(cmd) > PROGRAM_SIZE) {
		printf("502\n");
		exit(1);
	}

#if VERB
	printf("precompile\n");
#endif
	ret = compile_bf(cmd);
	if (ret != SUCCESS) {
		printf("503\n");
		exit(1);
	}
#if VERB
	printf("postcompile\n");
#endif

	ret = execute_bf((char**)(&cmd));
	if (ret != SUCCESS) {
		printf("504\n");
		exit(1);
	}
	printf("%s", cmd);
	free(cmd);
}
