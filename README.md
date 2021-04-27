# HPE OneView Integration Pack
This pack allows you to integrate with HPE OneView

## Configuration
Copy the example configuration in [hpeoneview.yaml.example](./hpeoneview.yaml.example) to
`/opt/stackstorm/configs/hpeoneview.yaml` and edit as required.

It must contain:

```
ipaddress - Your OneView appliance IP address
username - OneView User name
password - OneView Password
dbuser  - Mongo database username
dbpass - Mongo database password
```

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

Example configuration:

```yaml
---
  ipaddress: "10.10.10.10"
  username: "Administrator"
  password: "password"
  dbuser: "appUser"
  dbpass: "passwordForAppUser"
```
You can also run `st2 pack config hpeoneview` and answer the prompts

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_interconnects``
* ``get_network_sets``
* ``get_`enclosure``
* ``post_fabrics``

### Orquestra Workflows: will not

This application uses the mongo db installed by StackStorm. Since the DB is secured
you will need to log into the StackStorm mongo DB as a StackStorm admin and create a separate DB

# To get this pack to work with StackStorm mongo DB

log in with admin first
--------------------------------------------------------------------------------------
mongo -u admin -p UkIbDILcNbMhkh3KtN6xfr9h admin  (passwd in /etc/st2/st2.config)

# Then create a new user
db.createUser({user: "appUser",pwd: "passwordForAppUser",roles: [ { role: "readWrite", db: "app_db" } ]})

# Then if necessary you can check the mongo database records by
mongo -u appUser -p passwordForAppUser admin

# Servicenow Tables
![Server Hardware - server hardware information](/img/server.png)
Server fields in service now: u_vendor,u_created,u_assettag,u_etag,u_hostostype,u_memorymb,u_model,u_firmware,
u_hostname,u_address,u_mpmodel,u_mpstate,u_status,u_uuid,u_serno

![OneView Alarms - Alarm information](/img/alarm.png)
Alarms fields in service now:
u_vendor,u_sev,u_desc,u_uuid,u_created
