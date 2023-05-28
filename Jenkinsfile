pipeline {
  agent any
  environment {
  AWS_ACCOUNT_ID="659026651741"
  AWS_DEFAULT_REGION="us-east-1" 
  IMAGE_REPO_NAME="asg"
  IMAGE_TAG="latest"
  REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
  }
  tools { 
        maven 'Maven_3_5_2'  
    }        
        stage('Build') {
            steps {
                // Aquí irían los pasos para construir tu proyecto en Python, por ejemplo:
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Snyk Test') {
            steps {
                withCredentials([string(credentialsId: 'SNYK_TOKEN2', variable: 'SNYK_TOKEN2')]) {
                    sh 'snyk test --all-projects --all-branches --org=webodevops --all-issues --json --project-name=fastapi --severity-threshold=high'
                }
            }
        }
	stage('Logging into AWS ECR') {
 		steps {
 			script {
 			sh "sudo aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | sudo docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
 			}
 		}
 	}
 
 	// Building Docker images
	stage('Building image') {
 		steps{
 			script {
 			dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
 			}
 		}
 	}
 
 	// Uploading Docker images into AWS ECR
 	stage('Pushing to ECR') {
 		steps{ 
 			script {
 			sh "docker image tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:${IMAGE_TAG}"
 			sh "docker image push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
 			}
 		}
 	}
	    
	stage('Kubernetes Deployment of Application') {
	   steps {
	      withKubeConfig([credentialsId: 'kubelogin']) {
		  sh ('kubectl delete all --all -n devsecops')
		  sh ('kubectl apply -f fast-api.yaml --namespace devsecops')
		}
	      }
   	}
     }
   
}

