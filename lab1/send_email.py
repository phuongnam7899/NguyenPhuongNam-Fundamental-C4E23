from gmail import GMail, Message
from random import choice
gmail= GMail("nguyenphuongnam7899@gmail.com","namyeuthanh2503")

sickness_list=["mu","diec","cam"]

for i in range(5):
    template = '''<p>chao sep,</p>
<p>hom nay em ngu lam,bac si khong noi gi voi em</p>
<p>em buon lam nen e xin ghi</p>
<p>nhan vien cua sep<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></p>
    '''
    sickness= choice(sickness_list)
    content=template.replace("{{sick}}", sickness)
    message = Message("don xin nghi",to="qhuydtvt@gmail.com",html=content)
    gmail.send(message)