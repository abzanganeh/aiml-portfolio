#!/bin/bash

# Jenkins Security Verification Script
# This script helps verify that the Jenkins security fix is working properly

echo "🔍 Jenkins Security Verification"
echo "Checking if distributed builds are properly configured..."
echo ""

# Function to check if Jenkins is accessible
check_jenkins_url() {
    local jenkins_url="$1"
    if curl -s --connect-timeout 5 "$jenkins_url" > /dev/null; then
        return 0
    else
        return 1
    fi
}

# Try to detect Jenkins URL
JENKINS_URLS=(
    "http://localhost:8080"
    "http://127.0.0.1:8080"
    "http://$(hostname):8080"
)

JENKINS_URL=""
for url in "${JENKINS_URLS[@]}"; do
    if check_jenkins_url "$url"; then
        JENKINS_URL="$url"
        echo "✅ Found Jenkins at: $JENKINS_URL"
        break
    fi
done

if [ -z "$JENKINS_URL" ]; then
    echo "❌ Could not find Jenkins instance"
    echo "Please provide your Jenkins URL manually"
    exit 1
fi

echo ""
echo "🔧 Security Configuration Checklist:"
echo ""

# Check 1: Docker availability
echo "1. 🐳 Docker Agent Setup:"
if command -v docker &> /dev/null; then
    echo "   ✅ Docker is installed"
    
    if docker images | grep -q "jenkins-agent:portfolio"; then
        echo "   ✅ Jenkins agent Docker image exists"
    else
        echo "   ⚠️  Jenkins agent Docker image not found"
        echo "      Run: ./setup_jenkins_security.sh"
    fi
    
    if docker ps &> /dev/null 2>&1; then
        echo "   ✅ Docker is accessible"
    else
        echo "   ❌ Docker daemon not accessible"
        echo "      Check Docker permissions or restart Docker service"
    fi
else
    echo "   ❌ Docker not installed"
    echo "      Install Docker first: sudo apt install docker.io"
fi

echo ""
echo "2. 📋 Jenkinsfile Configuration:"
if [ -f "Jenkinsfile" ]; then
    if grep -q "agent.*docker" Jenkinsfile; then
        echo "   ✅ Jenkinsfile uses Docker agent"
    elif grep -q "agent any" Jenkinsfile; then
        echo "   ⚠️  Jenkinsfile still uses 'agent any'"
        echo "      Should be updated to use specific agent label"
    else
        echo "   ❓ Jenkinsfile agent configuration unclear"
    fi
else
    echo "   ❌ Jenkinsfile not found"
fi

echo ""
echo "3. 🌐 Manual Jenkins Web UI Checks Required:"
echo "   (These must be verified manually in Jenkins web interface)"
echo ""
echo "   a. Built-in Node Disabled:"
echo "      • Go to: Manage Jenkins → Nodes and Clouds"
echo "      • Click: Built-In Node → Configure"
echo "      • Verify: Number of executors = 0"
echo ""
echo "   b. Docker Plugin Installed:"
echo "      • Go to: Manage Jenkins → Manage Plugins"
echo "      • Verify: Docker Plugin is installed"
echo ""
echo "   c. Docker Cloud Configured:"
echo "      • Go to: Manage Jenkins → Configure System"
echo "      • Verify: Docker Cloud is configured with:"
echo "        - Docker Host URI: unix:///var/run/docker.sock"
echo "        - Agent Template with label 'docker'"
echo ""
echo "   d. Agent → Controller Access Control:"
echo "      • Go to: Manage Jenkins → Configure Global Security"
echo "      • Verify: 'Agent → Controller Access Control' is enabled"

echo ""
echo "4. 🧪 Testing Security Fix:"
echo "   • Run a Jenkins job"
echo "   • Check build console output"
echo "   • Verify job runs on Docker agent (not Built-In Node)"
echo "   • Security warning should disappear from Jenkins dashboard"

echo ""
echo "5. 📊 Version Tracking Test:"
if [ -f "version.json" ]; then
    current_version=$(grep '"version"' version.json | cut -d'"' -f4)
    echo "   ✅ Current version: $current_version"
    echo "   • After Jenkins build, check if live site shows this version"
    echo "   • This confirms both security fix AND deployment are working"
else
    echo "   ❌ version.json not found"
fi

echo ""
echo "🎯 Expected Results After Fix:"
echo "   ✅ No 'built-in node security' warnings in Jenkins"
echo "   ✅ Builds run on Docker agents, not built-in node"
echo "   ✅ Jenkins controller protected from build scripts"
echo "   ✅ Version tracking shows latest deployments"

echo ""
echo "📚 For detailed instructions, see:"
echo "   • JENKINS_SECURITY_FIX.md (comprehensive guide)"
echo "   • setup_jenkins_security.sh (automated setup)"

echo ""
echo "🆘 If builds stop working after security fix:"
echo "   1. Temporarily re-enable built-in node (set executors to 2)"
echo "   2. Check Docker agent configuration"
echo "   3. Verify Docker plugin is working"
echo "   4. Check agent connectivity in Jenkins"
