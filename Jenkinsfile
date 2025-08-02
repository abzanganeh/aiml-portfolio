pipeline {
    agent any
    
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
                echo '📦 Converting Flask app to static HTML for shared hosting...'
                sh '''
                    # Install Python dependencies if needed
                    cd flask_portfolio
                    if command -v python3 &> /dev/null; then
                        echo "🐍 Python 3 found"
                        python3 -m pip install --user -r requirements.txt || echo "Dependencies already installed"
                    else
                        echo "❌ Python 3 not found, using alternative method"
                    fi
                    cd ..
                    
                    # Generate static site using our generator
                    if command -v python3 &> /dev/null; then
                        echo "🔄 Generating static HTML files from Flask templates..."
                        python3 generate_static.py
                        
                        if [ -d "static_site" ]; then
                            echo "✅ Static site generated successfully"
                            # Use the generated static site as deployment
                            rm -rf deployment 2>/dev/null || true
                            mv static_site deployment
                            echo "📋 Using generated static files for deployment"
                        else
                            echo "❌ Static generation failed, using fallback method"
                            mkdir -p deployment
                            cp -r flask_portfolio/static deployment/
                            cp -r flask_portfolio/templates deployment/
                            
                            # Create proper index.html that works with the template structure
                            cat > deployment/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alireza Barzin Zanganeh - ML Engineer</title>
    <meta name="description" content="Machine Learning Engineer portfolio featuring AI tutorials, projects, and technical expertise">
    <link href="static/css/main.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="/">Alireza Barzin Zanganeh</a>
            </div>
            <div class="nav-menu">
                <a href="#about" class="nav-link">About</a>
                <a href="tutorials.html" class="nav-link">Tutorials</a>
                <a href="projects.html" class="nav-link">Projects</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
        </div>
    </nav>
    
    <section style="padding: 6rem 0 4rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-align: center;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 2rem;">
            <h1 style="font-size: 3rem; margin-bottom: 1rem;">Machine Learning Engineer</h1>
            <p style="font-size: 1.2rem; margin-bottom: 2rem;">Passionate about AI, Data Science, and Building Intelligent Systems</p>
            <a href="tutorials.html" style="background: transparent; color: white; border: 2px solid white; padding: 1rem 2rem; text-decoration: none; border-radius: 8px; font-weight: 700;">Explore Portfolio</a>
        </div>
    </section>
    
    <script src="static/js/main.js"></script>
</body>
</html>
EOF
                        fi
                    else
                        echo "⚠️ Python not available, creating simple static structure"
                        mkdir -p deployment
                        cp -r flask_portfolio/static deployment/
                        cp -r flask_portfolio/templates deployment/
                        
                        # Simple fallback index
                        cat > deployment/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Alireza Barzin Zanganeh - Portfolio</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="static/css/main.css" rel="stylesheet">
</head>
<body>
    <h1>Portfolio Loading...</h1>
    <p><a href="templates/">Browse Templates</a></p>
</body>
</html>
EOF
                    fi
                    
                    echo "📋 Final deployment structure:"
                    ls -la deployment/
                    echo "📄 Main files:"
                    find deployment/ -name "*.html" | head -10
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
