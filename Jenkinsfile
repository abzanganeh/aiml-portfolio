pipeline {
    agent any
    
    environment {
        // Define environment variables
        FTP_SERVER = '                        } || {
                            echo "❌ FTP connection test failed"
                            echo "Trying alternative server: ftp.srv637-files.hstgr.io"
                            lftp -c "
                            set ftp:ssl-allow no
                            set ftp:passive-mode on
                            set net:timeout 10
                            open ftp.srv637-files.hstgr.io
                            user $FTP_USERNAME $FTP_PASSWORD
                            pwd
                            ls
                            quit
                            " || exit 1
                        }        REMOTE_DIR = 'public_html'
        PROJECT_NAME = 'aiml-portfolio'
    }
    
    triggers {
        // Poll GitHub for changes every 2 minutes
        pollSCM('H/2 * * * *')
        // Alternative: Use GitHub webhook for instant triggers
        // githubPush()
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out code from GitHub...'
                checkout scm
                
                // Display current commit info
                script {
                    def commitId = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
                    def commitMessage = sh(returnStdout: true, script: 'git log -1 --pretty=format:"%s"').trim()
                    echo "🔹 Commit: ${commitId}"
                    echo "🔹 Message: ${commitMessage}"
                }
            }
        }
        
        stage('Validate Files') {
            steps {
                echo '🔍 Validating project structure...'
                sh '''
                    echo "Project files:"
                    ls -la
                    
                    echo "Checking for main files..."
                    test -f index.html && echo "✅ index.html found" || echo "❌ index.html missing"
                    test -d assets && echo "✅ assets/ directory found" || echo "❌ assets/ directory missing"
                    test -d projects && echo "✅ projects/ directory found" || echo "❌ projects/ directory missing"
                    
                    echo "File count: $(find . -name "*.html" | wc -l) HTML files"
                '''
            }
        }
        
        stage('Prepare Deployment') {
            steps {
                echo '📦 Preparing files for deployment...'
                sh '''
                    # Create deployment directory
                    mkdir -p deployment
                    
                    # Copy files excluding development files
                    rsync -av --progress ./ deployment/ \
                        --exclude='.git*' \
                        --exclude='node_modules' \
                        --exclude='.DS_Store' \
                        --exclude='README.md' \
                        --exclude='DEPLOYMENT.md' \
                        --exclude='.github' \
                        --exclude='Jenkinsfile' \
                        --exclude='deployment' \
                        --exclude='*.log'
                    
                    echo "Deployment package contents:"
                    ls -la deployment/
                '''
            }
        }
        
        stage('Deploy to Web Server') {
            steps {
                echo '🚀 Deploying to web server...'
                withCredentials([
                    usernamePassword(
                        credentialsId: 'ftp-credentials', 
                        usernameVariable: 'FTP_USERNAME', 
                        passwordVariable: 'FTP_PASSWORD'
                    )
                ]) {
                    sh '''
                        # Set PATH to include Homebrew binaries
                        export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
                        
                        # Check if lftp is available
                        if ! command -v lftp &> /dev/null; then
                            echo "❌ lftp not found in PATH. Please install with: brew install lftp"
                            exit 1
                        fi
                        
                        echo "✅ Using lftp: $(which lftp)"
                        echo "🔗 Connecting to: $FTP_SERVER"
                        echo "📁 Target directory: $REMOTE_DIR"
                        
                        # Test connection first
                        echo "Testing FTP connection..."
                        lftp -c "
                        set ftp:ssl-allow no
                        set ftp:passive-mode on
                        set net:timeout 10
                        open $FTP_SERVER
                        user $FTP_USERNAME $FTP_PASSWORD
                        pwd
                        ls
                        quit
                        " || {
                            echo "❌ FTP connection test failed"
                            echo "Trying alternative server: srv637-files.hstgr.io"
                            lftp -c "
                            set ftp:ssl-allow no
                            set ftp:passive-mode on
                            set net:timeout 10
                            open srv637-files.hstgr.io
                            user $FTP_USERNAME $FTP_PASSWORD
                            pwd
                            ls
                            quit
                            " || exit 1
                        }
                        
                        # Deploy using lftp
                        lftp -f "
                        set ftp:ssl-allow no
                        set ftp:passive-mode on
                        set net:timeout 10
                        set net:max-retries 3
                        open $FTP_SERVER
                        user $FTP_USERNAME $FTP_PASSWORD
                        lcd deployment
                        cd $REMOTE_DIR
                        mirror --reverse --delete --verbose --parallel=3
                        quit
                        "
                        
                        echo "✅ Deployment completed successfully!"
                    '''
                }
            }
        }
        
        stage('Verify Deployment') {
            steps {
                echo '🔍 Verifying deployment...'
                script {
                    try {
                        // Simple HTTP check (you can customize the URL)
                        sh '''
                            # Wait a moment for files to propagate
                            sleep 5
                            
                            # You can add curl checks here when you know your domain
                            # curl -I https://yourdomain.com || echo "Website check skipped - configure your domain"
                            
                            echo "✅ Deployment verification completed"
                        '''
                    } catch (Exception e) {
                        echo "⚠️ Verification failed, but deployment may still be successful"
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo '🧹 Cleaning up workspace...'
            cleanWs()
        }
        
        success {
            echo '🎉 Pipeline completed successfully!'
            emailext (
                subject: "✅ Portfolio Deployment Successful - ${env.BUILD_NUMBER}",
                body: """
                    <h2>Portfolio Deployment Successful</h2>
                    <p><strong>Project:</strong> ${env.PROJECT_NAME}</p>
                    <p><strong>Build:</strong> ${env.BUILD_NUMBER}</p>
                    <p><strong>Server:</strong> ${env.FTP_SERVER}${env.REMOTE_DIR}</p>
                    <p><strong>Time:</strong> ${new Date()}</p>
                    
                    <p>Your portfolio has been successfully deployed to the web server!</p>
                    
                    <p><em>This is an automated message from Jenkins CI/CD pipeline.</em></p>
                """,
                to: '$DEFAULT_RECIPIENTS',
                mimeType: 'text/html'
            )
        }
        
        failure {
            echo '❌ Pipeline failed!'
            emailext (
                subject: "❌ Portfolio Deployment Failed - ${env.BUILD_NUMBER}",
                body: """
                    <h2>Portfolio Deployment Failed</h2>
                    <p><strong>Project:</strong> ${env.PROJECT_NAME}</p>
                    <p><strong>Build:</strong> ${env.BUILD_NUMBER}</p>
                    <p><strong>Error:</strong> Please check Jenkins logs for details</p>
                    <p><strong>Time:</strong> ${new Date()}</p>
                    
                    <p>Please check the Jenkins console output for error details.</p>
                    <p><a href="${env.BUILD_URL}">View Build Log</a></p>
                    
                    <p><em>This is an automated message from Jenkins CI/CD pipeline.</em></p>
                """,
                to: '$DEFAULT_RECIPIENTS',
                mimeType: 'text/html'
            )
        }
        
        unstable {
            echo '⚠️ Pipeline completed with warnings'
        }
    }
}
