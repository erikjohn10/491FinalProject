pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python' 
                }
            }
            steps {
                sh 'python -m py_compile game.py blackjack.py Player.py Card.py Dealer.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
    }
}
