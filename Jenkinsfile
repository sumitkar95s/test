node
{
    stage('Git Pull')
    {
        echo "Pulling Code from GIT HUB"
        git 'https://github.com/sumitkar95s/test.git'
    }
    stage('Code build')
    {
        sh 'pip install -r packages.txt'
    }
    stage('Code deploy')
    {
        echo 'Deploying code'
        sh 'python Invoker.py'
        
    }
}
