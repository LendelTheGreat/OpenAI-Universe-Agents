# OpenAI-Universe-Agents



## Connect to AWS machine
`ssh -i ~/ssh/AWS_lendo_key.pem ubuntu@ec2-35-167-106-253.us-west-2.compute.amazonaws.com`

## Start docker env
`docker run -p 5900:5900 -p 15900:15900 --cap-add SYS_ADMIN --ipc host --privileged quay.io/openai/universe.flashgames:0.20.21`

## Run agent
`./agents/random_agent.py`

## Observe the results
`http://35.167.106.253:15900/viewer/?password=openai`
