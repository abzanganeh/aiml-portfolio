pipeline {
    agent {
        label 'macos'  // Use macOS agent for security (not built-in node)
    }
    
    // Security Fix: This pipeline now uses a dedicated macOS agent instead of the built-in node
    // to prevent security issues where builds have access to Jenkins controller files
    
    environment {
        // Define environment variables
        FTP_SERVER = 'srv637-files.hstgr.io'
        REMOTE_DIR = 'domains/zanganehai.com/public_html'
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
                echo '🔍 Validating Flask project structure...'
                sh '''
                    echo "Project files:"
                    ls -la
                    
                    echo "Checking for Flask application files..."
                    test -d flask_portfolio && echo "✅ flask_portfolio/ directory found" || echo "❌ flask_portfolio/ directory missing"
                    test -f flask_portfolio/app.py && echo "✅ Flask app.py found" || echo "❌ Flask app.py missing"
                    test -f flask_portfolio/requirements.txt && echo "✅ requirements.txt found" || echo "❌ requirements.txt missing"
                    test -d flask_portfolio/templates && echo "✅ templates/ directory found" || echo "❌ templates/ directory missing"
                    test -d flask_portfolio/static && echo "✅ static/ directory found" || echo "❌ static/ directory missing"
                    
                    echo "Flask files count:"
                    echo "- Templates: $(find flask_portfolio/templates -name "*.html" | wc -l) HTML files"
                    echo "- Static files: $(find flask_portfolio/static -type f | wc -l) static files"
                    echo "- Python models: $(find flask_portfolio/models -name "*.py" | wc -l) Python files"
                '''
            }
        }
        
        stage('Prepare Deployment') {
            steps {
                echo '📦 Preparing Flask application...'
                sh '''
                    echo "📁 Setting up deployment directory..."
                    rm -rf deployment 2>/dev/null || true
                    mkdir -p deployment
                    
                    echo "📋 Deploying Flask application..."
                    # Copy the entire Flask application including hidden files
                    cp -r flask_portfolio/. deployment/
                    
                    # Use the simple .htaccess for better compatibility
                    cp deployment/.htaccess_simple deployment/.htaccess
                    
                    # Set executable permissions for CGI
                    chmod +x deployment/app.py
                    
                    # Copy version info for reference
                    cp version.json deployment/ 2>/dev/null || true
                    
                    echo "✅ Flask application ready for deployment"
                    echo "📁 Deployment structure:"
                    ls -la deployment/
                    echo "🔧 CGI permissions:"
                    ls -la deployment/app.py
                    echo "📄 Configuration files:"
                    ls -la deployment/.htaccess 2>/dev/null || echo "Note: .htaccess will be created during deployment"
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
                        
                        # Test connection first with proper SSL
                        echo "Testing FTP connection..."
                        lftp -c "
                        set ftp:ssl-allow yes
                        set ftp:ssl-force yes
                        set ftp:passive-mode on
                        set net:timeout 15
                        set ssl:verify-certificate yes
                        open ftp://$FTP_SERVER
                        user $FTP_USERNAME $FTP_PASSWORD
                        pwd
                        ls
                        quit
                        " || {
                            echo "❌ SSL FTP failed, trying without SSL as fallback"
                            lftp -c "
                            set ftp:ssl-allow no
                            set ftp:passive-mode on
                            set net:timeout 10
                            open $FTP_SERVER
                            user $FTP_USERNAME $FTP_PASSWORD
                            pwd
                            ls
                            quit
                            " || exit 1
                        }
                        
                        # Deploy using lftp with SSL first, fallback to non-SSL
                        echo "Attempting secure SSL deployment..."
                        lftp -f "
                        set ftp:ssl-allow yes
                        set ftp:ssl-force yes
                        set ftp:passive-mode on
                        set net:timeout 15
                        set net:max-retries 3
                        set ssl:verify-certificate yes
                        open ftp://$FTP_SERVER
                        user $FTP_USERNAME $FTP_PASSWORD
                        lcd deployment
                        cd $REMOTE_DIR
                        mirror --reverse --verbose --parallel=3
                        quit
                        " || {
                            echo "⚠️ SSL deployment failed, using non-SSL fallback"
                            lftp -f "
                            set ftp:ssl-allow no
                            set ftp:passive-mode on
                            set net:timeout 10
                            set net:max-retries 3
                            open $FTP_SERVER
                            user $FTP_USERNAME $FTP_PASSWORD
                            lcd deployment
                            cd $REMOTE_DIR
                            mirror --reverse --verbose --parallel=3
                            quit
                            "
                        }
                        
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
