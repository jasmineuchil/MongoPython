## MongoPython

#Helm installation

For Helm installation please refer https://github.com/redhat-developer/redhat-helm-charts/tree/master/stable/ibm-mongodb-enterprise-helm

After completion of helm installation, validate if chart got installed successfully

```
[root@p1213-bastion cecuser]# helm ls
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /root/.kube/config
NAME                                    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                                APP VERSION
test                                    jas             1               2021-05-18 00:59:07.383811905 -0400 EDT deployed        ibm-mongodb-enterprise-helm-0.1.0    4.4.0
[root@p1213-bastion cecuser]# oc get po
NAME                                                          READY   STATUS    RESTARTS   AGE
test-ibm-mongodb-enterprise-helm-deployment-d6c8b784c-zlxkh   1/1     Running   0          111m
[root@p1213-bastion cecuser]#

```

Expose a node port for the application
```
[root@p1213-bastion templates]# oc expose deployment test-ibm-mongodb-enterprise-helm-deployment --type=NodePort --name=test-ibm
service/test-ibm exposed
[root@p1213-bastion templates]# oc get nodes
NAME                                STATUS   ROLES           AGE   VERSION
p1213-master.p1213.cecc.ihost.com   Ready    master,worker   13d   v1.19.0+a5a0987
[root@p1213-bastion templates]# oc get svc
NAME                                       TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                                                                                                     AGE
test-ibm                                   NodePort       172.30.22.77     <none>        27017:31466/TCP                                                                                             14s
test-ibm-mongodb-enterprise-helm-service   ClusterIP      172.30.78.82     <none>        27017/TCP                                                                                                   85m
```

Git clone this repository on your server -

```
cd $HOME/
git clone https://github.com/jasmineuchil/MongoPython
cd MongoPython
```
After cloning the repository to your system, change hostname and port number for all three `.py` scripts

Run python script `pythoncode.py` which will create a sample data

To validate, login to the container
```
[root@p1213-bastion cecuser]# oc get po
NAME                                                          READY   STATUS    RESTARTS   AGE
test-ibm-mongodb-enterprise-helm-deployment-d6c8b784c-zlxkh   1/1     Running   0          111m

[root@p1213-bastion cecuser]# oc rsh test-ibm-mongodb-enterprise-helm-deployment-d6c8b784c-zlxkh
sh-4.4$ mongo -u myUserAdmin -p password
MongoDB shell version v4.4.4
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("912c934e-bacd-4165-a2b8-f486a2c15019") }
MongoDB server version: 4.4.4
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
        https://docs.mongodb.com/
Questions? Try the MongoDB Developer Community Forums
        https://community.mongodb.com
---
The server generated these startup warnings when booting:
        2021-05-18T04:59:30.390+00:00: Soft rlimits too low
        2021-05-18T04:59:30.390+00:00:         lockedMemoryBytes: 65536
        2021-05-18T04:59:30.390+00:00:         minLockedMemoryBytes: 1048576
---
MongoDB Enterprise > show dbs
admin       0.000GB
business    0.000GB
config      0.000GB
local       0.000GB
newdb       0.000GB
MongoDB Enterprise > use newdb
switched to db newdb
MongoDB Enterprise > show collections
reviews
MongoDB Enterprise > db.reviews.find().count()
100
MongoDB Enterprise >
```
## Server Status Result

To check server status, run `ServerStatusResult.py` script

```
[root@p1213-bastion MongoPython]# python serverstatusresult.py
{'asserts': {'msg': 0, 'regular': 0, 'rollovers': 0, 'user': 14, 'warning': 0},
 'connections': {'active': 2,
                 'available': 838856,
                 'awaitingTopologyChanges': 1,
                 'current': 4,
                 'exhaustHello': 0,
                 'exhaustIsMaster': 0,
                 'totalCreated': 40},
...
...
...
'transaction range of timestamps pinned by the oldest active read timestamp': 0,
                                'transaction range of timestamps pinned by the oldest timestamp': 0,
                                'transaction read timestamp of the oldest active reader': 0,
                                'transaction sync calls': 0,
                                'transactions committed': 348,
                                'transactions rolled back': 1112,
                                'update conflicts': 0},
                'uri': 'statistics:'}}
```

## Database list

To check database list run `dblist.py` script
```
[root@p1213-bastion MongoPython]# python dblist.py
{'name': 'admin', 'sizeOnDisk': 167936.0, 'empty': False}
{'name': 'business', 'sizeOnDisk': 73728.0, 'empty': False}
{'name': 'config', 'sizeOnDisk': 36864.0, 'empty': False}
{'name': 'local', 'sizeOnDisk': 73728.0, 'empty': False}
{'name': 'newdb', 'sizeOnDisk': 139264.0, 'empty': False}
[root@p1213-bastion MongoPython]#
```
