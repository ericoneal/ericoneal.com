#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.api import mail

#http://eaoemail.appspot.com/?FromEmail=me@doodie.com&Message=doodietest
class MainHandler(webapp2.RequestHandler):
    def get(self):

        #Name = self.request.get('Name')
        FromEmail = self.request.get('FromEmail')
        Message = self.request.get('Message')

       

        if((FromEmail == '') or (Message == '')):
            self.response.write("false")
            return 
        
        message = mail.EmailMessage(sender="ericoneal.com <ericonealATgmailDOTcom>", subject="msg from ericoneal.com")

        message.to = "Eric ONeal <ericonealATgmailDOTcom>"
        message.body = """
        From:  """ + FromEmail + """

        """ + Message + """
        """

        message.send()

        self.response.write("true")



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
