FROM centos

ENV  AWS_ACCESS_KEY_ID=AIIUHJUYUY
ENV AWS_SECRET_ACCESS_KEY=IOIUUIHYUIUH
ENV AWS_DEFAULT_REGION=us-east-1

#install docker ... in docker 
RUN curl -fsSL https://get.docker.com/ | sh


RUN yum install -y openssh-server
RUN useradd remote_user && \
    echo "remote_user:1234" | chpasswd && \
    mkdir /home/remote_user/.ssh && \
    chmod 700 /home/remote_user/.ssh

#the command ssh-keygen was run and the key was named 'remote-key'
#ssh-keygen created a remote-key.pub and a remote-key

COPY remote-key.pub /home/remote_user/.ssh/authorized_keys

RUN chown remote_user:remote_user -R /home/remote_user/ && \
    chmod 600 /home/remote_user/.ssh/authorized_keys

RUN yum install epel-release -y  && \
    yum --enablerepo=extras install epel-release -y && \
    yum install python3-pip -y  && pip3 install awscli 


EXPOSE 22

RUN rm -rf /run/nologin

   
RUN ssh-keygen -A

CMD ["/usr/sbin/sshd","-D"] 

#docker cp remote-key jenkins:/tmp/remote-keyssh -I 
# <private_key_of_ssh_host>  user@host
