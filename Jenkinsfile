pipeline {
    agent none
    stages {
        stage('Tests') {
            matrix {
                agent { label "${NODENAME}" }
                axes {
                    axis {
                        name 'NODENAME'
                        values 'balfrin'
                    }
                }
                post {
                    always {
                        archiveArtifacts artifacts: 'log/**/*.log', allowEmptyArchive: true
                        deleteDir()
                    }
                }
                stages {
                    stage('Create environment') {
                        steps {
                            sh """
                            python3 -m venv .venv
                            source .venv/bin/activate
                            pip install pytest-xdist
                            """
                        }
                    }
                    stage('Unit Tests') {
                        steps {
                            sh """
                            source .venv/bin/activate
                            python3 test/unit_test.py
                            """
                        }
                    }
                    stage('Bootstrap spack') {
                        steps {
                            sh """
                            source .venv/bin/activate
                            source ./setup-env.sh
                            spack spec gnuconfig
                            """
                        }
                    }
                    stage('Integration Tests') {
                        steps {
                            sh """
                            source .venv/bin/activate
                            pytest -v -n auto test/integration_test.py
                            """
                        }
                    }
                    stage('System Tests') {
                        steps {
                            sh """
                            source .venv/bin/activate
                            source ./setup-env.sh /mch-environment/v6
                            pytest -v -n auto --maxprocesses=12 test/system_test.py
                            """
                        }
                    }
                }
            }
        }
    }
}
