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
                sh 'sudo docker-compose build'
            }
        }

        stage('git credentials') {
            steps {
                sh '''
                   git config --global user.email "vishalsaraya@outlook.com"
                   git config --global user.name "vishalsaraya"
                   git remote set-url origin git@github.com:vishal221/testTestCI-CD.git
                   '''
            }
        }

        stage('merge feature to dev') {
            steps {
                sh '''
                   git checkout -f dev
                   git merge origin/featureA
                   git push origin HEAD:dev
                   '''
            }
        }

        stage ('merge dev to main') {
            steps {
                sh '''
                   git checkout -f origin/main
                   git merge origin/dev
                   git push origin HEAD:main
                   '''
            }
        }

        stage('connect via ssh deploy server') {
            steps {
                sh '''
                   #!/bin/bash
                   ssh -i /home/jenkins/.ssh/myKey -o StrictHostKeyChecking=no ubuntu@172.31.43.217 << EOF
                   git clone https://github.com/vishal221/testTestCI-CD.git
                   sudo docker-compose -f /home/ubuntu/testTestCI-CD/docker-compose.yaml down
                   sudo docker system prune -a -f
                   sudo docker-compose -f /home/ubuntu/testTestCI-CD/docker-compose.yaml up -d
                   sudo rm -R /home/ubuntu/testTestCI-CD
                   << EOF
                '''
            }
        }
        
    }
}// some text
