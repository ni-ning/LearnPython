#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import paramiko
from io import StringIO

key_str = """-----BEGIN RSA PRIVATE KEY-----
MIIEoQIBAAKCAQEAw6O03HoOwJcf+NMvadRV4wZZwT5bgr3ZqIUazibzaDqAH5ep
zWD2bmbncVtOWC08+RTzjvbL8IviVrk0Tk57lTniXAHndB2u+sgkc5vT2zbysWHq
tJwalPkZsnecadzAlxLB81Ea60WH9GSrLy7xnDXwlStDYQNo/oza28auU7DRvw8f
tPGQOoCFl/gRiypWFVYzt3wg9EoipBjWbLH5WMZUVajXyVzDYdY2TNGe7KR7spLK
FjqPAc00ecjF7qHH2un/5H4ARlDE5l/U8aJtANMriwxvB/p3wXxTVixCPEYNANdX
wPgTUmJQINad+1FsDa/xkqQsV2E/sROcUtxN8QIBIwKCAQAQxOOd3pOM2cDpcS/z
INQpZvHAG0msHubFTTzP13Py/bM16G2j471Z65AuSaehKHLwx0gTkX8x4Bq2+e6K
Xn+fE5cPM1z7UwBeo3DWtZXQ9hTNYCoPexg4p6Md7P7HPs6t3QlPXrkqG+cU8q+W
VHscBJ+XweE0M34HMKULhg7xOuRMWUWkeAKIECKqt+0DUp1RcMgr0aAH6ONljRwQ
YAU6ALFeLjUPDxcCsk/I6UmWwtYdHHiuWu9Y1efZ3wbNu0TQoIIgh4oqBa8kQGit
KGQTPI0n5zcWLQbor2BALLcZyVlprrgY/RiUh7eeKfEPKuIbtYxK9XeuOHdt6IIl
qm2LAoGBAOF38kPlxJ2V0WcQh5ll8Ui+85X2t9s61zgy+ZSDs5Q8kw10sPg+Bi6M
i358zU25WnNo52OPXqMbrXVqY/+rv+uftY8x3cZYypLkO/AWF0t2tZ5MnLfYpw7P
s07MDN1R8Px9OeMno+K50BNKH0+TS43UxsXmPX2Q8HqeaABZciARAoGBAN4htgSl
tNUb8t9qZABTyoygPtPBi/qygI17Bk/UnigiKzGWMh8w+9211RT9YqFUaPD2CeaU
twOEYC4hkCGNWQ65OS03HZit7owF3x+iCTypsHPCO4nXRhhXIExIFbdoJ/1dUbt1
y2cpDYlMI1IMZuWgTcbsjDqAiKkQaFhB+y/hAoGAemWvZq/uZCzCIgGoslvpYgFC
Z1oMCUvT607fQf5aK+ZedQTVGQu6NobPYev6bAWI35C4IBqhFrdA5/ftJGSMwb0Z
av3QKdht9/g9y3m039K6XT+IRouN43gQ4aH4WuNW73cuDZktFK4DPavlHJHJ7eiJ
KZo+o0ANhGSe255FRJsCgYEA0XA95x/lA3IfgjEcdVZRQsL5aJHqYWZ5NPBWaIaj
v3CsYfQDXzzQN3DtejC8FHQobinO0hcwNoQgK367GFISI9M16M2Q7wpkkqZzSbYI
tYoMxOpVZLUHk0rVTzymwt6MGsWzdjvdCX56eiM3Prs8chrM/WKwGebnQFFMcHi5
oisCgYAYFC96FSx94P1nWZ1wMZtEASSGSlOfAncSOewW99jPOnduiZoukdaQ+SJr
2z56MVYn6TAWCnisSvIrsozrSUWPlPg7jDcka2IQN6EX0uc0f5anShixdG6amj19
dzNQDmpPBmiJmJtSRS/weyOrmLWslmFxdzJozGCAreertkuT5A==
-----END RSA PRIVATE KEY-----"""

private_key = paramiko.RSAKey(file_obj=StringIO(key_str))
transport = paramiko.Transport(('c3.salt.com', 22))
transport.connect(username='root', pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
# 将test.txt上传至服务器 /application/test.txt
sftp.put('test.txt', '/application/test.txt')

# 将/application/test.txt 下载到本地 test01.txt
sftp.get('/application/test.txt', 'test01.txt')
transport.close()

