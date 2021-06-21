job('Fathers Day Deployment' ) {
    
   description('Fathers Day Deployment')

   scm {
            git('https://github.com/si3mshady/Marvel_FathersDay_Deployment', 'main')
        }
    
    
    steps {       

        shell('''pip3  install aws-sam-cli
        sam build 
        sam deploy''')
    }

    
}
