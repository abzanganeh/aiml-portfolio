#!/bin/bash

# Jenkins Security Fix: Setup Docker Agent
# This script helps set up a Docker-based Jenkins agent to fix the security warning

set -e

echo "🔧 Jenkins Security Fix: Setting up Docker Agent"
echo "This will fix the 'Building on the built-in node can be a security issue' warning"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Installing Docker..."
    
    # Install Docker (Ubuntu/Debian)
    if command -v apt &> /dev/null; then
        sudo apt update
        sudo apt install -y docker.io
        sudo systemctl start docker
        sudo systemctl enable docker
        echo "✅ Docker installed"
    else
        echo "❌ Please install Docker manually for your system"
        exit 1
    fi
else
    echo "✅ Docker is already installed"
fi

# Check if current user can run Docker
if ! docker ps &> /dev/null; then
    echo "⚠️  Current user cannot run Docker. Adding to docker group..."
    sudo usermod -aG docker $USER
    echo "⚠️  Please log out and log back in, then run this script again"
    exit 1
fi

echo ""
echo "🐳 Creating Jenkins Agent Docker Image..."

# Create Dockerfile for Jenkins agent
cat > Dockerfile.jenkins-agent << 'EOF'
FROM jenkins/inbound-agent:latest

# Switch to root to install packages
USER root

# Install common tools needed for builds
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    nodejs \
    npm \
    curl \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages commonly needed
RUN pip3 install --no-cache-dir \
    flask \
    requests \
    pyyaml

# Switch back to jenkins user
USER jenkins

# Set working directory
WORKDIR /home/jenkins/agent
EOF

# Build the agent image
echo "Building Jenkins agent Docker image..."
docker build -f Dockerfile.jenkins-agent -t jenkins-agent:portfolio .

if [ $? -eq 0 ]; then
    echo "✅ Jenkins agent Docker image built successfully"
else
    echo "❌ Failed to build Jenkins agent image"
    exit 1
fi

echo ""
echo "🎯 Next Steps to Complete Security Fix:"
echo ""
echo "1. 📝 Configure Jenkins (Web UI):"
echo "   • Go to Manage Jenkins → Manage Plugins"
echo "   • Install 'Docker Plugin' if not already installed"
echo "   • Go to Manage Jenkins → Configure System"
echo "   • Add Docker Cloud with these settings:"
echo "     - Docker Host URI: unix:///var/run/docker.sock"
echo "     - Add Docker Agent Template:"
echo "       * Labels: docker portfolio"
echo "       * Docker Image: jenkins-agent:portfolio"
echo "       * Instance Capacity: 2"
echo ""
echo "2. 🚫 Disable Built-in Node:"
echo "   • Go to Manage Jenkins → Nodes and Clouds"
echo "   • Click 'Built-In Node' → Configure"
echo "   • Set 'Number of executors' to 0"
echo "   • Save"
echo ""
echo "3. 📋 Update Jenkinsfile:"

cat << 'EOF'
pipeline {
    agent {
        label 'docker'  // Use Docker agent instead of built-in
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building on secure Docker agent"'
                sh 'python3 --version'
                sh 'node --version'
                // Your existing build steps
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'echo "Deploying from secure agent"'
                // Your existing deployment steps
            }
        }
    }
}
EOF

echo ""
echo "4. ✅ Test Security Fix:"
echo "   • Run a build job"
echo "   • Verify it runs on Docker agent (not built-in node)"
echo "   • Security warning should disappear"
echo ""
echo "🔒 Security Benefits:"
echo "   ✅ Builds isolated from Jenkins controller"
echo "   ✅ Build scripts can't access Jenkins configuration"
echo "   ✅ Controller protected from malicious code"
echo "   ✅ Follows Jenkins security best practices"
echo ""
echo "📚 For more details, see: JENKINS_SECURITY_FIX.md"

# Clean up
rm -f Dockerfile.jenkins-agent

echo ""
echo "🎉 Docker agent setup complete!"
echo "   Image: jenkins-agent:portfolio"
echo "   Next: Configure Jenkins web UI as described above"
