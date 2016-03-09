#!/usr/bin/python

import webapp
import random

class redirect (webapp.webApp):

    def process(self, parsedRequest):
        numero = random.randint(1,10000000)
        returnCode = '300 Found'
        htmlAnswer = '<html><body><head> Redirigiendo a /'
        htmlAnswer += str(numero) + '<meta http-equiv="refresh"'
        htmlAnswer += 'content="6; url=' + str(numero) + '" />'
        return (returnCode, htmlAnswer)

if __name__ == "__main__":
    testWebApp = redirect("localhost", 1235)
