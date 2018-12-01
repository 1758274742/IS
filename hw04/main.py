import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,x):
        x = 9 if x == None else int(x)
        y = int(self.get_argument('n',10))
        if  y != 10:
            x = None
        if  0 < y < 10:
            x = y
        html='''
        <html>
        <body>
        <table>
        '''
        for a in range(1,x+1):
            html+='<TR>'
            for b in range(a,x+1):
                html+='<TD>'+'{}*{}={}'.format(a,b,a*b)+'</TD>'
            html+='</TR>'
        html+='''
        </table>
        </body>
        </html>
        '''
        self.write(html)
        
application = tornado.web.Application([
    (r"/([0-9])?", MainHandler),
],debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
