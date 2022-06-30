# MLOpsLearning

## login to ibm cloud
```
ibmcloud login
```
## If login unsuccessful in previous step, log in with a federated ID, use the --sso
```
ibmcloud login --sso
```
## set region
```
ibmcloud target -r <REGION>
```
## set target cloud foundry
```
ibmcloud target -cf
```
#set org and space, make sure you set the current region id in the cli, you can get organization id and space id from Manage->Account-> Cloud Foundry orgs
```
ibmcloud target -o 'ORGANIZATION_ID' -s 'SPACE_ID'
```
# to deploy the app
```
ibmcloud cf push
```
### after successful deployment log will show you all the information icluding routes to access your model
