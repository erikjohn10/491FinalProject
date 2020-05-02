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
                sh 'python -m py_compile sources/game.py sources/blackjack.py sources/Player.py sources/Card.py sources/Dealer.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}
