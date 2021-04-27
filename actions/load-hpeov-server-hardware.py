# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

import pymongo
from lib.actions import MongoBaseAction


class loadDb(MongoBaseAction):
    def run(self, servers):

        mydb = self.dbclient["app_db"]
        known = mydb["ovservers"]

        new_server={}

        for server in servers:
            myquery = { "_id" : server['created'] }
            records = known.find(myquery).count()
            if records == 0:
                new_server['u_vendor']='hpe-oneview'
                new_server['_id']=server['created']
                new_server['u_created']=server['created']
                new_server['u_assettag']=server['assetTag']
                new_server['u_etag']=server['eTag']
                new_server['u_hostostype']=server['hostOsType']
                new_server['u_memorymb']=server['memoryMb']
                new_server['u_model']=server['model']
                new_server['u_firmware']=server['mpFirmwareVersion']
                new_server['u_hostname']=server['mpHostInfo']['mpHostName']
                new_server['u_address']=server['mpHostInfo']['mpIpAddresses'][0]['address']
                new_server['u_mpmodel']=server['mpModel']
                new_server['u_mpstate']=server['mpState']
                new_server['u_status']=server['status']
                new_server['u_uuid']=server['uuid']
                new_server['u_serno']=server['virtualSerialNumber']
                new_server['u_process']='no'
                write_record = known.insert_one(new_server)
                # write_record = process.insert_one(alarm)
        return (records)
