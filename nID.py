class nIDError(value, Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)
def parse(nid,field):
    try:
        split=nid.split("@")
        count=0
        loop=0
        output=""
        for i in field:
            count=count+1
        for i in split:
            if i.startswith(field):
                for u in i:
                    if loop <= count:
                        pass
                    else:
                        output=output+u
                    loop=loop+1
        return output
    except:
        raise nIDError("Could not Parse nid")
