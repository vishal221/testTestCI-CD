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
<<<<<<< HEAD
                sh 'sudo docker system prune -a -f'
=======
                sh 'docker system prune -a -f'
>>>>>>> ea30f59e19af9118b74f5d347f10a144e538b6c1
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
                   git config --global user.email "nfeugene86@gmail.com"
                   git config --global user.name "nathanforester"
                   git remote set-url origin git@github.com:nathanforester/testTestCI-CD.git
                   '''
            }
        }

        stage('merge feature to dev') {
            steps {
                sh '''
                   git checkout origin/dev
                   git merge origin/featureA
                   git add .
                   git commit -m "testing merge"
                   git push origin HEAD:dev
                   '''
            }
        }

        stage ('merge dev to main') {
            steps {
                sh '''
                   git checkout origin/main
                   git merge origin/dev
                   git push origin HEAD:main
                   '''
            }
        }

        stage('connect via ssh deploy server') {
            steps {
                sh '''
                   #!/bin/bash
                   ssh -i /home/jenkins/.ssh/myKey -o StrictHostKeyChecking=no ubuntu@172.31.38.195 << EOF
                   git clone https://github.com/nathanforester/testTestCI-CD.git
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
