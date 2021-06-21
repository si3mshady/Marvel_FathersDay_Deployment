job('Fathers Day Deployment' ) {
    
   description('Fathers Day Deployment')

   scm {
            git('https://github.com/si3mshady/Marvel_FathersDay_Deployment', 'main')
        }
    
    
    steps {
        

        shell('''pip3  install aws-sam-cli 
                apt-get -y install  \
                apt-transport-https \
                ca-certificates \
                curl \
                gnupg \
                lsb-release 
                curl -fsSL https://download.docker.com/linux/debian/gpg |  gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg''')
    }

     steps {
        shell('''sam build  && \\
            latest_image=$(docker images | head -2 | awk '{print $3}' | column | awk '{print $2}')  && \\                          
            docker tag $latest_image  530182258888.dkr.ecr.us-east-2.amazonaws.com/si3mshady-projects:fathers_day && \\
            docker push  530182258888.dkr.ecr.us-east-2.amazonaws.com/si3mshady-projects:fathers_day''')
    }

    steps {
        shell('sam deploy --image-repository 530182258888.dkr.ecr.us-east-2.amazonaws.com/si3mshady-projects')
    }
}
