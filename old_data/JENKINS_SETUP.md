# Jenkins CI/CD Setup Guide

## Jenkins Pipeline for Auto-Deployment

This guide will help you set up Jenkins to automatically deploy your portfolio to `https://srv637-files.hstgr.io/54b7d1bc1ec58d94/files/public_html/` whenever you push to GitHub.

## Prerequisites

1. **Jenkins Server**: Running Jenkins instance
2. **Required Plugins**:
   - Git plugin
   - Pipeline plugin
   - Email Extension plugin
   - Credentials plugin

## Step 1: Install Jenkins (if not already installed)

### On macOS:
```bash
brew install jenkins-lts
brew services start jenkins-lts
```

### On Ubuntu/Linux:
```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

### Access Jenkins:
- Open browser: `http://localhost:8080`
- Get initial password: `sudo cat /var/lib/jenkins/secrets/initialAdminPassword`

## Step 2: Configure Jenkins

### Install Required Plugins:
1. Go to **Manage Jenkins** → **Manage Plugins**
2. Install these plugins:
   - Git plugin
   - Pipeline plugin
   - Email Extension plugin
   - Credentials plugin
   - Blue Ocean (optional, for better UI)

## Step 3: Set Up Credentials

1. Go to **Manage Jenkins** → **Manage Credentials**
2. Click **Global** → **Add Credentials**
3. Add FTP credentials:
   - **Kind**: Username with password
   - **ID**: `ftp-credentials`
   - **Username**: Your FTP username
   - **Password**: Your FTP password
   - **Description**: FTP Server Credentials

## Step 4: Create Jenkins Job

1. **New Item** → **Pipeline**
2. **Name**: `aiml-portfolio-deploy`
3. **Pipeline Configuration**:
   - **Definition**: Pipeline script from SCM
   - **SCM**: Git
   - **Repository URL**: `https://github.com/abzanganeh/aiml-portfolio.git`
   - **Branch**: `*/main`
   - **Script Path**: `Jenkinsfile`

## Step 5: Configure GitHub Webhook (Optional)

### In GitHub:
1. Go to your repository: `https://github.com/abzanganeh/aiml-portfolio`
2. **Settings** → **Webhooks** → **Add webhook**
3. **Payload URL**: `http://your-jenkins-url:8080/github-webhook/`
4. **Content type**: `application/json`
5. **Events**: Just the push event

### In Jenkins:
1. In your job configuration
2. **Build Triggers** → **GitHub hook trigger for GITScm polling**

## Step 6: Configure Email Notifications (Optional)

1. **Manage Jenkins** → **Configure System**
2. **Extended E-mail Notification**:
   - **SMTP server**: Your email provider's SMTP
   - **Default Recipients**: Your email address
   - Configure authentication if needed

## Step 7: Test the Pipeline

1. Make a small change to your repository
2. Push to the `main` branch
3. Watch Jenkins automatically trigger the build
4. Check the console output for deployment status

## Jenkins Pipeline Features

### Automatic Triggers:
- **GitHub Push**: Deploys on every push to main branch
- **Polling**: Checks for changes every 2 minutes
- **Manual**: Can be triggered manually from Jenkins

### Deployment Process:
1. **Checkout**: Gets latest code from GitHub
2. **Validate**: Checks project structure
3. **Prepare**: Creates clean deployment package
4. **Deploy**: Uploads to your web server via FTP
5. **Verify**: Confirms deployment success
6. **Notify**: Sends email notification

### Security:
- Credentials stored securely in Jenkins
- No passwords in code or logs
- Encrypted connections where possible

## Troubleshooting

### Common Issues:

1. **FTP Connection Failed**:
   - Check server address and credentials
   - Verify firewall settings
   - Test FTP access manually

2. **Git Checkout Failed**:
   - Check repository URL
   - Verify GitHub access
   - Check network connectivity

3. **Permission Denied**:
   - Verify FTP user has write permissions
   - Check target directory exists
   - Confirm server directory structure

### Jenkins Logs:
- Console output in each build
- Jenkins system logs in `/var/log/jenkins/`
- Job-specific logs in Jenkins workspace

## Alternative: Docker Jenkins

If you prefer Docker:

```bash
# Run Jenkins in Docker
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

# Get initial password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

## Benefits of Jenkins vs GitHub Actions

### Jenkins Advantages:
- **Self-hosted**: Complete control over environment
- **Plugins**: Extensive plugin ecosystem
- **Complex Pipelines**: Better for complex deployment scenarios
- **Resource Control**: No usage limits
- **Private Networks**: Can deploy to internal servers

### GitHub Actions Advantages:
- **No Setup**: Hosted by GitHub
- **Integrated**: Native GitHub integration
- **Free Tier**: Generous free usage
- **Maintenance-Free**: No server maintenance needed

## Recommendation

Use **Jenkins** if:
- You have complex deployment requirements
- You need to deploy to multiple environments
- You want full control over the CI/CD environment
- You're deploying to internal/private networks

Use **GitHub Actions** if:
- You want simple, quick setup
- Your deployment is straightforward
- You prefer hosted solutions
- You want minimal maintenance

Both configurations are included in this repository, so you can choose based on your needs!
