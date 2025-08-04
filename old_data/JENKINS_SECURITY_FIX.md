# Jenkins Security Fix: Distributed Builds Setup

## Issue
**Warning:** "Building on the built-in node can be a security issue. You should set up distributed builds."

## Problem Explanation
- Jenkins is currently running builds on the built-in node (controller)
- This gives builds the same file system access as Jenkins itself
- Security risk: Malicious build scripts could access Jenkins configuration files
- Solution: Set up distributed builds using agents

## Quick Fix: Disable Built-in Node Executors

### Step 1: Access Jenkins Configuration
1. Go to Jenkins web interface
2. Navigate to **Manage Jenkins** → **Nodes and Clouds**
3. Click on **Built-In Node**
4. Click **Configure**

### Step 2: Disable Built-in Node
1. Set **Number of executors** to `0`
2. Click **Save**

**⚠️ Warning:** After this, builds won't run until you set up agents!

## Solution Options

### Option 1: Same Machine Agent (Quick Setup)
Run an agent on the same machine but as a different user for basic isolation:

```bash
# Create Jenkins agent user
sudo useradd -m -s /bin/bash jenkins-agent

# Create agent directory
sudo mkdir -p /home/jenkins-agent/workspace
sudo chown jenkins-agent:jenkins-agent /home/jenkins-agent/workspace

# Download agent JAR
cd /home/jenkins-agent
sudo -u jenkins-agent wget http://your-jenkins-url/jnlpJars/agent.jar
```

### Option 2: Docker Agent (Recommended)
Use Docker containers for complete isolation:

```bash
# Install Docker if not already installed
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker

# Add Jenkins user to docker group
sudo usermod -aG docker jenkins
```

### Option 3: Separate Machine Agent (Most Secure)
Set up agents on different machines entirely.

## Jenkins Agent Configuration

### Step 1: Create New Agent in Jenkins
1. Go to **Manage Jenkins** → **Nodes and Clouds**
2. Click **New Node**
3. Enter node name: `agent-1`
4. Select **Permanent Agent**
5. Configure:
   - **Remote root directory**: `/home/jenkins-agent/workspace`
   - **Labels**: `linux docker` (or appropriate labels)
   - **Launch method**: 
     - For same machine: "Launch agent by connecting it to the controller"
     - For Docker: "Docker"
     - For remote: "Launch agents via SSH"

### Step 2: Update Jenkinsfile
Update your pipeline to use specific agents:

```groovy
pipeline {
    agent {
        label 'linux'  // Use agent with 'linux' label
    }
    
    stages {
        stage('Build') {
            steps {
                // Your build steps
                sh 'echo "Building on agent node"'
            }
        }
        
        stage('Deploy') {
            steps {
                // Your deployment steps
                sh 'echo "Deploying from agent node"'
            }
        }
    }
}
```

## Quick Docker Agent Setup

### Create Docker Agent
```bash
# Create Dockerfile for Jenkins agent
cat > Dockerfile.jenkins-agent << EOF
FROM jenkins/inbound-agent:latest
USER root
RUN apt-get update && apt-get install -y \\
    git \\
    python3 \\
    python3-pip \\
    nodejs \\
    npm \\
    && rm -rf /var/lib/apt/lists/*
USER jenkins
EOF

# Build agent image
docker build -f Dockerfile.jenkins-agent -t jenkins-agent:latest .
```

### Configure Docker Plugin in Jenkins
1. Install **Docker Plugin** in Jenkins
2. Go to **Manage Jenkins** → **Configure System**
3. Add **Docker Cloud**:
   - **Docker Host URI**: `unix:///var/run/docker.sock`
   - **Docker Agent templates**:
     - **Labels**: `docker linux`
     - **Docker Image**: `jenkins-agent:latest`
     - **Instance Capacity**: `2`

## Verification Steps

### 1. Check Built-in Node is Disabled
- Go to **Manage Jenkins** → **Nodes and Clouds**
- Verify Built-In Node shows "0 executors"

### 2. Test Agent Connection
- Run a simple job to verify agent works
- Check job console output shows it's running on agent

### 3. Security Verification
```bash
# Test that agent can't access Jenkins home
# (This should fail when run on agent)
ls /var/lib/jenkins/  # Should not work from agent
```

## Emergency Rollback
If builds stop working:
1. Go to **Manage Jenkins** → **Nodes and Clouds**
2. Configure Built-In Node
3. Set **Number of executors** back to `2` (or original value)

## Benefits After Setup
✅ **Security**: Builds isolated from Jenkins controller  
✅ **Stability**: Controller protected from build failures  
✅ **Scalability**: Can add more agents as needed  
✅ **Compliance**: Follows Jenkins security best practices  

## Next Steps
1. Implement one of the agent options above
2. Update your Jenkinsfile to specify agent labels
3. Test deployment pipeline
4. Monitor for any issues
5. Consider adding more agents for redundancy

## Additional Security Measures
- Enable **Agent → Controller Access Control** (should be on by default)
- Regularly review agent permissions
- Use least-privilege principle for agent access
- Consider network isolation for agents
