job('Fathers Day Deployment' ) {
    
   description('Fathers Day Deployment')

   

    scm {
        git('https://github.com/si3mshady/Marvel_Hero_FathersDay.git', 'main')
        

    }          
            steps {
                shell(

                    '''aws ecr get-login-password --region us-east-2 | sudo docker login --username AWS \
                    --password-stdin 8888888.dkr.ecr.us-east-2.amazonaws.com'''
                    
                )
            }
    

     steps {
        shell("""        
            
            #aws ecr create-repository --repository-name si3mshady-projects -region us-east-1
            #aws ecr get-login-password --region us-east-2 | sudo docker login --username AWS \
            #--password-stdin 8888888.dkr.ecr.us-east-2.amazonaws.com
            #sudo docker build . -t si3mshady/workspace-user
            #sudo docker tag 70f119814140  538258888.dkr.ecr.us-east-2.amazonaws.com/si3mshady-projects:<custom_tag>
            #sudo docker push  538258888.dkr.ecr.us-east-2.amazonaws.com/si3mshady-projects:<custom_tag>
                    
        """)
    }
}
