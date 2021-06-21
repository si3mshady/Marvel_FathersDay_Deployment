job('Fathers Day Deployment' ) {
    
   description('Fathers Day Deployment')
    
    
    steps {
        shell('''whoami
                apt update
                id''')
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
