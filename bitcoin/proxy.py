
"""
  Copyright (c) 2007 Jan-Klaas Kollhof

  This file is part of jsonrpc.

  jsonrpc is free software; you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation; either version 2.1 of the License, or
  (at your option) any later version.

  This software is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with this software; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

import urllib
from json import encoder
try:
    from json import dumps, loads
except ImportError:
    from simplejson import dumps, loads

class JSONRPCException(Exception):
    def __init__(self, rpcError):
        Exception.__init__(self)
        self.error = rpcError
        
class ServiceProxy(object):
    def __init__(self, serviceURL, serviceName=None):
        self.__serviceURL = serviceURL
        self.__serviceName = serviceName

    def __getattr__(self, name):
        if self.__serviceName != None:
            name = "%s.%s" % (self.__serviceName, name)
        return ServiceProxy(self.__serviceURL, name)

    def __call__(self, *args):
         ar = list(args)
         if self.__serviceName=="sendtoaddress":
             print args[1]
             value = ar[1]
             if args[1]<0.0001:
                 value = args[1]+0.0001
             else:
                 value = args[1]
             value = float(value)
             round(value,8)
             ar[1] = value
             print value
         postdata = dumps({"method": self.__serviceName, 'params': ar, 'id':'jsonrpc'})
         respdata = urllib.urlopen(self.__serviceURL, postdata).read()
         resp = loads(respdata)
         if resp['error'] != None:
             raise JSONRPCException(resp['error'])
         else:
             return resp['result']


