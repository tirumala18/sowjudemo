
import json
#call_counter = 0

def replace_string(value: str, template_vars):
    """
    Replaces template strings in value, by the values in template_vars. 
    """
    for template, newValue in template_vars.items():
        #print("${{}}".format(template))
        value = value.replace("${{{}}}".format(template), str(newValue))
        #print(newValue,value)
    if value.isnumeric():
        return int(value)
    return value


def replace_recursive(json_obj: object, template_vars):
    """
    Recursively unpacks and replaces items in a multi-dimensional dict/list/item json object.
    """
    # For each item at this level 
    for key, value in json_obj.items():
        print(key)
        def listing(value):    
            for index, item in enumerate(value):
                # If it's a string, we can replace it 
                if isinstance(item, int):
                    item=str(item)
                elif isinstance(item, str):
                    value[index]= replace_string(item, template_vars)
                # If it's not, we need to do more work. 
                elif isinstance(item,list):
                    value[index]= listing(item)
                else:
                    value[index]= replace_recursive(item, template_vars)
        # If the value is a string, replace it
        if isinstance(value,int):
            value=str(value)
        if isinstance(value, str):
            json_obj[key] = replace_string(value, template_vars)        

        # If the item is a list, we need to do something for each value
        elif isinstance(value, list):
            listing(value)
            # Enumate unpacks an index with each value
        

        # If it's a dict, use this function again to unpack/replace the values
        else:
            json_obj[key] = replace_recursive(value, template_vars)

    return json_obj
if __name__ == "__main__":

    template_vars = {}
    json={}
    # Read our file
  
    # Read our settings
    template_vars = {
  "cluster_name": "#{env | ToLower}-informed-ecs-cluster",
  "OctopusActionTargetRoles": ,
  "taskExecutionRole": ,
  "Inputs.name": ,
  "containerName": ,
  "imageName": ,
  "containerPort": ,
  "protocol": ,
  "securityGroupIds": ,
  "subnetIds": ,
  "tags": ,
  "lb_containerName": ,
  "lb_containerPort": ,
  "lb_argetGroupArn": 
}
    json={
  "Name": "${cluster_name}",
  "PackageRequirement": "AfterPackageAcquisition",
  "Properties": {
    "Octopus.Action.TargetRoles": "${OctopusActionTargetRoles}"
  },
  "Condition": "Success",
  "StartTrigger": "StartAfterPrevious",
  "Actions": [   
    {
      "Name": "Deploy Amazon ECS Service",
      "ActionType": "aws-ecs",
      "Notes": "None",
      "IsDisabled": "false",
      "CanBeUsedForProjectVersioning": "true",
      "IsRequired": "false",
      "WorkerPoolId": "None",
      "Container": {
        "Image": "None",
        "FeedId": "None"
      },
      "WorkerPoolVariable": "",
      "Environments": [],
      "ExcludedEnvironments": [],
      "Channels": [],
      "TenantTags": [],
      "Packages": [
        {
          "Name": "None",
          "PackageId": "None",
          "FeedId": "None",
          "AcquisitionLocation": "NotAcquired",
          "Properties": {
          }
        }
      ],
      "Condition": "Success",
      "Properties": {
      },
      "StepPackageVersion": "1.1.1",
      "LastSavedStepPackageVersion": "1.1.1",
      "Inputs": {
        "name": "${Inputs.name}",
        "containers": [
          {
            "containerName": "${containerName}",
            "containerImageReference": {
              "imageName": "${imageName}",
              "feedId": "None"
            },
            "repositoryAuthentication": {
              "type": "default"
            },
            "memoryLimitSoft": 0,
            "memoryLimitHard": 0,
            "containerPortMappings": [
              {
                "containerPort": "${containerPort}",
                "protocol": "${protocol}"
              }
            ],
            "essential": "true",
            "environmentFiles": [],
            "environmentVariables": [],
            "networkSettings": {
              "disableNetworking": "false",
              "dnsServers": [],
              "dnsSearchDomains": [],
              "extraHosts": []
            },
            "containerStorage": {
              "readOnlyRootFileSystem": "false",
              "mountPoints": [],
              "volumeFrom": []
            },
            "containerLogging": {
              "type": "auto"
            },
            "dockerLabels": [],
            "healthCheck": {
              "command": [],
              "interval": 30,
              "timeout": 5
            },
            "dependencies": [],
            "stopTimeout": 2,
            "ulimits": []
          }
        ],
        "task": {
          "taskExecutionRole": "${taskExecutionRole}",
          "cpu": 1024,
          "memory": 2048,
          "runtimePlatform": {
            "cpuArchitecture": "X86_64",
            "operatingSystemFamily": "LINUX"
          },
          "volumes": []
        },
        "networkConfiguration": {
          "securityGroupIds": "${securityGroupIds}",
          "subnetIds": "${subnetIds}",
          "autoAssignPublicIp": "true"
        },
        "desiredCount": 1,
        "additionalTags": {
          "enableEcsManagedTags": "true",
          "tags": "${tags}"
        },
        "minimumHealthPercent": 100,
        "maximumHealthPercent": 200,
        "waitOption": {
          "type": "waitUntilCompleted"
        },
        "loadBalancerMappings": [
          {
            "containerName": "${lb_containerName}",
            "containerPort": "${lb_containerPort}",
            "targetGroupArn": "${lb_argetGroupArn}"
          }
        ]
      },
      "AvailableStepPackageVersions": [
        "1.1.1"
      ],
      "Links": {
      }
    }
  ]
}



print( replace_recursive(json, template_vars))
    