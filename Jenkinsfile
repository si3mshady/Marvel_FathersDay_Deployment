job('Fathers Day Deployment' ) {
    
   description('Fathers Day Deployment')
    properties {
        githubProjectUrl('https://github.com/si3mshady/Marvel_FathersDay_Deployment')
    }
   

    scm {
        git('https://github.com/si3mshady/Marvel_Hero_FathersDay.git', 'main',Closure configure = null)

        // git(Closure configure = null, remote {             
        //         github('si3mshady/Marvel_Hero_FathersDay')
        //          credentialsId('github')
        //     })
      }          
            steps {
                shell('''aws ecr get-login-password --region us-east-2  | docker login --username AWS --password-stdin 530182258888.dkr.ecr.us-east-2.amazonaws.com''')
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
