#!/bin/bash

# Same-Machine Jenkins Agent Setup Script
# Run this with your Jenkins URL as an argument

if [ -z "$1" ]; then
    echo "❌ Error: Please provide your Jenkins URL"
    echo "Usage: $0 <jenkins-url>"
    echo "Example: $0 http://your-jenkins-server:8080"
    exit 1
fi

JENKINS_URL="$1"
echo "🔧 Setting up Jenkins agent for: $JENKINS_URL"

# Test Jenkins connectivity
if ! curl -s --connect-timeout 10 "$JENKINS_URL" > /dev/null; then
    echo "❌ Error: Cannot connect to Jenkins at $JENKINS_URL"
    echo "Please check the URL and ensure Jenkins is running"
    exit 1
fi

echo "✅ Jenkins is accessible at $JENKINS_URL"

# Download agent JAR
echo "📥 Downloading Jenkins agent JAR..."
cd /home/jenkins-agent
sudo -u jenkins-agent wget "$JENKINS_URL/jnlpJars/agent.jar"

if [ $? -eq 0 ]; then
    echo "✅ Agent JAR downloaded successfully"
else
    echo "❌ Failed to download agent JAR"
    exit 1
fi

# Install common tools for the agent user
echo "🔧 Installing common tools for jenkins-agent user..."
sudo apt update > /dev/null 2>&1
sudo apt install -y git python3 python3-pip nodejs npm curl unzip > /dev/null 2>&1

# Set up basic environment
sudo -u jenkins-agent bash -c "
    echo 'export PATH=\$PATH:/usr/local/bin' >> /home/jenkins-agent/.bashrc
    echo 'export JAVA_HOME=\$JAVA_HOME' >> /home/jenkins-agent/.bashrc
"

echo ""
echo "✅ Same-machine Jenkins agent setup complete!"
echo ""
echo "📋 Next Steps in Jenkins Web UI:"
echo "1. Go to: Manage Jenkins → Nodes and Clouds"
echo "2. Click: New Node"
echo "3. Configure:"
echo "   • Node name: same-machine-agent"
echo "   • Type: Permanent Agent"
echo "   • Remote root directory: /home/jenkins-agent/workspace"
echo "   • Labels: linux same-machine"
echo "   • Launch method: Launch agent by connecting it to the controller"
echo "   • Use WebSocket: ✓ (checked)"
echo ""
echo "4. After creating the node, copy the connection command shown"
echo "5. Run the connection command as jenkins-agent user:"
echo "   sudo -u jenkins-agent java -jar /home/jenkins-agent/agent.jar -jnlpUrl [URL] -secret [SECRET] -workDir /home/jenkins-agent/workspace"
echo ""
echo "🔒 Security Benefits:"
echo "   ✅ Builds run as jenkins-agent user (not Jenkins controller user)"
echo "   ✅ Limited file system access"
echo "   ✅ Process isolation from Jenkins controller"
echo ""
echo "🎯 Update your Jenkinsfile to use:"
echo "   agent { label 'same-machine' }"
