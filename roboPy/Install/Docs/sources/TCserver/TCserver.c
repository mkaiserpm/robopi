/*
 * TCserver.c
 * (C) 2014 Dr. Alexander K. Seewald, Seewald Solutions
 * Authors: Georg Weissinger, Alexander K. Seewald
 * License: GPLv3  http://www.gnu.org/licenses/gpl-3.0.txt
 */

/* Formatting: tabstop=2 */

#include <wiringPi.h>
#include <wiringSerial.h>

#include <stdlib.h>
#include <ncurses.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <math.h>
#include <signal.h>
#include <unistd.h>


#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

int fd = -1;

void my_handler(int s) {

	if (fd!=-1) {
		int m0_=0;
		int m1_=0;

		serialPutchar(fd,0x88); // 0x88 = vorwaerts, 0x89 = rueckwaerts
		serialPutchar(fd,m0_);
		serialPutchar(fd,0x8C); // 0x8C = vorwaerts, 0x8D = rueckwaerts
		serialPutchar(fd,m1_);
		serialClose(fd);
		pwmWrite (18, 0);
	}
	
	system("killall raspivid");
	system("killall nc");
	printf("caught signal %d\n",s);

	exit(1);
}

int main(int argc , char *argv[])
{
	signal(SIGINT,my_handler);
	signal(SIGTERM,my_handler);
	signal(SIGQUIT,my_handler);
	signal(SIGHUP,my_handler);

	wiringPiSetupGpio();

	fd = serialOpen("/dev/ttyAMA0",38400);
	if (fd==-1) {
		printf("Problem opening serial port: %d\n",errno);
		return -1;
	}

	// set timeout to 262ms
	serialPutchar(fd,0x84);
	serialPutchar(fd,0x03);
	serialPutchar(fd,0x01);
	serialPutchar(fd,0x55);
	serialPutchar(fd,0x2a);

	delay(4);

	int ch = serialGetchar(fd);
	if (ch!=0) {
		printf("Problem setting timeout on Qik motor controller: %d\n",ch);
		return -1;
	}




  int socket_desc;
  struct sockaddr_in server;

  //Create socket
  socket_desc = socket(AF_INET , SOCK_STREAM | SOCK_NONBLOCK | SOCK_CLOEXEC , 0);
  if (socket_desc == -1) {
    printf("Could not create socket");
  }

  int optval = 1;
  setsockopt(socket_desc, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof(optval));

  memset( &server, 0, sizeof (server));

  server.sin_family = AF_INET;
  server.sin_addr.s_addr = htonl( INADDR_ANY );

  // Portnummer
  server.sin_port = htons( 5002 );

  if(bind( socket_desc, (struct sockaddr*)&server, sizeof( server)) < 0) {
  	printf("errno=%d (%s)\n",errno,strerror(errno));
    puts("connect error");
    return 1;
  }

  if( listen( socket_desc, 3 ) == -1 ) {
   	printf("errno=%d (%s)\n",errno,strerror(errno));
    puts("listen error");
    return 2;
  }

  puts("Connected");

  signed char message[2];
  int m0=0; int m1=0;
  float m0_0=0; float m1_1=0;
  int m0_=0; int m1_=0;

  pinMode(18,PWM_OUTPUT);
  pwmSetMode(PWM_MODE_MS);

  pwmSetClock(65);		// LED Frequency = 19.2MHz/Clock/Range ~ 200Hz
  pwmSetRange(128);

  struct sockaddr_in client;
  int sock2 = -1;
  socklen_t len = sizeof(client);

  int cnt=0;

  for (;;) {
  	if (sock2<0) {
   		sock2 = accept( socket_desc, (struct sockaddr*)&client, &len);
   	}
   	if (sock2>=0) {
   		int res = recv(sock2 , message , 2 , MSG_DONTWAIT);
   		if (res<0) {
   			if ((errno!=EAGAIN && errno!=EWOULDBLOCK)) {
   				printf("\nerrno=%d encountered.\n",errno);
   				system("killall raspivid");
   				system("killall nc");
   				close(sock2);
   				sock2=-1;
   				m0=m1=0;
   				pwmWrite (18, 0);
   				continue;
   			} else {
   				//printf("no data received - ok.\n");
   			}
   		} else {
   			if (res==2) {
   				puts("Data Recv\n");
   				printf("\n%d %d\n",message[0],message[1]); // VELOCITY, ROTATION

    			if (message[0]==-128 && message[1]==-128) {
        		system("raspivid -o - -rot 90 -t 0 -fps 20 -b 2500000 -h 1280 -w 720 | nc -l -p 5001 &");
    				
    				continue;
    			}
    				
    			if (message[0]==-128 && message[1]!=-128) {
			    	pwmWrite (18,message[1]);
	 	    		continue;		    
   				}
    				
    			// VELOCITY
    			int geschwindigkeit = message [0];
    			if (geschwindigkeit < -127)   geschwindigkeit = -127;
    			if (geschwindigkeit > 127) geschwindigkeit = 127;

    			float richtungl=1.0, richtungr=1.0;

    			// ROTATION
    			int d = message[1];

    			if (d==-127) {
						richtungl = 1.0;
 						richtungr =-1.0;
 					} else if (d==+127) {
						richtungl = -1.0;
 						richtungr =1.0;
 					} else if (d==0) {
						richtungl = 1.0;
 						richtungr = 1.0;
 					} else if(d>=0) {			// winkel +-126
						richtungr=1;
 						richtungl	 = 1 - (0.5/127)*d;

 						if(richtungl<-1) richtungl=0.5;
 						if(richtungr<0.5) richtungr=0.5;

					} else if(d<=0) {			// winkel +-126
						richtungr	 = 1+ (0.5/127)*d;
 						richtungl =1;

						if(richtungl<-1) richtungl=0.5;
 						if(richtungr<0.5) richtungr=0.5;
 					}

					// Send to motor controller

					m0 = (int)(roundf((float)geschwindigkeit*richtungl));
 					m1 = (int)(roundf((float)geschwindigkeit*richtungr));
   			} else {
   				printf("\nExpected %d, got %d bytes.\n",2,res);
   				close(sock2);
   				system("killall raspivid");
   				system("killall nc");
   				m0_=m1_=0;
   				pwmWrite (18, 0);
   				sock2=-1;
   				continue;
   			}
   		}
   	}

   	if (cnt%20 == 0) {
   		printf("."); fflush(stdout);
   	}
   	cnt++;
    	
   	m0_0 = m0_0 + 1.0/5.0*((float)m0-m0_0);
   	m1_1 = m1_1 + 1.0/5.0*((float)m1-m1_1);
    	
   	m0_ = (int)(roundf((float)m0_0));
   	m1_ = (int)(roundf((float)m1_1));

		if (m0_>=0) {
			serialPutchar(fd,0x88); // 0x88 = vorwaerts,
			serialPutchar(fd,m0_);
#ifdef DEBUG
			printf("Motor0 forward: %d\n",m0_);
#endif
		} else {
			serialPutchar(fd,0x8A); // 0x8A = rueckwaerts
			serialPutchar(fd,m0_*-1);
#ifdef DEBUG
			printf("Motor0 backward: %d\n",m0_*-1);
#endif
		}

		if(m1_>=0) {
			serialPutchar(fd,0x8C); // 0x8C = vorwaerts
			serialPutchar(fd,m1_);
#ifdef DEBUG
			printf("Motor1 forward: %d\n",m1_);
#endif
		} else {
			serialPutchar(fd,0x8E); //0x8E = rueckwaerts
			serialPutchar(fd,m1_*-1);
#ifdef DEBUG
			printf("Motor1 backward: %d\n",m1_*-1);
#endif
		}

    delay(10);
  }

  close(socket_desc);


  m0=0;
 	m1=0;

 	serialPutchar(fd,0x88); // 0x88 = vorwaerts, 0x89 = rueckwaerts
 	serialPutchar(fd,m0_);
 	serialPutchar(fd,0x8C); // 0x8C = vorwaerts, 0x8D = rueckwaerts
 	serialPutchar(fd,m1_);
    	
	system("killall raspivid");
	system("killall nc");

	pwmWrite (18, 0);

 	serialClose(fd);
  return 0;
}
