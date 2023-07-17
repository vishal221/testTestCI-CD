pipeline {
    agent any
    parameters {
        booleanParam(name: 'Refresh',
                    defaultValue: false,
                    description: 'Read Jenkinsfile and exit.')
		    }
    stages {
        
        stage('Integration Tests') {
            steps {
                sh '''
                      python3 -m pytest ./prime/tests/test_unit.py
                   '''
            }
        }
        stage('docker prune') {
            steps {
                sh 'sudo docker system prune -a -f'
            }
        }

        stage('docker compose') {
            steps {
                sh 'sudo docker-compose build'
            }
        }

        // stage('connect via ssh deploy server') {
        //     steps {
        //         sh '''
        //            #!/bin/bash
        //            ssh -i /home/jenkins/.ssh/myKey -o StrictHostKeyChecking=no ubuntu@172.31.33.237 << EOF
        //            ansible-playbook -v /home/ubuntu/playbook.yaml
        //            docker-compose -f /home/ubuntu/API2/docker-compose.yaml down
        //            docker system prune -a -f
        //            docker-compose -f /home/ubuntu/API2/docker-compose.yaml up -d
        //            sudo rm -R /home/ubuntu/API2
        //            << EOF
        //         '''
        //     }
        // }
        
    }
}
