pipeline {
    agent any
    parameters {
        booleanParam(name: 'Refresh',
                    defaultValue: false,
                    description: 'Read Jenkinsfile and exit.')
		    }
    stages {
        stage('Unit Tests') {
            steps {
                sh '''
                      python3 -m pytest ./prime/tests/test_unit.py
                   '''
            }
        }
        
        stage('Integration Tests') {
            steps {
                sh '''
                      python3 -m pytest ./main/tests/test_unit.py
                   '''
            }
        }
        stage('docker prune') {
            steps {
                sh 'docker system prune -a -f'
            }
        }

        stage('docker compose') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('connect via ssh deploy server') {
            steps {
                sh '''
                   #!/bin/bash
                   ssh -i /home/jenkins/.ssh/myKey -o StrictHostKeyChecking=no ubuntu@172.31.38.195 << EOF
                   sudo docker-compose -f /home/ubuntu/myDir/docker-compose.yaml down
                   sudo docker system prune -a -f
                   sudo docker-compose -f /home/ubuntu/myDir/docker-compose.yaml up -d
                   sudo rm -R /home/ubuntu/testTestCI-CD
                   << EOF
                '''
            }
        }
        
    }
}
