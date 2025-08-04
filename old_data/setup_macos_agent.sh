#!/bin/bash

# macOS Jenkins Agent Setup Script
# This script sets up a Jenkins agent on macOS

if [ -z "$1" ]; then
    echo "❌ Error: Please provide your Jenkins URL"
    echo "Usage: $0 <jenkins-url>"
    echo "Example: $0 http://localhost:8080"
    exit 1
fi

JENKINS_URL="$1"
echo "🔧 Setting up Jenkins agent for macOS: $JENKINS_URL"

# Test Jenkins connectivity
if ! curl -s --connect-timeout 10 "$JENKINS_URL" > /dev/null; then
    echo "❌ Error: Cannot connect to Jenkins at $JENKINS_URL"
    echo "Please check the URL and ensure Jenkins is running"
    exit 1
fi

echo "✅ Jenkins is accessible at $JENKINS_URL"

# Create jenkins-agent user on macOS
echo "👤 Setting up jenkins-agent user..."
if ! id jenkins-agent &>/dev/null; then
    echo "Creating jenkins-agent user on macOS..."
    sudo dscl . -create /Users/jenkins-agent
    sudo dscl . -create /Users/jenkins-agent UserShell /bin/bash
    sudo dscl . -create /Users/jenkins-agent RealName "Jenkins Agent"
    sudo dscl . -create /Users/jenkins-agent UniqueID 502
    sudo dscl . -create /Users/jenkins-agent PrimaryGroupID 20
    sudo dscl . -create /Users/jenkins-agent NFSHomeDirectory /Users/jenkins-agent
    sudo createhomedir -c -u jenkins-agent
    echo "✅ jenkins-agent user created"
else
    echo "✅ jenkins-agent user already exists"
fi

# Create workspace directory
echo "📁 Setting up workspace..."
sudo mkdir -p /Users/jenkins-agent/workspace
sudo chown jenkins-agent:staff /Users/jenkins-agent/workspace

# Download agent JAR
echo "📥 Downloading Jenkins agent JAR..."
cd /Users/jenkins-agent
sudo -u jenkins-agent curl -o agent.jar "$JENKINS_URL/jnlpJars/agent.jar"

if [ $? -eq 0 ]; then
    echo "✅ Agent JAR downloaded successfully"
else
    echo "❌ Failed to download agent JAR"
    exit 1
fi

# Set up basic environment for macOS
echo "🔧 Setting up environment..."
sudo -u jenkins-agent bash -c "
    echo 'export PATH=\$PATH:/usr/local/bin:/opt/homebrew/bin' >> /Users/jenkins-agent/.bashrc
    echo 'export JAVA_HOME=\$JAVA_HOME' >> /Users/jenkins-agent/.bashrc
"

echo ""
echo "✅ macOS Jenkins agent setup complete!"
echo ""
echo "📋 Next Steps in Jenkins Web UI:"
echo "1. Go to: Manage Jenkins → Nodes and Clouds"
echo "2. Click: New Node"
echo "3. Configure:"
echo "   • Node name: macos-agent"
echo "   • Type: Permanent Agent"
echo "   • Remote root directory: /Users/jenkins-agent/workspace"
echo "   • Labels: macos same-machine"
echo "   • Launch method: Launch agent by connecting it to the controller"
echo "   • Use WebSocket: ✓ (checked)"
echo ""
echo "4. After creating the node, copy the connection command shown"
echo "5. Run the connection command as jenkins-agent user:"
echo "   sudo -u jenkins-agent java -jar /Users/jenkins-agent/agent.jar -jnlpUrl [URL] -secret [SECRET] -workDir /Users/jenkins-agent/workspace"
echo ""
echo "🔒 Security Benefits:"
echo "   ✅ Builds run as jenkins-agent user (not Jenkins controller user)"
echo "   ✅ Limited file system access"
echo "   ✅ Process isolation from Jenkins controller"
echo ""
echo "🎯 Update your Jenkinsfile to use:"
echo "   agent { label 'macos' }"
